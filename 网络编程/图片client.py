# -*- coding:utf-8 -*-
import socket
import requests

client = socket.socket()
client.connect(('127.0.0.1', 9093))
data = bytes()
while True:
    re_data = client.recv(1024)
    data += re_data
    print('接收到数据')
    if not re_data:
        break
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1543395098&di=2a5bbaa5600097b050ba69a688672de9&src=http://p0.qhimgs4.com/t0112e7ebfdef7f923d.jpg'
    response = requests.get(url)
    image_data = response.content
    print('数据接收完')
    with open('new.png', 'bw') as f:
        f.write(data)
    while True:
        message = input('客户端')
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        print('服务器:', data.decode('utf-8'))
