def login(request, params):
    response_json_data = request.send_requests('api_login', params=params)
    return response_json_data


def login_success(request):
    params = {
        "phone": 15321919666,
        "password": "123456"
    }
    response_json_data = login(request, params=params)
    if response_json_data['state'] == 1:
        return response_json_data
    else:
        return None
    