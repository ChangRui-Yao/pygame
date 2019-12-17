"""
#1导入模块
#2创建套接字
#3绑定端口和ip
#4开启监听（设置套接字为被动模式）
#5等待客户端连接
#6收发数据
#7关闭连接


"""
#1导入模块
import socket
#2创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3绑定端口和ip
tcp_server_socket.bind(("192.168.3.19",10000))
#4开启监听（设置套接字为被动模式）
#listen() 的作用设置  tcp_sever_socket 这个套接字为被动监听模式,不能主动发送数据
#128  允许接收的最大连接数，在windows 128有效   ，Linux此数字无效
tcp_server_socket.listen(128)
#5等待客户端连接
#-----开始接收客户端连接 程序会进入阻塞状态 如果有客户端连接  自动解除阻塞 往下执行
#recv_data有两部分
#               第一部分返回一个新的套接字
#                第二部分客户端的ip地址和端口号
new_client_socket,client_ip_port = tcp_server_socket.accept()
print("新客户端上线了:%s" % str(client_ip_port))
#6收发数据
#----recv会让程序进一步阻塞   ，收到信息后解除阻塞
recv_data = new_client_socket.recv(1024)
recv_text = recv_data.decode("gbk")
print("接受到[%s]的信息:%s" % (str(client_ip_port),recv_text))
#--------------这句话关闭表示不能再和当前的客户端通信
new_client_socket.close()
#7关闭连接
#tcp_server_socket.close()表示程序不再接受新的客户端连接
tcp_server_socket.close()