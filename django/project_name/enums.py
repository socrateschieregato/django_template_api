from enum import Enum


class EnumDatabaseChoicesMixin(Enum):

    @classmethod
    def get_database_choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_database_max_length(cls):
        return max(len(item.value) for item in cls)

    @classmethod
    def get_database_choices_tuple(cls):
        return [(key.value[0], key.value[1]) for key in cls]

    @classmethod
    def get_database_max_length_tuple(cls):
        return max(len(item.value[0]) for item in cls)

    @classmethod
    def get_database_choices_label_tuple(cls):
        return [(key.value[1], key.value[0]) for key in cls]

    @classmethod
    def get_database_max_length_label_tuple(cls):
        return max(len(item.value[1]) for item in cls)