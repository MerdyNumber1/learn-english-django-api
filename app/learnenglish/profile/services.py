from .models import User


def create_user(username, email, password):
    return User.objects.create_user(username, email, password)


def create_superuser(username, email, password):
    return User.objects.create_superuser(username, email, password)
