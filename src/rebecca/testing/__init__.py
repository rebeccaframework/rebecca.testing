import pytest

@pytest.fixture
def config(request):
    from pyramid import testing
    config = testing.setUp()

    def fin():
        testing.tearDown()

    request.addfinalizer(fin)
    return config
