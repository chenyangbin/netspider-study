#%%
import requests
import re
header_code = {
    'Referer': 'https://book.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 '
}
douban_text = requests.get('https://book.douban.com/', headers=header_code).text
#print(douban_text)
patten = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
get_content = re.findall(patten, douban_text)
print(get_content)

