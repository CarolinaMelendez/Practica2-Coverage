import pytest
from Code.juego1 import name_to_number

def test_function():
    answer = name_to_number("rock")
    assert answer == 0