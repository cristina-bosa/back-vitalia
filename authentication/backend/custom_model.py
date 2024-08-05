from django.contrib.auth.backends import ModelBackend

from authentication.models import User


class CustomModel(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Exception as e:
            return None

