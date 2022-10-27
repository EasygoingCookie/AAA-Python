import json
from myadvert import Advert


def test_can_get_title():
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
    assert corgi.title == 'Вельш-корги', (
        'test_can_get_title() works incorrectly'
    )


def test_can_check_title():
    corgi_info = """{
                "price": 1000,
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    try:
        corgi_info_loads = json.loads(corgi_info)
        corgi = Advert(corgi_info_loads)
    except AttributeError as error:
        assert str(error) == 'There is no title attribute'


def test_can_check_negative_price():
    corgi_info = """{
                "title": "Вельш-корги",
                "price": -50,
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    try:
        corgi_info_loads = json.loads(corgi_info)
        corgi = Advert(corgi_info_loads)
    except AttributeError as error:
        assert str(error) == 'Price has negative value'


def test_can_check_empty_price():
    corgi_info = """{
                "title": "Вельш-корги",
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    corgi_info_loads = json.loads(corgi_info)
    corgi = Advert(corgi_info_loads)
    assert corgi.price == 0, (
        'test_can_check_empty_price() works incorrectly'
    )


def test_can_get_address():
    corgi_info = """{
                "title": "Вельш-корги",
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    corgi_info_loads = json.loads(corgi_info)
    corgi = Advert(corgi_info_loads)
    assert corgi.location.address == 'сельское поселение Ельдигинское, поселок санатория Тишково, 25', (
        'test_can_get_address() works incorrectly'
    )


def test_can_get_class():
    corgi_info = """{
                "title": "Вельш-корги",
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    corgi_info_loads = json.loads(corgi_info)
    corgi = Advert(corgi_info_loads)
    assert corgi.class_ == 'dogs', (
        'test_can_get_address() works incorrectly'
    )