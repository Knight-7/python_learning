import pymysql


class MysqlConeect():
    """自定义一个连接MySql的类"""

    def __init__(self, database, host='47.102.223.103', port=3306,
                 charset='utf8', user='root', password='aliyun',
                 is_close_auto=True):
        self._host = host
        self._port = port
        self._database = database
        self._charset = charset
        self._user = user
        self._password = password
        self._connect = None
        self._cursor = None
        self._is_close_auto = is_close_auto
        self.connect_to_mysql()

    def connect_to_mysql(self):
        self._connect = pymysql.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password,
            charset=self._charset
        )
        if self._connect:
            self._cursor = self.connect.cursor()

    @property
    def connect(self):
        return self._connect

    @property
    def connect_and_cursor(self):
        return self._connect, self._cursor

    def creat_table(self, table):
        pass

    def insert(self, table, *args):
        pass

    def __del__(self):
        if self._is_close_auto:
            if self._cursor:
                self._cursor.close()
            if self._connect:
                self._connect.close()


def main():
    mysql = MysqlConeect('course_design')
    con, cur = mysql.connect_and_cursor
    sql = 'show tables;'
    cur.execute(sql)
    res = cur.fetchall()
    print(res)


if __name__ == '__main__':
    main()