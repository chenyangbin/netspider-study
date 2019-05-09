# requests.get
"""
    requests.get()
    r=requests.get(url,params,**kwargs)

    url: 需要爬取的网站地址。
    params: 翻译过来就是参数， url中的额外参数，字典或者字节流格式，可选。
    **kwargs : 12个控制访问的参数


    **kwargs有以下的参数，对于requests.get,其第一个参数被提出来了。

        params：字典或字节序列， 作为参数增加到url中,使用这个参数可以把一些键值对以?key1=value1&key2=value2的模式增加到url中


        例如：kv = {'key1':' values', 'key2': 'values'}
        r = requests.get('http:www.python123.io/ws', params=kw)

        data：字典，字节序或文件对象，重点作为向服务器提供或提交资源是提交，，作为request的内容，与params不同的是，data提交的数据并不放在url链接里， 而是放在url链接对应位置的地方作为数据来存储。，它也可以接受一个字符串对象。
        json：json格式的数据， json合适在相关的html，http相关的web开发中非常常见， 也是http最经常使用的数据格式， 他是作为内容部分可以向服务器提交。


        例如：kv = {'key1': 'value1'}
        r = requests.post('http://python123.io/ws', json=kv)

        headers：字典是http的相关语，对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何我们想模拟的浏览器来对url发起访问。


        例子： hd = {'user-agent': 'Chrome/10'}
        r = requests.post('http://python123.io/ws', headers=hd)

        cookies：字典或CookieJar，指的是从http中解析cookie
        auth：元组，用来支持http认证功能
        files：字典， 是用来向服务器传输文件时使用的字段。


        例子：fs = {'files': open('data.txt', 'rb')}
        r = requests.post('http:/#/python123.io/ws', files=fs)

        timeout: 用于设定超时时间， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一个timeout的异常。
        proxies：字典， 用来设置访问代理服务器。
        allow_redirects: 开关， 表示是否允许对url进行重定向， 默认为True。
        stream: 开关， 指是否对获取内容进行立即下载， 默认为True。
        verify：开关， 用于认证SSL证书， 默认为True。
        cert： 用于设置保存本地SSL证书路径
"""
#%%
import requests

re_get = requests.get('http://www.baidu.com')  # 方法
print(type(re_get))   # 查看re的响应类型
print("状态码", re_get.status_code)  # 查看状态码
print("响应头", re_get.headers)  # 响应头
print("cookie信息", re_get.cookies)  # 查看cookie
print(re_get.content) # 获取二进制字节流
print(re_get.text)



#%% 其他方法
re_put = requests.put('http://www.baidu.com')  # put方法
re_delete = requests.delete('http://www.baidu.com')  # delete方法
re_head = requests.head('http://www.baidu.com')  # head方法
re_options = requests.options('http://www.baidu.com')  # options方法


#%% 获取二进制字节流并保存
import requests
re_binary = requests.get('http://www.baidu.com')   # 保存图片或者视频,使用content 获取字节流内容,再用文件读取保存方法,写入文件
with open('html.txt', 'wb') as f:   # 从内存中读取
    f.write(re_binary.content)      # 写入文件
    f.close()          # 写完以后关闭文件


#%% 返回对象 response 的常用属性
import requests
response = requests.get('http://www.sinna.com')
print(type(response.cookies), response.cookies)  # cookie属性<class 'requests.cookies.RequestsCookieJar'>
print(type(response.headers), response.headers)  # 响应头属性<class 'requests.structures.CaseInsensitiveDict'>
print(type(response.status_code), response.status_code)  # 状态码属性<class 'int'>
print(type(response.history), response.history)  # <class 'list'>

#%% 添加头handers 通过handers参数传递头信息
import requests
headers =
response = requests.get('http://www.zhihu.com')

print(response.text)

#%% requests 高级操作 文件上传post方法
import  requests
files = {'files':open('html.txt', 'rb')}
re_getfile = requests.post('http://www.baidu.com', files=files)
print(re_getfile.text)

#%% 获取cookie
import requests
re_getcookie = requests.get('https://www.zhihu.com')
print(re_getcookie.cookies)
for key, value in re_getcookie.cookies.items():
    print(key+ '=' + value)
print("查看cookie的类型", type(re_getcookie.cookies))  # 结果<class 'requests.cookies.RequestsCookieJar'>
#%% 使用cookies 维持会话登陆状态 模拟登陆
import requests
requests.get('https://www.zhihu.com')
headers = {
    'cookie': '_xsrf=YK7uoGlgTv8cb0JtfMgBJp2oPZY5RtSS; _zap=fe71ca1a-7289-4bdd-84a9-0d076231c54d; d_c0="ABCpCN6EVw-PTlP73QcM0aiovVNqdmFe_Js=|1556351339"; q_c1=7ada6803fd1346f493fb14b6fd3dfc78|1556870335000|1556870335000; capsion_ticket="2|1:0|10:1557038880|14:capsion_ticket|44:Zjc3Y2ViNzMyNzIzNDA4NmJhZjg0Mjc3M2IzMTU5NGE=|df4811ac1986393e56bc2e0fbf82be62bbbccb484077e043617ddae549159b75"; z_c0="2|1:0|10:1557038909|4:z_c0|92:Mi4xeEYtQkF3QUFBQUFBRUtrSTNvUlhEeVlBQUFCZ0FsVk5QZFc3WFFEUzRhMnhWUGcwNHg5UDljRmsyRGFCaV9XbTJ3|4ecf6ed88f680f8dc549ce47b874b13d7cf198338cdef74c3c93b554316a3aba"; tst=r; tgw_l7_route=6936aeaa581e37ec1db11b7e1aef240e',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'www.zhihu.com'
}
re_keep_log = requests.get('https://www.zhihu.com', headers=headers)
print(re_keep_log.text)

#%% 会话维持 session维持会话 对于使用获取cookie后保存cookie 维持后续登陆session 发起请求



#%% ssl 证书验证
# 发送https请求的时候会检查证书 verify 参数设置ssl true:验证开启, False验证关闭
import requests
re = requests.get('https://www.12306.cn', verify = False)
print(re.status_code)
print(re.text)


#%% 代理设置  直接使用proxies 参数的字典格式设置代理
import requests

proxies = {"http":"http://127.0.0.1:1080" }
re = requests.get('https://www.taobao.com', proxies = proxies)
print(re.status_code)

#%% 超时设置 网路状况不好的时候,设置服务器应答等待时间 timeout参数
# 超时时间分为连接connect超时以及读取read超时 分别设置时候使用二元数组设置
import requests
re = requests.get('https://www.12306.cn', verify = False, timeout=1)
re = requests.get('https://www.12306.cn', verify = False, timeout=(1, 2, 30))
print(re.status_code)
print(re.text)


#%% 身份认证 auth:传入用户名, 密码
import requests
re = requests.get('https:// www.knsdnsnd.com', auth = ('user', 'code'))
print(re.status_code)


#%% 异常处理, 超时, 访问错误, httperror, proxyerror, sslerror, timeouterror, connectionerror

import requests
from requests.exceptions import ReadTimeout, Timeout, ConnectionError, RequestException

try:
    response = requests.get('https://www.python.org', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection error on")



