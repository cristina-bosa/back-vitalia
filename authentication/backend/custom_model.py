from django.contrib.auth.backends import ModelBackend

from authentication.models import User


class CustomModel(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

