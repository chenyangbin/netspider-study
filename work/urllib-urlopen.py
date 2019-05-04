import urllib


#%%
import urllib.request
resonsea = urllib.request.urlopen('http://www.baidu.com',timeout=500)
print(resonsea.read().decode('utf-8'))
print(type(resonsea))

# 参数：
#  url 地址
#  timeout 超时设置
# data 提交数据设置

#%%
# data 参数,post提交数据
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf8')
resonses = urllib.request.urlopen('http://httpbin.org/post', data= data)
print(resonses.read())

#%%
# timeout 参数
import urllib.request

resonsea = urllib.request.urlopen('http://www.baidu.com', timeout=0.5)
print(resonsea.read())


#%%
# timeout 异常捕获
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.com', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("time out")


#%% 响应的类型
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(type(response))  # 响应类型
print(response.status)  #响应状态
print(response.getheaders())  # 响应头全部内容
print(response.getheader('Server')) # 服务器类型
print(response.getheader('content-type'))  # 头中内容编码

#%%  read方法:获取响应体内容,是个字节流,需要解码才能看到
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))  # 获取读取响应体内容
# response 对象是个class 'http.client.HTTPResponse' urlopen的对象, 获取链接的响应体
print("---------")
print(type(response))


