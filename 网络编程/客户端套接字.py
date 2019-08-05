# -*- coding:utf-8 -*-
import socket

# 创建套接字对象
client = socket.socket()
# 连接服务器
client.connect('127.0.0.1', 8088)
# 发送消息
message = input('>>')
client.send(message.encode('utf-8'))
# 接收消息
re_data = client.recv(1024)
print(re_data.decoe('utf-8'))

