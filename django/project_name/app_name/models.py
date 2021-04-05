from django.conf import settings
from django.db import models


from {{ project_name }}.app_name.enums import STATES, AddressTypeEnum, StatusExampleEnum


class Status(models.Model):
    description = models.CharField(
        'Status',
        choices=StatusExampleEnum.get_database_choices_tuple(),
        max_length=StatusExampleEnum.get_database_max_length_tuple(),
    )
    label = models.CharField(
        choices=StatusExampleEnum.get_database_choices_label_tuple(),
        max_length=StatusExampleEnum.get_database_max_length_label_tuple(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Address(models.Model):
    address = models.CharField('Endereço', max_length=100)
    number = models.IntegerField('Número')
    postal_code = models.CharField('CEP', max_length=100)
    complement = models.CharField('Complemento', max_length=100, null=True, blank=True, default='')
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', choices=STATES, max_length=50)
    type = models.CharField(
        'Tipo',
        choices=AddressTypeEnum.get_database_choices_tuple(),
        max_length=AddressTypeEnum.get_database_max_length_tuple(),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    default = models.BooleanField('Padrão', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('address', 'number', 'postal_code', 'city', 'complement')

    def __str__(self):
        return f'{self.address}, {self.number}, {self.city}'
