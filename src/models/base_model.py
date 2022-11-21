import abc
from collections import namedtuple
import datetime
import json

Field = namedtuple("Field", "key type setter")


class BaseModel(object, metaclass=abc.ABCMeta):
    hash_exclude_fields = {}
    TABLE: str = None
    fields = {}

    TypeMapping = namedtuple("TypeMapping", "default_value")

    default_value = {
        "str": TypeMapping(default_value=""),
        "int": TypeMapping(default_value=-1),
        "numeric": TypeMapping(default_value=None),
        "boolean": TypeMapping(default_value=False),
        "date": TypeMapping(default_value=""),
        "tstzrange": TypeMapping(default_value=None),
        "timestampz": TypeMapping(default_value=None)
    }

    def __hash__(self):
        #TODO: to be implemented
        pass

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        for field in self.fields:
            if self.__dict__[field] != other.__dict__[field]:
                return False
        return True

    def __str__(self):
        return "{}({})".format(self.get_simple_name(), self.to_json())

    @classmethod
    def get_simple_name(cls):
        return cls.__name__

    def to_json(self, excluded_fields=None):
        def __converter(value):
            if isinstance(value, datetime.date):
                return value.__str__()

        if excluded_fields is None:
                excluded_fields = {}
        values = self.__dict__.copy()

        for field in excluded_fields:
            del values[field]
        return json.dumps(values, default=__converter)

    def from_json(self):
        #TODO Implement it.
        pass

    def hash(self, excluded_fields):
        # TODO: to be implemented
        pass



