from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams = '?' + urlencode({quote_plus('serviceKey') : 	
'qOcIoYwcIfqHRrXCZmWVGVS4c3P6Ww4yf4ozsUspap0vG6g1HJhLDOp8ORHW0oSmWVJaKcW3wVm4CjHSyf6otA=='
                               ,quote_plus('returnType'):'xml'
                               ,quote_plus('numOfRows') :'5'
                               ,quote_plus('pageNo'):'1'
                               ,quote_plus('stationName'):'주안'
                               ,quote_plus('dataTerm'):'DAILY'
                               ,quote_plus('ver'):'1.0'})

res = requests.get(url+queryParams)
soup = BeautifulSoup(res.content,'html.parser')
data = soup.find_all('item')
#print(data)

for item in data:
    print(item.find('datatime').text)
    print(item.find('pm25value').text)
   