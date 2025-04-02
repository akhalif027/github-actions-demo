import pytest 
from Package.letters import adding_letters

def test_main(a: str, b: str):
    assert adding_letters('I love', ' rice') == 'I love rice'
    assert adding_letters('Let\'s', 'Gooo!') == "Let'sGooo!"


def test_adding_numbers(a: int, b: int):
    assert adding_letters(1, 1) != 2 
    assert adding_letters(10,10) != 20



