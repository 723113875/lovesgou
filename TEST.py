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
        sql = "SELECT 登录成功的账号, 登录成功的密码 FROM {}".format(value)
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

if __name__ == '__main__':
    aa = db_conn().check_sql('codetest')
    print(aa)