from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request

from main.serializers import EqptTypeSerializer, EqptSerializer
from main.models import EqptType, Eqpt


@api_view(["GET"])
def health(request):
    """
    Check health
    """
    return Response({"I'm OK"})


class EqptTypeListView(mixins.ListModelMixin, generics.GenericAPIView):
    """EqptType"""

    # permission_classes = [IsAuthenticated]
    serializer_class = EqptTypeSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """фильтрую

        /?mask={mask} Маска серийного номера
        """

        queryset = EqptType.objects.all()

        mask = self.request.query_params.get("mask")

        if mask:
            queryset = queryset.filter(mask=mask)

        return queryset

    def get(self, request: Request, *args, **kwargs):
        """Обработка get запроса"""

        return self.list(request, *args, **kwargs)


class EqptListView(mixins.ListModelMixin, generics.GenericAPIView):
    """Eqpt"""

    # permission_classes = [IsAuthenticated]
    serializer_class = EqptSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Eqpt.objects.filter(deleted=False)

    def get(self, request: Request, *args, **kwargs):
        """Обработка get запроса"""

        return self.list(request, *args, **kwargs)


class EqptView(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    """Eqpt"""

    # permission_classes = [IsAuthenticated]
    serializer_class = EqptSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Eqpt.objects.filter(deleted=False)

    def perform_destroy(self, instance: Eqpt):
        """мягкое удаление"""
        instance.deleted = True
        instance.save(update_fields=["deleted"])
