import pytest
from src.base_utils import StringConversion

def test_camel_to_snake():
    assert StringConversion.camel_to_snake("chetnaChaudhari") == "chetna_chaudhari"

def test_snake_to_camel():
    assert StringConversion.snake_to_camel('chetna_chaudhari') == "chetnaChaudhari"
    