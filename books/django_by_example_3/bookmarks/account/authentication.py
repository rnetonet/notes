from django.contrib.auth import get_user_model

class EmailAuthBackend:
    """
    Allow user to authenticate using e-mail and password
    """
    def authenticate(self, requer, username=None, password=None):
        try:
            User = get_user_model()
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
