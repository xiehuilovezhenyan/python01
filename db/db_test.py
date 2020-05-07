# encoding=utf-8
import pymysql
import redis
import time


def getListTest(sql):
    # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
    db = pymysql.connect(host='192.168.1.239',
                         user='root',
                         password='Mysql_1234',
                         database='knowledge',
                         port=3306,
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    date = cursor.fetchall()
    for i in date:
        print(i)
        # print(i['name'])
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
    return date

def redisTest(key):
    r = redis.Redis(host='192.168.1.178', port=6379, db=0, password='qkk2018', charset='utf8', decode_responses=True)
    # r.set('name', 'zhangsan')   #添加
    data = r.hgetall(key)
    # print(str(data,'utf-8'))  # 获取
    # print(str(data,'utf-8'))
    print(data)


if __name__ == '__main__':
    getListTest("select * from t_course")
    redisTest('kakaka:Object:systemConfigure:bank21OrderPayLimitConfig')