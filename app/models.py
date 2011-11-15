from mongoengine import *
from hashlib import sha256

class User(Document):
    username = StringField(required=True, unique=True)
    name = StringField(required=True)
    email = EmailField(required=True)
    password = BinaryField(required=True)
    site = URLField()
    authenticated = BooleanField(default=False)
    active = BooleanField(default=True)
    def set_password(self, password):
        self.password = "{SHA}" + sha256(password).digest()
    def check_password(self, password):
        return sha256(password).digest() == self.password[5:]
    def is_authenticated(self):
        return self.authenticated
    def is_active(self):
        return self.active
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.username