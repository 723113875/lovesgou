import pymysql

class db_conn():
    def __init__(self):
        import configparser
        import os
        proDir = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(proDir, "database.ini")

        conf = configparser.ConfigParser()
        conf.read(configPath, encoding='utf-8')

        host = conf.get('sql', 'host')
        user = conf.get('sql', 'user')
        password = conf.get('sql', 'password')
        database = conf.get('sql', 'database')

        self.mydb = pymysql.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def check_sql(self, value):
        sql = "SELECT 页面的定位元素 FROM pagepath WHERE 页面定位的解释=%s"
        self.mycursor.execute(sql, value)
        return self.mycursor.fetchone()[0]

    def check_table_all(self, value):
        sql = "SELECT 登录成功的账号, 登录成功的密码 FROM {}".format(value)
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()