from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        #print("COOKIE:", raw_token)

        # 1️⃣ Try default header authentication
        header = self.get_header(request)
        if header is not None:
            return super().authenticate(request)

        # 2️⃣ Try cookie authentication
        raw_token = request.COOKIES.get("access_token")
        print("COOKIE:", raw_token)

        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token")

        return self.get_user(validated_token), validated_token