from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        return request.COOKIES.get('jwt')

    def get_raw_token(self, header):
        return header
