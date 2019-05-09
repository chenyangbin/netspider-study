# cooke用于服务器识别用户,维持登陆信息, 记录用户身份的文件
"""
在使用爬虫的时候，经常会用到cookie进行模拟登陆和访问。在使用urllib库做爬虫，
需要借助http.cookiejar库中的CookieJar来实现。

CookieJar类有一些子类，分别是FileCookieJar，MozillaCookieJar，LWPCookieJar。

CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
           整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

FileCookieJar (filename,delayload=None,policy=None)：
            从CookieJar派生而来，用来创建FileCookieJar实例，
            检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。
            delayload为True时支持延迟访问访问文件，
            即只有在需要时才读取文件或在文件中存储数据。

MozillaCookieJar (filename,delayload=None,policy=None)：
            从FileCookieJar派生而来，
            创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

LWPCookieJar (filename,delayload=None,policy=None)：
            从FileCookieJar派生而来，创
            建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例
"""
#%% http.cookiejar 管理cookie
# 管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象
# 整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失

# 使用CookieJar获取cookie值
import urllib.request, http.cookiejar
cookie = http.cookiejar.CookieJar()  # 获取cookie
handler = urllib.request.HTTPCookieProcessor(cookie)   # 处理cookie
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

print(type(cookie))  # cookie是个 <class 'http.cookiejar.CookieJar'>   cookiejar的对象
print(type(item))

# 保存cookie文件 使用save方法
import urllib.request, http.cookiejar
filename = 'cookie-LWP.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)  # 获取cookie 使用浏览器方法保存cookie格式
# 或者lwp保存cookie格式
#cookie = http.cookiejar.LWPCookieJar(filename)  # 获取cookie 使用浏览器方法保存cookie格式
handler = urllib.request.HTTPCookieProcessor(cookie)   # 处理cookie
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
# ignore_expires 忽略过期时间
for item in cookie:
    print(item.name+"="+item.value)

print(type(cookie))  # cookie是个 <class 'http.cookiejar.CookieJar'>   cookiejar的对象
print(type(item))

# 读取加载kooie load方法
import urllib.request, http.cookiejar
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie) #处理cookie
opener = urllib.request.build_opener(handler)  # 构造自定义的opener 发送请求
response = opener.open('http://www.baidu.com') # 发送请求
print(response.read().decode('utf-8'))


#%%
data = {

    'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'cache-control':' max-age=0',
    'cookie: BAIDU_SSP_lcr=https':'//www.baidu.com/link?url=_BLF1rnwf9Nvco7EY1MwU2dntMk7-MoM1d8H5Q7UK8g0eSEynPs20OL6Sz3DbW2K7hbJU168f4H7IlXDnm6HRLUfmdxejMAfpri59vZ-6IW&wd=&eqid=bb3d75760007c1ed000000035cc57847; uuid_tt_dd=10_18649041300-1556316071833-929853; dc_session_id=10_1556316071833.282116; bdshare_firstime=1556318517334; UserName=weixin_39454561; UserInfo=7298c2fd7546401481bbc19ee240f87f; UserToken=7298c2fd7546401481bbc19ee240f87f; UserNick=binyangyan; AU=136; UN=weixin_39454561; BT=1556318916112; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_18649041300-1556316071833-929853!5744*1*weixin_39454561; firstDie=1; __yadk_uid=fpyutXFwvI78a9nQavCeRWBqMUsgOyvr; dc_tos=pqo0un; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1556440469,1556445075,1556445156,1556445264; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1556445264',
    'dnt':' 1',
    'referer: https':'//www.baidu.com/link?url=_BLF1rnwf9Nvco7EY1MwU2dntMk7-MoM1d8H5Q7UK8g0eSEynPs20OL6Sz3DbW2K7hbJU168f4H7IlXDnm6HRLUfmdxejMAfpri59vZ-6IW&wd=&eqid=bb3d75760007c1ed000000035cc57847',
    'upgrade-insecure-requests':' 1',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }