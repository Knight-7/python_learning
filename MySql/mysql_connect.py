import pymysql


class MysqlConeect():
    """自定义一个连接MySql的类"""

    def __init__(self, database, host='localhost', port=3306,
                 charset='utf8', user='root', password='123456'):
        self.host = host
        self.port = port
        self.database = database
        self.charset = charset
        self.user = user
        self.password = password
        self.connect = None
        self.cursor = None
        self.connect_to_mysql()

    def connect_to_mysql(self):
        self.connect = pymysql.connect(
            host = self.host,
            port = self.port,
            database = self.database,
            user = self.user,
            password = self.password,
            charset = self.charset
        )
        if self.connect:
            self.cursor = self.connect.cursor()

    def __del__(self):
        if self.connect:
            self.connect.close()
        if self.cursor:
            self.cursor.close()


def main():
    con1 = MysqlConeect('python_use')


if __name__ == '__main__':
    main()