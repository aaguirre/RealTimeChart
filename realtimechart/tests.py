import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_chart(self):
        from .views import home
        request = testing.DummyRequest()
        info = home(request)
