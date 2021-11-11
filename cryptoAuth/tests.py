from django.test import TestCase
from django.http import HttpRequest
from .views import confirm_auth_coinbase
from django.test.client import RequestFactory
from django.urls import resolve
import unittest



class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def coinbase_test_alive(self):
        # Create an instance of a GET request
        found = resolve('/auth/coinbase/confirm_auth')

        self.assertEqual(found.func, confirm_auth_coinbase)

    def url_working(self):
        # Create an instance of a GET request.

        request = self.factory.get('/coinbase/confirm_auth', {'code': '2835a679ed4847ddc3357612e9fd984839a076a02ac1c60cc44ca00f15a46406'}, HTTP_HOST='127.0.0.1')

        # Test my_view() as if it were deployed at /customer/details
        response = confirm_auth_coinbase(request)
        self.assertEqual(response.status_code, 200)