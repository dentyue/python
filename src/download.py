# -*-codeing:utf-8 -*-
import re
import requests

url='http://wwww.sohu.com'
res=requests.get(url)
if res.status_code==200:
    #打印网页内容
    print(res.text)  
