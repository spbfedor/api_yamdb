from django.utils import timezone

from django.core.exceptions import ValidationError


def validate_not_future_year(value):
    todays_year = timezone.now().year
    if value > todays_year:
        raise ValidationError(
            f'Год выпуска {value} не должен быть больше '
            f'текущего {todays_year} года'
        )
    return value
