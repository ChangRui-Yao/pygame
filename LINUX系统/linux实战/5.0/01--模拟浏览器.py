"""
#1导入模块
#2创建套接字
#3建立连接
#4拼接请求协议
#5发送请求协议
#6接受服务器相应内容
#7保存内容
#8关闭连接

"""
#1导入模块
import socket
#2创建套接字
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3建立连接
tcp_client_socket.connect(("www.icoderi.com",80))
#4拼接请求协议
    #4.1请求行
request_line = "GET / HTTP/1.1\r\n"
    #4.2请求头
request_header = "Host:www.icoderi.com\r\n"
    #4.3请求空行
request_blank = "\r\n"
    #整天拼接
request_data = request_line + request_header + request_blank 
#5发送请求协议
tcp_client_socket.send(request_data.encode())
#6接受服务器相应内容
recv_data = tcp_client_socket.recv(4096)        #4096=4k
recv_text = recv_data.decode()
#7保存内容
        #7.1\r\n的位置
loc = recv_text.find("\r\n\r\n")
        #7.2截取字符串
html_data = recv_text[loc+4:]
print(html_data)
        #7.3保存内容到文件中
with open("index.html","w") as file:
    file.write(html_data)
#8关闭连接
tcp_client_socket.close()