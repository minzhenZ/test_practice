from parameterized import parameterized
from api.api_login import login
from base.cases import Cases
from base.utils import read_json_data


class TestInterfaceLogin(Cases):

    def setUp(self) -> None:
        self.init_request_without_authorization()

    @parameterized.expand(read_json_data('data_login.json'))
    def test_params_login(self, case_name, phone, pwd, status):
        params = {
            "phone": phone,
            "password": pwd
        }
        response = login(self.request, params)
        self.assertion_equals_expected(response, case_name, status)

    @parameterized.expand([('无参数', 206)])
    def test_login_with_no_params(self, case_name, status):
        params = {
        }
        response = login(self.request, params)
        self.assertion_equals_expected(response, case_name, status)

    @parameterized.expand([("多余参数", 15321919666, "123456", "多余参数值", 1)])
    def test_login_with_much_params(self, case_name, phone, pwd, redundant_param, status):
        params = {
            "phone": phone,
            "password": pwd,
            "redundant_param": redundant_param
        }
        response = login(self.request, params)
        self.assertion_equals_expected(response, case_name, status)




