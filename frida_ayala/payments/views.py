"""Payments views"""
# Django
from rest_framework import viewsets, status
from rest_framework.decorators import action
# DRF
from rest_framework.response import Response


class PaymentsViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['post'], url_path='done')
    def payment_done(self, request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='cancel')
    def payment_cancel(self, request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)
