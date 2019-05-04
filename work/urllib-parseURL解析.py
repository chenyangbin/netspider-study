# urlparse URL的拆分 处理网址,访问链接
"""
    urlparse模块主要是把url拆分为6部分，并返回元组。并且可以把拆分后的部分再组成一个url。
    主要有函数有urljoin、urlsplit、urlunsplit、urlparse等。

    参数:urlparse.urlparse(url[, scheme[, allow_fragments]])

    将URL解析成6个部分，从urlstring中取得URL，并返回元组
    元组:(scheme, netloc, path, parameters, query, fragment)，
    但是实际上是基于namedtuple，是tuple的子类。它支持通过名字属性或者索引访问的部分URL，
    每个组件是一串字符，也有可能是空的。组件不能被解析为更小的部分，%后面的也不会被解析，
    分割符号并不是解析结果的一部分，除非用斜线转义，注意，返回的这个元组非常有用，
    例如可以用来确定网络协议(HTTP、FTP等等 )、服务器地址、文件路径，其他参数...
    具体元组元素:
    scheme: 网络协议类型 http, https, ftp...
    netloc:服务器位置
    path:// 资源路径
    prams: 其他参数
    query: 链接符号 链接键值对
    fragment: 拆分文档中的特殊键

"""

#%% urlparse 拆分网址
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/s?wd=%E5%9B%BE%E7%89%87&rsv_spt=1&rsv_iqid=0xf97809da00007e28&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&inputT=5837&rsv_t=8a03Uyg3nmaxbAuFyDgAOxi1dmg1j%2Bx%2BVC0lGJP5K10trQYaDHQqX%2BUsX9W4F4ZH16Y7&rsv_sug3=14&rsv_sug1=15&rsv_sug7=100&oq=%25E5%2593%2588%25E5%2593%2588&rsv_pq=f0e9790700009fd5&rsv_sug2=0&rsv_sug4=6458')
print(type(result))
print(result, sep='\n')

#%% urlparse 指定协议类型 schema
from urllib.parse import urlparse
result = urlparse('www.baidu.com/s?wd=哈', scheme='https')
print(type(result))
print(result, sep='\n')

#%% 链接符号
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/s?wd=哈#dn',allow_fragments=False)
print(type(result))
print(result, sep='\n')



#%% urlunpars  拼接url
from urllib.parse import urlunparse
url = ['http', 'www.baidu.com', 'index.html','user', 'wd=hah', 'comment']
print(urlunparse(url))


#%% urljoin 拼接url 对多个url过滤拼接, 以参数的中的url列中的后url为准
from urllib.parse import urljoin
print(urljoin('http://www.baidu,com','index.html'))
print(urljoin('http://www.baidu..com', 'http://www.baidu.com/index.html'))


#%% urlencode 把字典对象转换为get请求参数, 对请求字典形式的参数编码成服务器可识别的字符串形式
from urllib.parse import urlencode
parameters = {'name': 'net',
              'age':22,
              'cname':'鹏'}
base_url = 'http://www.baidu.com'
url = base_url + urlencode(parameters)  # 对参数编码http://www.baidu.comname=net&age=22&cname=%E9%B9%8F
uncodeurl = 'http://www.baidu.comname=net&age=22&cname=%E9%B9%8F'
print(url)

#%% 对网址的单独的解码编码




