from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api_yamdb.settings import CODE_LENGTH


EMAIL_SUBJECT = 'Код подтверждения'
EMAIL_MESSAGE = '{}, Ваш код подтверждения: {}'

# Генерация кода подтверждения
def set_code(user):
    user.confirmation_code = get_random_string(
        CODE_LENGTH, '123456789')
    user.save()
    return user.confirmation_code

# TODO Почем не работает???
def send_code(user):

    send_mail(
        subject=EMAIL_SUBJECT,
        message=EMAIL_MESSAGE.format(
            user.username,
            user.confirmation_code
        ),
        from_email=None,
        recipient_list=[user.email]
    )


class APIToken(APIView):

    pass


class APISignUp(APIView):

    pass


class UserViewSet(ModelViewSet):

    pass
