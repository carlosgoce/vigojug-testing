import pytest

from store.models import Author


def test_fullname_is_correctly_displayed():
    author = Author(first_name='Kent', last_name='Beck')
    assert 'Kent Beck' == author.fullname


@pytest.mark.parametrize('first,last,result', [
    ('Kent', 'Beck', 'Kent Beck'),
    ('Martin', 'Fowler', 'Martin Fowler'),
    # Add missing cases
])
def test_fullname(first, last, result):
    author = Author(first_name=first, last_name=last)
    assert result == author.fullname


# def test_validate_credit_card():
#     tdd
