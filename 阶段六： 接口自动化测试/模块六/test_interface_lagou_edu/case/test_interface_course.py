import json
from api.api_course import save_course, find_course
from base.cases import Cases
from parameterized import parameterized

from base.mysql import MysqlRequest
from base.utils import get_work_path


class TestInterfaceCourse(Cases):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mysql_request = MysqlRequest()
        cls.mysql_request.backup_db('course')
        cls.init_request_with_authorization()

    @parameterized.expand([('查询所有课程', 200)])
    def test_find_all_course(self, case_name, status):
        json_data = {}
        response = find_course(self.request, self.headers, json_data)
        self.assertion_equals_expected(response, case_name, status)

    @parameterized.expand([('根据名称查询课程', "自动化测试", 200)])
    def test_find_course_by_name(self, case_name, course_name, status):

        json_data = {
            "courseName": course_name
        }
        response = find_course(self.request, self.headers, json_data)
        self.assertion_equals_expected(response, case_name, status)

    @parameterized.expand([('新建课程', '全栈开发工程师', 200)])
    def test_save_course(self, case_name, course_name, status):

        file = get_work_path() + '/data/data_save_course.json'
        with open(file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        self.mysql_request.init_db()
        response = save_course(self.request, self.headers, json_data)
        self.assertion_equals_expected(response, case_name, status)

        self.mysql_request.connect_db()
        result = self.mysql_request.query_data(f"select course_name from course where course_name = '{course_name}';")
        self.assertIn(course_name, str(result))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql_request.close_db()
        cls.mysql_request.reduce_db()



