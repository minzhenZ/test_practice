from base.cases import Cases


class ApiRegister(Cases):

    def get_verify_for_register(self):
        response_json_data = self.request.send_requests('api_verify_reg_params')
        return response_json_data

    def register(self, data):
        response_json_data = self.request.send_requests('api_reg', headers=self.headers, data=data)
        return response_json_data


