import logging

from lxml import etree

from base.utils import get_work_path


class Apis:

    def __init__(self, session=None):
        self.session = session

        self.tree = etree.parse(get_work_path() + "/config.xml")
        self.base_url = self.tree.xpath('//api/host/text()')[0] + self.tree.xpath('//api/base_url/text()')[0]
        self.content_type = self.tree.xpath('//api//content-type/text()')[0] + ';charset=utf-8;'

    def parse_url(self, key_url):
        url = self.tree.xpath(f'//{str(key_url)}/text()')[0]
        method = self.tree.xpath(f'//{str(key_url)}/@method')[0]
        return url, method

    def send_requests(self, key_url, headers=None, params=None, data=None, json=None):
        url, method = self.parse_url(key_url)
        url = self.base_url + url

        if params is not None and params != {}:
            url += '?'
            str_params = ''
            for k, v in params.items():
                if str_params != '':
                    str_params += '&'
                str_params += f'{k}={v}'
            url = url + str_params

        response = None
        if method == 'get':
            response = self.session.get(url=url, headers=headers)
        elif method == 'post':
            response = self.session.post(url=url, headers=headers, json=json, data=data)
        else:
            logging.error('无法解析，请检查xml文件')
            return response

        if 'text/html' in response.headers['Content-Type']:
            return response.json()
        else:
            return response


