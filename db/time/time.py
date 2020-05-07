import time
import datetime

print(int(time.time()))  # 时间戳
print(time.localtime(time.time()))  # 时间元组
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))   # 输入自定义格式

#计算时间消耗，特别是对程序运行时间消耗
start = time.time()
for _ in range(100):
    pass
end = time.time()
print("循环运行时间:%.2f秒"%(end-start))

print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.today())

start = datetime.datetime.now()
while True:
    for i in range(100000000):
        pass
    break
end = datetime.datetime.now()
print("程序运行时间："+str((end-start).seconds)+"秒")