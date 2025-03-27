import jwt
import datetime
from config import get_config
from exceptions import AuthorizationError

config = get_config()

class JWT:
    def __init__(self, secret_key, algorithm):
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def create_access_token(self, data: dict, expires_delta: int = 1):
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=expires_delta)
        data.update({"exp": expire})
        return jwt.encode(data, self.secret_key, algorithm=self.algorithm)

    def create_refresh_token(self, data: dict, expires_delta: int = 7):
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=expires_delta)
        data.update({"exp": expire})
        return jwt.encode(data, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token):
        try:
            if not token:
                raise AuthorizationError("Token not provided")
            
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            raise AuthorizationError("Token expired")
        except jwt.InvalidTokenError:
            raise AuthorizationError("Invalid token")

jwt_instance = JWT(secret_key=config.SECRET_KEY, algorithm=config.ALGORITHM)