from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    Serializer=URLSafeTimedSerializer('codegnan@123')
    return Serializer.dumps(data,salt=salt)
def decode(data):
    Serializer=URLSafeTimedSerializer('codegnan@123')
    return Serializer.loads(data,salt=salt)