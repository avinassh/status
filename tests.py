# -*- coding: utf-8 -*-

import unittest

import status


class HTTPStatusCodeTest(unittest.TestCase):
    def test_200_ok(self):
        self.assertEqual(status.HTTP_200_OK, 200)


if __name__ == "__main__":
    unittest.main()
