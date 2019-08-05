# -*- coding:utf-8 -*-
import socket


class Client:
    def __init__(self, por, ip='127.0.0.1'):
        self.por = por
        self.ip = ip

    def method(self):
        client = socket.socket()
        client.connect((self.ip, self.por))
        while True:
            data = input('客户端:')
            client.send(data.encode('utf-8'))
            if data == '拜拜':
                return
            else:
                message = client.recv(1024)
                print('来自服务器端的消息:', message.decode('utf-8'))
                if str(message) == '拜拜':
                    return


num = 8093
while True:
    client = Client(num).method()
    num += 1
