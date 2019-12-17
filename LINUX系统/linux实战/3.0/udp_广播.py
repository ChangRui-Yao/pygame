"""
1导入模块
2创建套接字
3设置广播权限
4发送数据
5关闭套接字
"""

#1导入模块
import socket
#2创建套接字
#                           IPV4               UDP
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3设置广播权限
            #--套接字默认不允许发送广播
            #--需要用setsockopt(套接字，属性，属性值)
            #--socket.SOL_SOCKET-----当前套接字
            #---socket.SO_BROADCAST-----发送广播
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
#4发送数据
udp_socket.sendto("服务器即将关闭".encode("gbk"),("192.168.3.255",8080))
#5关闭套接字
udp_socket.close()