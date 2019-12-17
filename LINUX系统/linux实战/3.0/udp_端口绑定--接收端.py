#1导入模块
import socket
#2创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定发送端地址
udp_socket.bind(("192.168.43.153",12346))


#4-----从套接字接受1024个字节的数据
            #---此方法会造成程序的阻塞     等待另外一台据算计发送来的数据

              #---如果对方发送数据  recvfrom  会自动解除阻塞

while True:
    recv_data,ip_port = udp_socket.recvfrom(1024)
    str(recv_data, encoding = "utf-8") 
    if str(recv_data, encoding = "utf-8") == "ok":
        s = "服务器即将关闭"
        udp_socket.sendto(bytes(s,encoding = "utf-8"),ip_port)
        break
    #-6打印
    print("用户：",ip_port[0],"端口：",ip_port[1],"数据",str(recv_data, encoding = "utf-8"))


    s = "测试"
    udp_socket.sendto(recv_data,ip_port)
    #7关闭套接字

udp_socket.close()