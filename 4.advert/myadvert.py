# Реализация класса Advert
import json
from keyword import iskeyword
import functools


class JsonToPyobject:
    """From json to python object"""
    def __init__(self, json_object: dict):
        for key, value in json_object.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                setattr(self, key, JsonToPyobject(value))
            else:
                setattr(self, key, value)


class ColorizeMixin:
    """"""
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.__repr__ = cls._replace_repr(cls.__repr__)

    @classmethod
    def _replace_repr(cls, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f'\033[1;{str(cls.repr_color)};40m{text}\033[1;0;40m'
        return wrapper


class Advert(ColorizeMixin, JsonToPyobject):
    """My advert"""
    repr_color = 33

    def __init__(self, json_object: dict):
        super().__init__(json_object)
        if not hasattr(self, 'title'):
            raise AttributeError('There is no title attribute')
        if not hasattr(self, 'price'):
            self.price = 0
        elif self.price < 0:
            raise AttributeError('Price has negative value')

    def __repr__(self):
        return f'{self.title} | {self.price} RUB'


if __name__ == '__main__':
    corgi_info = """{
                    "title": "Вельш-корги",
                    "price": 1000,
                    "class": "dogs",
                    "location": {
                        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                    }
                }"""
    corgi_info_loads = json.loads(corgi_info)
    corgi = Advert(corgi_info_loads)
    print(corgi)
    print(corgi.class_)
    print(corgi.title)
    print(corgi.location.address)
