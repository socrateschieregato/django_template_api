from {{ project_name }}.enums import EnumDatabaseChoicesMixin


STATES = [
  ("SP", "São Paulo"),
]


class StatusExampleEnum(EnumDatabaseChoicesMixin):
    ACTIVE = ('active', 'ativo')
    INACTIVE = ('inactive', 'inativo')


class PaymentMethodExampleEnum(EnumDatabaseChoicesMixin):
    CASH = 'cash'
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'


class AddressTypeEnum(EnumDatabaseChoicesMixin):
    HOME = ("home", "Residencial")
    JOB = ("job", "Comercial")