# urllib.error 异常处理
"""
    URLError:来自urllib库的error模块，继承自OSError,由request模块
    产生的异常都可以通过捕捉这个类来处理．
    父类: URLError 包含属性 reason


    HTTPError是URLError的子类，发出一个请求时，
    服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"。
    专门用来处理ＨTTP请求错误，比如未认证，页面不存在等

    有三个属性：
    code:返回HTTP的状态码
    reason:返回错误原因
    headers:返回请求头
"""



#%%
from urllib import request, error
try:
    response = request.urlopen('http://www.dnandna.com')
except error.URLError as e:
    print(e.reason)

#%% 获取HTTP子类中的reason, code, headers
from urllib import request, error
try:
    response = request.urlopen('http://www.40404.com')
except error.HTTPError as he:
    print(he.reason, he.code, he.headers, sep='\n')  # 查看httperror返回到异常信息

except error.URLError as  ue:
    print(ue.reason)   # 查看urlerror中的reason

else:
    print("请求成功")  # 没有抛出异常.则请求成功

