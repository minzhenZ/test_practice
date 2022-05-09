import logging
import unittest
import jsonpath
import requests

from api import api_login
from base.apis import Apis


class Cases(unittest.TestCase):
    request = None
    Authorization = None
    headers = {}

    @classmethod
    def init_request_with_authorization(cls) -> None:
        session = requests.session()
        cls.request = Apis(session)

        response = api_login.login_success(cls.request)
        if response is not None:
            cls.Authorization = ''.join(jsonpath.jsonpath(response, '$..access_token'))

        cls.headers = {
            "Authorization": cls.Authorization,
            "Content-Type": cls.request.content_type
        }

    def init_request_without_authorization(self) -> None:
        session = requests.session()
        self.request = Apis(session)

    def assertion_equals_expected(self, response, case_name, expected):
        logging.info(case_name)
        logging.info(response)
        self.assertEqual(response['state'], expected)
