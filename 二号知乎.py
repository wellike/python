import time
from http import cookiejar
import requests
from base64 import beautifulsoup
headers= dict{
    "host":"www.zhihu.com",
    "referer":"https://www,zhihu.com",
    'User-Agent': 'User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)
}
session=requests.session()
session.cookies=cookiejar.lwpcookiejar(filename="cookie.txt")
try:
    print (session.cookies)
    session.cookies.load(ignore_discard=true)
except:
    print "还没有cookie信息"

def get_xsrf():
        response=session.get("https://www.zhihu.com",headers=headers)
        soup=beautifulsoup(response.content,"html.parser")
        xsrf=soup.find("input",attrs={"name": "_xsrf"}.get("value"))
        return xsrf
def get_captcha():
    t=str(int(time.time()*1000))
    captcha_url='https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r=session.get(captcha_url,headers=headers)
    with open("captcha.jpg","wb") as f:
        f.write(r.content)
        captcha=input("验证码：")
        return captcha
def login(email,password):
    login_url = 'https://www.zhihu.com/login/email'
    data={
        "email":email,
        "password":password,
        "_xsrf":get_xsrf(),
        "captcha":get_captcha(),
        "remember_me":"true"
    }
    response=session.post(login_url,data=data,headers=headers)
    login_code=response.json()
    print(login_code["msg"])
    for i in session.cookies:
        print i
        session.cookies.save()






