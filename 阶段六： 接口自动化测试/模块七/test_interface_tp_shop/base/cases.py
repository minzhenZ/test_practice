import json
import logging
import unittest
import requests

from base.apis import Apis


class Cases(unittest.TestCase):
    request = None
    headers = {}

    def init_request_without_authorization(self) -> None:
        session = requests.session()
        self.request = Apis(session)
        self.headers = {
            "Content-Type": self.request.content_type
        }

    def assertion_equals_expected(self, response, case_name, expected):
        logging.info(case_name)
        logging.info(response)
        self.assertEqual(response['msg'], expected)
