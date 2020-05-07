from DataBaseHandle import DataBaseHandle

def test1():
    DbHandle = DataBaseHandle('192.168.1.239', 'root', 'Mysql_1234', 'knowledge', 3306)

    courseList = DbHandle.selectDb('select * from t_course')
    print(courseList)



    DbHandle.closeDb()




if __name__ == '__main__':
    test1()
