"""
1导入模块
2创建套接字
3发送数据
4接受数据（二进制）
5解码数据，得到字符串
6打印字符串
7关闭套接字

"""
#1导入模块
import socket
#2创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#3发送数据
udp_socket.sendto("123123".encode(),("192.168.43.153",8070))
#4-----从套接字接受1024个字节的数据
            #---此方法会造成程序的阻塞     等待另外一台据算计发送来的数据
                #---如果对方发送数据  recvfrom  会自动解除阻塞

recv_data = udp_socket.recvfrom(1024)
#5解码
l = recv_data[0].decode("gbk")
#-6打印
print("来自：",recv_data[1],"的消息:",l)
#7关闭套接字

udp_socket.close()