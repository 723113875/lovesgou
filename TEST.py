import pymysql
import configparser

conf = configparser.ConfigParser()
conf.read('database.ini', encoding='utf-8')

host = conf.get('sql', 'host')
user = conf.get('sql', 'user')
password = conf.get('sql', 'password')
database = conf.get('sql', 'database')

class db_conn():
    def __init__(self):
        self.mydb = pymysql.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def check_sql(self, value):
        sql = "SELECT 登录成功的账号, 登录成功的密码 FROM {}".format(value)
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

if __name__ == '__main__':
    aa = db_conn().check_sql('codetest')
    print(aa)