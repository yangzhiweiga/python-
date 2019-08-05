# -*- coding:utf-8 -*-
import socket


class Server:
    def __init__(self, por, ip='127.0.0.1'):
        self.por = por
        self.ip = ip

    def method(self):
        server = socket.socket()
        server.bind((self.ip, self.por))
        server.listen(1024)
        while True:
            convsation, addr = server.accept()
            while True:
                data = convsation.recv(1024)
                new_data = str(data, 'utf-8')
                print('来自客户端的消息:', new_data)
                if new_data == '拜拜':
                    return
                else:
                    message = input('服务器端:')
                    convsation.send(message.encode('utf-8'))
                    if message == '拜拜':
                        return


num = 8093
while True:
    srever = Server(num).method()
    num += 1
