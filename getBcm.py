import requests, webbrowser
webbrowser.open(requests.get('https://api.codemao.cn/creation-tools/v1/works/' + input('你要获取bcm文件的ID')).json()['bcm_url'])
