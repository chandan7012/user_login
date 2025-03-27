from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from jwt_utils import jwt_instance 
from .models import tbl_user

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")

        if not token:
            return None  
        try:
            user_id = jwt_instance.verify_token(token)
            user = tbl_user.objects.get(id=user_id)  
            return (user, None)
        except Exception as e:
            raise AuthenticationFailed(str(e))
