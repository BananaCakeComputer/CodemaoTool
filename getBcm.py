'''作者：蕉饼
这个程序已经不管用了，因为官方修复了这个问题，bcm_url对应空'''
import requests, webbrowser
webbrowser.open(requests.get('https://api.codemao.cn/creation-tools/v1/works/' + input('你要获取bcm文件的ID')).json()['bcm_url'])
