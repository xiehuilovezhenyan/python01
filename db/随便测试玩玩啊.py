from DataBaseHandle import DataBaseHandle
import xlrd

# 测试连接数据库
def _test1():
    DbHandle = DataBaseHandle('192.168.1.239', 'root', 'Mysql_1234', 'knowledge', 3306)

    courseList = DbHandle.selectDb('select * from t_course')
    print(courseList)
    for i in courseList:
        #print(i[-1])
        modyTime = i[-1]
        if modyTime is not None and modyTime != '':
            print(modyTime)


    courseCount = DbHandle.selectCount('select count(*) from t_course');
    print(courseCount[0])



    DbHandle.closeDb()

# 测试解析Excel
def inputExcel(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)

    for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            print(rowVale[colNum])
        print("---------------")


if __name__ == '__main__':
    _test1()
    #inputExcel("C:\\Users\\82796\\Desktop\\投放渠道模板.xlsx")
