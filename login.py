from bs4 import BeautifulSoup
import json
from json import dumps
import requests
headers={"Content-Type":"application/json",'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17'}
def pid():
    res=requests.get('https://shequ.codemao.cn',headers=headers)
    soup=BeautifulSoup(res.text,'ht'+'ml.parser')
    data=json.loads(soup.find_all("script")[0].string.split("=")[1])
    return data['pid']
identity = input('账号')
password = input('密码')
print(requests.post('https://api.codemao.cn/tiger/v3/web/accounts/login',headers = headers,data = dumps({'identity':identity,'password':password,'pid':pid()})).text)
