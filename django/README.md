# VIGOJUG TESTING

TODO:

Organización de Tests a libre albedrío versus imitando la organización de carpetas

- Presentación.
- Tests artesanos (custom_tests.py)
- xUnit
    - https://en.wikipedia.org/wiki/JUnit
    - https://en.wikipedia.org/wiki/XUnit
    - python unittest https://docs.python.org/3/library/unittest.html (tests.py)
- Assertions
  - https://phpunit.de/manual/current/en/appendixes.assertions.html
  - https://github.com/rspec/rspec-expectations
  - https://docs.pytest.org/en/latest/assert.html

- Métodos. CamelCase vs SnakeCase vs Rspec + Organización
  - https://github.com/spring-projects/spring-framework/blob/master/spring-webmvc/src/test/java/org/springframework/web/servlet/mvc/method/RequestMappingInfoTests.java#L196
  - https://github.com/django/django/blob/master/tests/requests/tests.py#L614
  - https://github.com/phanan/koel/blob/master/tests/Unit/Services/iTunesTest.php#L11
  - https://github.com/laravel/framework/blob/56a58e0fa3d845bb992d7c64ac9bb6d0c24b745a/tests/Database/SeedCommandTest.php
  - https://github.com/prawnpdf/prawn/blob/master/spec/prawn/text/box_spec.rb#L208
- Pytest
    - test_models.py
- Injección de dependencias
    - https://es.wikipedia.org/wiki/Inyección_de_dependencias
    - Seller.objects (https://github.com/django/django/blob/master/django/db/models/base.py#L341)

- Mocks
  - https://es.wikipedia.org/wiki/Objeto_simulado
  - http://www.phpspec.net/en/stable/manual/prophet-objects.html#stubs
  - test_mocks.py
  - test_services.py
- Integración Contínua y Cobertura
  - https://travis-ci.org/initios/aeat-web-services/jobs/343838773
