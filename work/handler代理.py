
# 使用handler 构造代理 伪装爬虫地址, 防止本机爬虫被封
# 在urllib库中，提供了一些Handler，如：HTTPHandler，HTTPSHandler，ProxyHandler，BaseHandler，AbstractHTTPHandler，FileHandler，FTPHandler，
# 分别用于处理HTTP，HTTPS，Proxy代理等。
# 使用urllib库请求是都是使用urlopen()方法实现的。实际上它的底层是使用HTTPHandler个Opener来实现的
# 同样可以自己实现自定义的opener对象

# 简单的自定义opener()
"""
 import urllib.request
 第一步：构建一个HTTPHandler 处理器对象，支持处理HTTP请求
 http_handler = urllib.request.HTTPHandler()
 第二步：调用urllib.build_opener()方法，创建支持处理HTTP请求的opener对象
 pener = urllib.request.build_opener(http_handler)
 第三步：构建 Request请求
 request = urllib.request.Request("http://www.baidu.com/")
 第四步：调用自定义opener对象的open()方法，发送request请求
 response = opener.open(request)
 第五步：获取服务器响应内容
 print(response.read())
"""



#%%
import urllib.request
proxy_handler = urllib.request.ProxyHandler({  # 构造proxy代理 传入代理地址
     'http':'http://127.0.0.1:9734'
    })
# 使用urllib库请求是都是使用urlopen()方法实现的。实际上它的底层是使用HTTPHandler个Opener来实现的
# 同样可以自己实现自定义的opener对象

opener = urllib.request.build_opener(proxy_handler)   # 构建代理
response = opener.open('http://www.baodu.com', timeout=1)
print(response.read())



