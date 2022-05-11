from parameterized import parameterized
from api.api_login import ApiLogin
from base.mysql import MysqlRequest
from base.utils import read_csv_data


class TestInterfaceLogin(ApiLogin):

    msr = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.msr = MysqlRequest()
        cls.msr.backup_db(table_name='tp_users')
        cls.msr.init_db(init_file='init_login.sql')

    def setUp(self) -> None:
        self.init_request_without_authorization()
        self.get_verify_for_login()

    @parameterized.expand(read_csv_data('data_login.csv'))
    def test_login_with_params(self, case_name, phone, pwd, verify, msg):
        data = f'username={phone}&password={pwd}&verify_code={verify}'
        response = self.login(data.encode('utf-8'))
        self.assertion_equals_expected(response, case_name, msg)

    @parameterized.expand([('无参数', '验证码错误')])
    def test_login_with_no_params(self, case_name, msg):
        response = self.login(None)
        self.assertion_equals_expected(response, case_name, msg)

    @parameterized.expand([("多余参数", 15321919666, "123456", "多余参数值", '登陆成功')])
    def test_login_with_much_params(self, case_name, phone, pwd, redundant_param, msg):
        data = f'username={phone}&password={pwd}&verify_code=8888&redundant_param={redundant_param}'
        response = self.login(data.encode('utf-8'))
        self.assertion_equals_expected(response, case_name, msg)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.msr.reduce_db()


