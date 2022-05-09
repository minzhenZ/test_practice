def find_course(request, headers, json_data):
    response = request.send_requests('api_find_course', headers=headers, json=json_data)
    return response


def save_course(request, headers, json_data):
    response = request.send_requests('api_save_course', headers=headers, json=json_data)
    return response





