from datetime import datetime, timedelta

from django.core.exceptions import ValidationError


def validate_birth_date(value):
    if value >= datetime.date(datetime.today()):
        raise ValidationError(f'{value} is not a valid date!')


def validate_event_time(value):
    if value <= datetime.date(datetime.today() + timedelta(days=14)):
        raise ValidationError(f'{value} is not a valid date,the show must be at least in 2 weeks')


def validate_price_amount(value):
    if value < 0:
        raise ValidationError(f'{value} is not a valid amount for a price')


def validate_ticket_stock(value):
    if value < 0:
        raise ValidationError(f'The stock must be greater than 0')
