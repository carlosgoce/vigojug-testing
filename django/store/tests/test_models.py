from store.models import Author


def test_fullname_is_correctly_displayed():
    author = Author(first_name='Kent', last_name='Beck')
    assert 'Kent Beck' == author.fullname
