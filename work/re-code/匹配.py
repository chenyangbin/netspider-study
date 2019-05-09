# 泛化匹配  mach 使用的是开头开始匹配, 一旦开头不能匹配成功, 匹配就会结束
import re
content = "hello 123 4578 World_This is a regex demo"
result = re.match('^hello.*demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)


#%% group 匹配目标 匹配一段字符的左端点和右端点, 并用括号() 括起来 表示组
# 在result.group中. 第一个括号结果为group(1)  此类型使用于多字段匹配
import re
content = "hello 1234578 World_This is a regex demo"
result = re.match('^hello\s(\d+)\s.*demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)
print(result.group(1))

#%% 贪婪匹配 贪婪模式下的 .* 会匹配尽可能多的字符
import re
content = "hello 1234578 World_This is a regex demo"
result = re.match('^he.*(\d+)\s.*demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)
print(result.group(1))   # 看到结果是数字中的 结果只留下最后的8作为结果,, 其余被前面的 .* 贪婪

#%% 非贪婪模式  .*?
import re
content = "hello 1234578 World_This is a regex demo"
result = re.match('^he.*?(\d+)\s.*demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)
print(result.group(1))   # .*? 可以匹配尽可能少的字符 当(\d+) 别人可以匹配的时候就自己放弃匹配,让别人的条件匹配


#%% 匹配模式 对匹配过程的模式进行设置使匹配处于非默认状态下
# 常见的模式 参数
# re.I 使匹配对大小写不敏感
# re.L 使匹配做本地化识别
# re.M 多行匹配影响 ^ 和 $
# re.S 使 . 可以匹配 换行符号在内的所有字符
# re.U 根据Unicode字符解析字符, 该标志会影响 \w \W \b \B
# re.X 可使用更加灵活的格式, 将正则表达式写的方便理解


#%% re.S 针对 . 不能匹配换行符的情况
import re  # 没有对 . 的匹配模式进行设置的情况下,换行符号无法匹配
content = """hello 1234578 World_T
his is a regex demo"""
result = re.match('^hello.*?(\d+).*?demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)
print(result.group(1))

#%%
import re  # 设置 re.S 可以匹配匹配
content = """hello 1234578 World_T
his is a regex demo"""
result = re.match('^hello.*?(\d+).*?demo$', content, re.S)  # 匹配开头和结尾 中间用 ,*匹配任意多个
print(result)
print(result.group(1))

#%% 转义匹配 匹配目中含有 匹配字符 使用 \ 转义即可
import re
content = "price is $5.00"
result = re.match('price is \$5\.00', content)
print(result)

#%% 匹配总结
# 尽量使用泛化匹配模式,
# 使用括号得到匹配目标,
# 尽量使用非贪婪 .*? 模式
# 有换行就使用 re.S

#%% re.search 扫描整个字符串, 并返回第一个成功的匹配
# 即search 可以匹配字符串的一部分, 没有匹配时候返回none
import re

html = """
html = <div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>"""
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(result.group(1), result.group(2))


#%% re.search升级版 re.findall  找到所有符合匹配条件的以列表类型返回结果
import re
html = """
html = <div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>"""
result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
for i in result:
    print(i)

#%% sub 修改文本 sub('被修改的字符', '修改后的字符', 修改源)
import re
html = """
html = <div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>"""
result = re.sub('<a.*?>|</a>', '', html)  # 先去掉a表情
song_lic = re.findall('<li.*?>(.*?)</li>', result, re.S)
print(song_lic)
for i in song_lic:
    print(i.strip())

#%% compile编译方法 将正则表达式编译为正则对象, 以供快捷调用
# compile('正则表达式', 匹配模式)
import re
content = "hello 1234578 World_This is a regex demo"
# result = re.match('^hello\s(\d+)\s.*demo$', content)  # 匹配开头和结尾 中间用 ,*匹配任意多个
pattern = re.compile('^hello\s(\d+)\s.*demo$', re.S)   # compile 是正则更加方便
result = re.match(pattern, content)
print(result)
print(result.group(1))












