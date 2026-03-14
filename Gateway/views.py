from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, Order, Transaction

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):

    product_id = request.data.get("product_id")

    # 1️⃣ Get product
    product = Product.objects.get(id=product_id)

    # 2️⃣ Create order
    order = Order.objects.create(
        user=request.user,
        product=product,
        price_at_purchase=product.price
    )

    # 3️⃣ Create Stripe Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": product.name,
                },
                "unit_amount": int(product.price * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://localhost:8000/payment-success/",
        cancel_url="http://localhost:8000/payment-cancel/",
        metadata={
            "order_id": order.id
        }
    )

    # 4️⃣ Return checkout URL
    return Response({
        "checkout_url": session.url
    })


############ webhook successful ################


@api_view(["POST"])
@permission_classes([])
def stripe_webhook(request):

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return Response(status=400)
    except stripe.error.SignatureVerificationError:
        return Response(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session["metadata"]["order_id"]

        order = Order.objects.get(id=order_id)

        Transaction.objects.create(
            order=order,
            gateway="stripe",
            transaction_id=session["payment_intent"],
            amount=order.price_at_purchase,
            status="SUCCESS"
        )

        order.status = "PAID"
        order.save()

    return Response(status=200)

########### celery task for sending email ################
from .tasks import send_welcome_email

send_welcome_email.delay("salamlakhan7@gmail.com")