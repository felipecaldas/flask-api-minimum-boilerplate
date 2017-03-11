import pytest
from app import create_app


@pytest.fixture(scope='module')
def app(request):
    app = create_app('local')
    ctx = app.app_context()

    ctx.push()

    def tear_down():
        ctx.pop()

    request.addfinalizer(tear_down)
    return app


@pytest.fixture
def client(app):
    return app.test_client()