import requests


# 以下为GET请求
url = 'https://www.csdn.net/'
requests = requests.get(url)
print(requests.content)
