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