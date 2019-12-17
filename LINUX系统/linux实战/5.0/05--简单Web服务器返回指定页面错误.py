"""
#1导入模块
#2创建套接字
#3设置地址重用
#4绑定端口
#5设置监听   让套接字由主动变为被动
#6接受客户端的连接       定义函数request_handler()
#7接受客户端发送的请求协议
#8判断协议是否为空
#9拼接响应报文
#10关闭操作

"""
import socket

def request_handler(new_client_socket,ip_port):
    """接受信息做出响应"""
    #7接受客户端发送的请求协议
    request_data = new_client_socket.recv(1024)
    #8判断协议是否为空
    if not request_data:
        print("[%s]客户端已经下线"% str(ip_port))
        new_client_socket.close()
        return
    #---根据浏览器请求的资源路径返回请求的资源(进行一次解码)
                #1）将请求协议进行解码的到字符串
    request_text = request_data.decode()
                #2）得到请求行
                        #1）查找第一个\r\n的位置
    loc = request_text.find("\r\n")
                        #2）截取字符串从开头到第一个\r\n的位置
    request_line = request_text[:loc]        
                #3）将请求行按照空格进行拆分 得到列表
    request_line_list = request_line.split(" ")
                #得到的请求资源路径
    file_path = request_line_list[1]
    print("[%s]正在请求：%s" % (str(ip_port),file_path))
    if file_path == "/":
        file_path = "index.html"

    #9拼接响应报文
    #响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    #响应头
    request_header = "Server:Python/30WS\r\n"
    #响应空行
    request_blank = "\r\n"
    #响应主体
    #response_body = "helloworld!"
    #返回 指定页面
    try:
        with open("G:/GitPro/pygame/LINUX系统/linux实战/5.0/static/"+file_path,"rb") as file:
            response_body = file.read()
    except Exception as e:
        #重新修改响应行 404
        #相应信息为错误信息
        response_line = "HTTP/1.1 404 Not Found \r\n"
        response_body = "Error! (%s)" % str(e)
        #将字符串转换为二进制
        response_body = response_body.encode("gbk")
        
   
    #--响应全体拼接
    response_data = (response_line + request_header +request_blank).encode() + response_body
    #10发送响应报文
    new_client_socket.send(response_data)

    #11关闭当前连接
    new_client_socket.close()


def main():
    """主入口"""
    #2创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #3设置地址重用
                                #当前套接字          地址重用            地址重用
    tcp_client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #4绑定端口
    tcp_client_socket.bind(("",8080))
    #5设置监听   让套接字由主动变为被动
    tcp_client_socket.listen(128)
    #6接受客户端的连接   
    while True:   
        new_client_socket,ip_port = tcp_client_socket.accept()
        print("新客户端上线：",ip_port)
        #7接受数据  响应请求
        request_handler(new_client_socket,ip_port)

if __name__ == "__main__":
    main()