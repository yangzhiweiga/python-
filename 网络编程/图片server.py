# -*- coding:utf-8 -*-
import socket

server = socket.socket()
server.bind(('127.0.0.1', 9093))
server.listen(512)
while True:
    conversation, addr = server.accept()
    print(addr)
    with open('飞机大战/images/enemy0.png', 'br') as f:
        content = f.read()
        conversation.send(content)
    while True:
        data = conversation.recv(1024)
        print('客户端：', data.decode('utf-8'))
        message = input('服务器')
        conversation.send(message.encode('utf-8'))

    conversation.close()
