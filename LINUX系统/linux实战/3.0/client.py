#1导入模块
import socket
#2创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#udp_socket.bind(("",12345))
#3发送数据
while True:
    ll = input("请输入数据：")
    s =ll.encode("utf-8")
    udp_socket.sendto(s,("127.0.0.1",12346))


    #4-----从套接字接受1024个字节的数据
                #---此方法会造成程序的阻塞     等待另外一台据算计发送来的数据
                    #---如果对方发送数据  recvfrom  会自动解除阻塞
    recv_data,ip_port = udp_socket.recvfrom(1024)
    l = str(recv_data, encoding = "utf-8")
    if l == "服务器即将关闭":
        break

    #-6打印
    print("服务器返回数据:",recv_data)
    #7关闭套接字

udp_socket.close()
