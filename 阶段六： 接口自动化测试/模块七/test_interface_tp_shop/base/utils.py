import csv
import hashlib
import json
import logging
import os
import time
from logging import handlers


def get_work_path():
    work_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return work_path


def read_json_data(file):
    file = get_work_path() + '/data/' + file

    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        parameterized_data = [data.values() for data in json_data]

    return parameterized_data


def read_csv_data(file):
    file = get_work_path() + '/data/' + file

    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        parameterized_data = tuple(reader)[1:]
        print(parameterized_data)

    return parameterized_data


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    file = get_work_path() + f'/log/log{time.strftime("%Y%M%d%h%m%s", time.localtime())}.log'
    fh = handlers.TimedRotatingFileHandler(file, when='h', interval=24, backupCount=3, encoding='utf-8')
    fmt = '%(levelname)s %(asctime)s %(pathname)s %(lineno)d %(message)s'
    formatter = logging.Formatter(fmt)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger


def encrypt_data(code, data):
    sign = hashlib.md5()
    sign.update((code+data).encode('utf-8'))
    return sign.hexdigest()

