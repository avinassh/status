# -*- coding: utf-8 -*-

import unittest

import status
from status import InvalidHTTPStatusCode


class HTTPStatusCodeTest(unittest.TestCase):

    def test_is_informational(self):
        self.assertTrue(status.is_informational(105))

    def test_is_success(self):
        self.assertTrue(status.is_success(202))

    def test_is_redirect(self):
        self.assertTrue(status.is_redirect(304))

    def test_is_client_error(self):
        self.assertTrue(status.is_client_error(403))

    def test_is_server_error(self):
        self.assertTrue(status.is_server_error(500))

    def test_200_ok(self):
        self.assertEqual(status.HTTP_200_OK, 200)

    # Dummy tests. 
    def test_all(self):
        for k,v in vars(status).items():
            self.assertEqual(vars(status).get(k), v)
    
    def test_invalid_http_status_code(self):
        with self.assertRaises(InvalidHTTPStatusCode):
            status.describe(777)
    
if __name__ == "__main__":
    unittest.main()
