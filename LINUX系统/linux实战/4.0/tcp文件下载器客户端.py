"""
#1导入模块
#2创建套接字
#3建立连接
#4接受用户输入的文件名
#5发送文件名到服务端
#6创建文件，并且准备保存
#7接受服务器的数据，保存到本地（循环）
#8关闭套接字
"""
#1导入模块
import socket
#2创建套接字
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3建立连接
tcp_client_socket.connect(("192.168.43.153",8888))
#4接受用户输入的文件名
file_name = input("要下载的文件名：\n")
#5发送文件名到服务端
tcp_client_socket.send(file_name.encode("gbk"))
#6创建文件，并且准备保存
with open("C:/Users/lenovo/Desktop/"+file_name,"wb") as file:
    #7接受服务器的数据，保存到本地（循环）
    while True:
        file_data = tcp_client_socket.recv(1024)
        if file_data:
            file.write(file_data)
        else:
            break
#8关闭套接字
tcp_client_socket.close()
