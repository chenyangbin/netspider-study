from selenium import  webdriver
bro = webdriver.Chrome()
bro.get('http://www.baidu.com')
bro.get('http://www.zhihu.com')
print(bro.page_sourc)