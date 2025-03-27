from user.models import tbl_user
from serializers import UserSerializer
import hashlib
import hmac
from .helpers import generate_salt_key, password_verify
import datetime
from jwt_utils import jwt_instance
from exceptions import ParameterError


def access_token(payload):
    try:
        refresh_token = payload.data.get('refresh')
        if not refresh_token:
            return {'message': 'Refresh token not provided'}, 400
        user_id = jwt_instance.verify_token(refresh_token)
        
        access_token = jwt_instance.create_access_token({'user_id': user_id})
        refresh_token = jwt_instance.create_refresh_token({'user_id': user_id})
        
        return {'access_token': access_token, 'refresh_token': refresh_token}, 200
        
        
    except ParameterError as e:
        print(f"Error while verifying token: {e}")
        return {'message': str(e)}, 400
    
    except Exception as e:
        print(f"Error while verifying token: {e}")
        return {'message': 'Internal Server Error'}, 400

def register_user(payload):
    try:
        user_seriializer = UserSerializer(data=payload)
        if not user_seriializer.is_valid():
            raise ParameterError('Invalid parameters')
        
        is_user_exist = tbl_user.objects.filter(email=payload['email']).exists()
        if is_user_exist:
            return {'message': 'User already exists'}, 400
        
        if not password_verify(payload.get('password')):
            raise ParameterError('Invalid password format')
        
        salt_key = generate_salt_key()
        hashed_password = hmac.new(salt_key.encode(), payload.get('password').encode(), hashlib.sha512).hexdigest()
        
        user_obj = tbl_user(name = payload.get('name'),
                            email = payload.get('email'),
                            password = hashed_password,
                            mobile = payload.get('mobile'),
                            salt_key = salt_key,
                            created_at = datetime.datetime.now(),
                            updated_at = datetime.datetime.now()) 
        
        user_obj.save()

        return {'message': 'User registered successfully'}, 200

    except ParameterError as e:
        return {'message': str(e)}, 400
        
    except Exception as e:
        return {'message': str(e)}, 400
    

def login_user(payload):
    try:
        user_seriializer = UserSerializer(data=payload)
        if not user_seriializer.is_valid():
            raise ParameterError('Invalid parameters')
        
        is_user_exist = tbl_user.objects.filter(email=payload['email']).exists()
        if not is_user_exist:
            return {'message': 'Invalid Email'}, 400
        
        salt_key = tbl_user.objects.get(email=payload['email']).salt_key
        hashed_password = hmac.new(salt_key.encode(), payload.get('password').encode(), hashlib.sha512).hexdigest()
        
        user_obj = tbl_user.objects.get(email=payload['email'], password = hashed_password)
        
        if not user_obj:
            return {'message': 'Invalid Password'}, 400
        
        access_token = jwt_instance.create_access_token({'user_id': user_obj.id})
        refresh_token = jwt_instance.create_refresh_token({'user_id': user_obj.id})
        
        return {'access_token': access_token, 'refresh_token': refresh_token}, 200
        
    except Exception as e:
        return {'message': str(e)}