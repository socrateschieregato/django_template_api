import django_filters
from rest_framework.pagination import LimitOffsetPagination

from {{ project_name }}.app_name.models import Address


class ExampleFilter(django_filters.FilterSet):
    created_at__gte = django_filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Address
        fields = [
            'created_by'
        ]


class ExamplePagination(LimitOffsetPagination):
    default_limit = 10
