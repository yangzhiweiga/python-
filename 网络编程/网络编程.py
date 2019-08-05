# -*- coding:utf-8 -*-
import socket

# socket 又叫套接字，指的是实现通信的两个端，等待请求的一段叫服务端套接字，发送请求的一端叫客户端套接字 python中提供了socket模块来支持socket编程
# family 设置IP类型默认ip4
# type 设置传输类型默认tcp
server = socket.socket()
# 绑定ip地址和端口
server.bind('127.0.0.1', 8080)
# 开始监听 listen(最大监听数) 相当于服务器一次可以处理多少个请求
server.listen(100)
# 让服务一直处于启动状态
while True:
    # 接收到客户端发送的请求，返回建立的会话和客户端地址
    conversation, addr = server.accept()
    # 接收消息（客户端发送个服务器的消息)
    re_data = conversation.recv(1024)
    print(re_data.decode('utf-8'))
    # 发送数据（服务器给客户端发送数据)
    message = '你好！！！'
    conversation.send(message.encode(encoding='utf-8'))
    conversation.close()