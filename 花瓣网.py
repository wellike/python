import requests
from parsel import Selector
import js2xml
url = 'http://huaban.com/favorite/beauty/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
headers1 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept':'application/json',
    'X-Request':'JSON',
    'X-Requested-With':'XMLHttpRequest'
}
params = {
    'j0ga0hbi':'',
    'max':'1062161596',
    'limit':'1',
    'wfl':'1'
}
z1 = requests.get(url=url,params=params,headers=headers1)
for i in z1.json()['pins']:
    print i['pin_id']
detailurl = 'http://huaban.com/pins/1062650100/'
z3 =requests.get(url=detailurl,headers=headers)
# print z3.text
sel1 = Selector(text=z3.text)
sel1.xpath('//script/text()')
print sel1.xpath('//script/text()')
