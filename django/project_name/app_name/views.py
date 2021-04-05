import logging

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from {{ project_name }}.app_name.filters import ExampleFilter, ExamplePagination
from {{ project_name }}.app_name.serializers import ExampleAddressSerializer
from {{ project_name }}.app_name.models import Address

logger = logging.getLogger('infologger')


class ExampleViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = ExampleAddressSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExampleFilter
    lookup_field = 'tag__string'
    pagination_class = ExamplePagination

    def function_example(self, request, *args, **kwargs):
        data = request.data
        try:
            # do something...
            print(data)
            logger.info('printing from function_example')
            # return Response(ExampleAddressSerializer(delivery).data, status=200)
            return Response({}, status=200)

        except Exception as e:
            logger.error('Error from function_example')
            Response(data={'detail': 'error trying to include a driver', 'error': f'{e}'}, status=400)
