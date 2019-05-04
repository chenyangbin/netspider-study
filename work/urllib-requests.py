# requests 发送复杂请求,构建requests请求对象,再用requests.urlopen 发送请求,接受响应信息
#%% 将url构建request对象,同样可以发起请问,但是requests可以添加众多请求参数

import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

#%%
# 构造多参数请求
from urllib import request, parse

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
           # 字典形式来构建
           }
dict = {'wd':'Germey'}       # 大量的字典形式的参数可以使用正则快捷键进行正则替换
data = bytes(parse.urlencode(dict), encoding='utf8')  # 提交的数据要使用编码流来对数据编码
req = request.Request(url= url, data=data, headers=headers, method='POST')  # 构造euquests请求对象
# 构造一个requests的复杂参数请求对象
response = request.urlopen(req)  # 使用urlopen发送请求对象
print(response.read().decode('utf-8'))
print("请求头的类型",type(headers))
print("返回请求头所有信息",response.getheaders())



#%% 添加请求头的方法二 请求对象.add_header
from urllib import  request, parse
url = 'http://www.baidu.com'
dict = {'wd':'hello'}  # 构造请求数据内容
data = bytes(parse.urlencode(dict), encoding='utf8') # 对请求数据编码
req = request.Request(url=url, data=data, method='POST') # 构造请求对象
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64)') # 使用add添加请求头
response = request.urlopen(req)  # 使用urlopen发送请求对象
print(response.read().decode('utf-8'))
