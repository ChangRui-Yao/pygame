#1导入模块
#2创建套接字
#3发送数据
#4关闭套接字
#导入模块
import socket
#2创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3发送数据
        #udp_spcket.sendto(要发送数据的二进制格式，对方的IP和端口)
                                #1参数一   字符串转换为二进制    字符串.encode()
                                #2参数二   对方IP和端口号为元组  
                                        #("ip地址"，端口号
udp_socket.sendto("hello world".encode(),("192.168.43.153",8080))
#4关闭  套接字
udp_socket.close()