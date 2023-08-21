"""Utility operations"""
from django.db.models import Max

# Models
from frida_ayala.payments.models import Payment


def generate_reference_number():
    # Get the latest reference number from the database
    latest_reference = Payment.objects.aggregate(latest=Max('id'))

    latest_reference_number = Payment.objects.get(id=latest_reference['latest']).id if latest_reference['latest'] else 0

    # Generate the new reference number based on the previous one
    new_number = str(latest_reference_number + 1).zfill(6)[:6]

    return new_number
