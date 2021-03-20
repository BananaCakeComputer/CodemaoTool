'''作者：蕉饼
能获取作品ID的bcmc文件
自己改后缀名，虽然获取的没有代码'''
import requests, webbrowser
webbrowser.open(requests.get('https://api-creation.codemao.cn/kitten/work/player/load/' + input('你要获取bcm文件的ID')).json()['source_urls'][0])
