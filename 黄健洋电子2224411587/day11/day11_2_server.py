import requests
import random
import json
from hashlib import md5
import time
import threading
from socket import *
sk = socket.socket()
sk.bind( ("127.0.0.1",8999) )
sk.listen(10)
conn, addr = sk.accept()
print("hello")
print(f'conn is:{conn}')
print(f'addr is:{addr}')
 

appid = '20231003001835485'
appkey = 'TwLgpjvkHKx0oPpKeGL2'
from_lang = 'zh'
to_lang =  'en'
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def baidu_api(query,from_lang,to_lang):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result["trans_result"][0]['dst']

def trans(query: str) -> None:
    return baidu_api(query, from_lang, to_lang)

while True:
	accept_data = conn.recv(1024)
	accept_data = accept_data.decode('utf8')
	send_data = trans(accept_data)
	conn.sendall(bytes(send_data, encoding="utf8"))
conn.close()