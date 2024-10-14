from django.contrib.auth.backends import ModelBackend
from adopet.models import Tutor

class EmailBackend(ModelBackend):
    """Autentica utilizando o campo `email` em vez de `username`."""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Tutor.objects.get(email=username)
        except Tutor.DoesNotExist:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
