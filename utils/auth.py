import datetime
import jwt
from config import Config


def generate_jwt_token(user_id, email, role):
    payload = {
        'sub': user_id,
        'email': email,
        'rol': role,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=Config.JWT_EXPIRATION_SECONDS)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')


def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado')
    except jwt.InvalidTokenError:
        raise Exception('Token inválido')
