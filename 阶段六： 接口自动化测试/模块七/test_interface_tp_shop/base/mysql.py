import logging
import os
import pymysql as pymysql
from lxml import etree
from base.utils import get_work_path


class MysqlRequest:

    conn = None
    csr = None

    def __init__(self):
        tree = etree.parse(get_work_path() + "/config.xml")
        self.host = tree.xpath('//sql/host/text()')[0]
        self.port = int(tree.xpath('//sql/port/text()')[0])
        self.database = tree.xpath('//sql/database/text()')[0]
        self.user = tree.xpath('//sql/user/text()')[0]
        self.password = tree.xpath('//sql/password/text()')[0]

        self.sub_system_order = ' -h' + self.host + ' -P' + str(self.port) + ' -u' + \
                                self.user + ' -p' + self.password + ' ' + self.database

    def connect_db(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            charset='utf8',
            user=self.user,
            password=self.password
        )

    def query_data(self, sql):
        self.csr = self.conn.cursor()
        self.csr.execute(sql)
        result = self.csr.fetchall()
        self.csr.close()
        return result

    def modify_data(self, sql):
        self.csr = self.conn.cursor()
        try:
            self.csr.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error("捕获异常", e.args)
            self.conn.rollback()
        finally:
            self.csr.close()

    def close_db(self):
        self.conn.close()

    def backup_db(self, table_name='', backup_file='backup.sql'):
        backup_file = get_work_path() + '/sql/' + backup_file
        order = 'mysqldump --ssl-mode=disabled --column-statistics=0' + \
                self.sub_system_order + ' ' + table_name + '>' + backup_file
        os.system(order)

    def init_db(self, init_file='init.sql'):
        init_file = get_work_path() + '/sql/' + init_file
        order = 'mysql --ssl-mode=disabled' + \
                self.sub_system_order + '<' + init_file
        os.system(order)

    def reduce_db(self, backup_file='backup.sql'):
        backup_file = get_work_path() + '/sql/' + backup_file
        order = 'mysql --ssl-mode=disabled' + \
                self.sub_system_order + '<' + backup_file
        os.system(order)
