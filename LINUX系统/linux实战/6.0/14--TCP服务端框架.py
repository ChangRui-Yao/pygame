"""
#1导入模块
#2创建套接字
#3设置地址可以重用
#4绑定端口
#5设置套接字由主动变被动
#6接受客户端连接
#7接受客户端方的信息
#8解码进行输出
#9进行关闭和当前客户端的连接
"""
#1导入模块
import socket
import threading
#定义函数接受信息
def recv_msage(new_server_socket,ip_port):
    while True:
        #7接受客户端方的信息
        recv_data = new_server_socket.recv(1024)
        if recv_data:
            #8解码进行输出
            recv_text = recv_data.decode("GBK")
            print("来自[%s]的信息：%s" % (ip_port,recv_text))
        else:
            break





#2创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3设置地址可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#4绑定端口
tcp_server_socket.bind(("",8080))
#5设置套接字由主动变被动
tcp_server_socket.listen(128)
while True:
    #6接受客户端连接
    new_server_socket,ip_port= tcp_server_socket.accept()
    print("欢迎新用户上线",ip_port)
    #recv_msage(new_server_socket,ip_port)

    #创建线程
    thread_recv_msage = threading.Thread(target=recv_msage,args=(new_server_socket,ip_port))
    #设置线程守护
    thread_recv_msage.setDaemon(True)
    #线程运行
    thread_recv_msage.start()

    #9进行关闭和当前客户端的连接
#tcp_server_socket.close()