from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from {{ project_name }}.app_name.models import Status, Address


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ExampleAddressSerializer(ModelSerializer):
    status = StatusSerializer(many=False, read_only=True)
    created_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Address
        fields = (
            'address',
            'number',
            'postal_code',
            'complement',
            'neighborhood',
            'city',
            'state',
            'type',
            'created_by',
            'default',
            'status',
            'created_at',
            'updated_at'
        )