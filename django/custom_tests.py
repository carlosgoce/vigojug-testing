if __name__ == '__main__':
    import os, django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
    django.setup()

    from store.models import Author

    author = Author(first_name='Kent', last_name='Beck')
    assert 'Kent Beck' == author.fullname


    print('Todo correcto')
