import pytest
from Package.letters import adding_letters

def test_main():
    assert adding_letters('I love', ' rice') == 'I love rice'
    assert adding_letters('Let\'s', 'Gooo!') == "Let'sGooo!"


def test_adding_numbers():
    assert adding_letters(1, 1) == 'Incorrect input. Insert text only.'
    assert adding_letters(1, '2') == 'Incorrect input. Insert text only.'


#Testing if pull requests is checked. 