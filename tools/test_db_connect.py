import pymysql

class db_conn():
    def __init__(self):
        self.mydb = pymysql.connect(
            host='127.0.0.1',
            user='sbroot',
            passwd='1234',
            database='lovesgou_database'
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