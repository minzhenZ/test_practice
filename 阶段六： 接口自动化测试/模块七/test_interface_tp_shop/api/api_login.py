from base.cases import Cases


class ApiLogin(Cases):

    def get_verify_for_login(self):
        response_json_data = self.request.send_requests('api_verify_login_params')
        return response_json_data

    def login(self, data):
        response_json_data = self.request.send_requests('api_login_params', headers=self.headers, data=data)
        return response_json_data
    