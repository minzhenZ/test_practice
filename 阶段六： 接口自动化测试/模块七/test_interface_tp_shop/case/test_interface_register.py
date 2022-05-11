from parameterized import parameterized

from api.api_register import ApiRegister
from base.mysql import MysqlRequest
from base.utils import encrypt_data, read_csv_data


class TestInterfaceRegister(ApiRegister):
    msr = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.msr = MysqlRequest()
        cls.msr.backup_db(table_name='tp_users')
        
    def setUp(self) -> None:
        self.init_request_without_authorization()
        self.get_verify_for_register()
        self.msr.init_db()

    @parameterized.expand(read_csv_data('data_register.csv'))
    def test_register_with_params(self, case_name, user_name, pwd, verify_code, auth_code, msg):

        sign = encrypt_data(auth_code, pwd)
        data = f'auth_code={auth_code}' + '&' + f'username={user_name}' + '&' + f'verify_code={verify_code}' \
               + '&' + f'password={sign}' + '&' + f'password2={sign}'
        response = self.register(data.encode('utf-8'))
        self.assertion_equals_expected(response, case_name, msg)

    @parameterized.expand([('两次密码不一致', '15321919666', '123456', '两次密码不一致')])
    def test_register_without_confirm_pwd(self, case_name, user_name, pwd, msg):

        sign = encrypt_data('TPSHOP', pwd)
        data = 'auth_code=TPSHOP' + '&' + f'username={user_name}' + '&' + f'verify_code=8888' \
               + '&' + f'password={sign}'
        response = self.register(data.encode('utf-8'))
        self.assertion_equals_expected(response, case_name, msg)

    @parameterized.expand([('账号已存在', '15321919666', '123456', '账号已存在')])
    def test_register_user_already_exist(self, case_name, user_name, pwd, msg):

        sign = encrypt_data('TPSHOP', pwd)
        data = 'auth_code=TPSHOP' + '&' + f'username={user_name}' + '&' + f'verify_code=8888' \
               + '&' + f'password={sign}' + '&' + f'password2={sign}'

        response = self.register(data.encode('utf-8'))
        self.assertion_equals_expected(response, '注册成功', '注册成功')

        self.init_request_without_authorization()
        self.get_verify_for_register()
        response = self.register(data)
        self.assertion_equals_expected(response, case_name, msg)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.msr.reduce_db()
