from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create Admin group
        self.admin_group = Group.objects.create(name="Admin")

        # Create admin user
        self.admin_user = User.objects.create_user(
            username="admin",
            password="pass123"
        )
        self.admin_user.groups.add(self.admin_group)

        # Create normal user
        self.normal_user = User.objects.create_user(
            username="user",
            password="pass123"
        )

    def test_login_returns_tokens(self):
        response = self.client.post("/test1/api/token/", {
            "username": "admin",
            "password": "pass123"
        }, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_admin_can_access(self):
        refresh = RefreshToken.for_user(self.admin_user)
        access = str(refresh.access_token)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access}"
        )

        response = self.client.post("/test1/admin-test/")
        self.assertEqual(response.status_code, 200)

    def test_normal_user_gets_403(self):
        refresh = RefreshToken.for_user(self.normal_user)
        access = str(refresh.access_token)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access}"
        )

        response = self.client.post("/test1/admin-test/")
        self.assertEqual(response.status_code, 403)

    def test_no_token_gets_401(self):
        response = self.client.post("/test1/admin-test/")
        self.assertEqual(response.status_code, 401)