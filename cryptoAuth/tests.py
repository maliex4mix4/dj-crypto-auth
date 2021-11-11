from django.test import TestCase
from django.http import HttpRequest
from .views import confirm_auth_coinbase
from django.test.client import RequestFactory
from django.utils import unittest



class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_alive(self):
        # Create an instance of a GET request.

        request = self.factory.get('/coinbase/confirm_auth')

        # Test my_view() as if it were deployed at /customer/details
        response = confirm_auth_coinbase(request)
        self.assertEqual(response.status_code, 200)