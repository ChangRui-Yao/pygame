"""
#1导入模块
#2创建套接字
#3绑定端口
#4设置监听，设置套接字由主动到被动
#5接受客户端连接
#6接受客户端发送的文件名
#7根据文件名读取文件内容
#8吧读取的内容发送给客户端（循环）
#9关闭和当前客户的连接
#10，关闭服务器
"""
#1导入模块
import socket
#2创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置套接字地址可以重用
#tcp_server_socket.setsockopt(当前套接字，属性名，属性值)
#socket.SO_REUSEADDR    地址是否可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#3绑定端口
tcp_server_socket.bind(("",8888))
#4设置监听，设置套接字由主动到被动
tcp_server_socket.listen(128)
#5接受客户端连接
while True:
    new_client_socket,ip_port = tcp_server_socket.accept()
    print("欢迎新客户端", ip_port)
    #6接受客户端发送的文件名
    recv_data = new_client_socket.recv(1024)
    recv_name = recv_data.decode()
    print(recv_name)
    try:
        #7根据文件名读取文件内容
        with open("G:/GitPro/pygame/LINUX系统/linux实战/4.0/"+recv_name,"rb") as file:
            while True:
                file_data = file.read(1024)
                if file_data:
                #8吧读取的内容1发送给客户端（循环）
                    new_client_socket.send(file_data)
                else:
                    break
    except Exception as e:
        print("[%s]下载失败" % recv_name)
    else:
        print("[%s]下载成功" % recv_name)
    #9关闭和当前客户的连接
    new_client_socket.close()
#10，关闭服务器
tcp_server_socket.close()