from django.contrib.auth.models import BaseUserManager
from user.utils import validate_password, ERROR_MESSAGE


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have email address!')
        if not password:
            raise ValueError('Users must have a password!')
        if not validate_password(password):
            raise ValueError(ERROR_MESSAGE)
        else:
            user = self.model(
                email=self.normalize_email(email),
            )
            user.is_active = is_active
            user.is_staff = is_staff
            user.is_admin = is_admin
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
