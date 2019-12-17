"""
#1导入模块
#2创建套接字tcp()
#3建立连接
#4发送数据
#5关闭套接字

"""
#1导入模块
import socket
#2创建套接字tcp()
#---SOCK_STREAM是创建tcp套接字
#---SOCK_DGRAM  创建udp套接字
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3建立连接
tcp_client_socket.connect(("allianceshan.top",8080))
#4发送数据
tcp_client_socket.send("约吗？".encode("gbk"))


#--接收数据
recv_data = tcp_client_socket.recv(1024)
recv_text = recv_data.decode("gbk")
print(recv_text)
#5关闭套接字
tcp_client_socket.close()
