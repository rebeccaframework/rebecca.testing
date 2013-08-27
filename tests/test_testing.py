from pyramid import testing
from rebecca.testing import config


class DummyView(object):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        from pyramid.httpexceptions import HTTPFound
        return HTTPFound(self.request.route_url("testing"))


def test_it(config):
    config.add_route("testing", "/this/is/testing")

    request = testing.DummyRequest()
    view = DummyView(request)
    res = view()

    assert res.location == 'http://example.com/this/is/testing'