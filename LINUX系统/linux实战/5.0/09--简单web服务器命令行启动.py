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
from application import app
import sys
class WebServer(object):
    def __init__(self,port):
            #2创建套接字
        tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #3设置地址重用
                                    #当前套接字          地址重用            地址重用
        tcp_client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        #4绑定端口
        tcp_client_socket.bind(("",port))
        #5设置监听   让套接字由主动变为被动
        tcp_client_socket.listen(128)
        #定义实例属性保存套接字对象
        self.tcp_client_socket = tcp_client_socket
    def start(self):
        #启动服务器
        print("web服务器已经启动，等待客户端连接中....")
        #6接受客户端的连接   
        while True:
            new_client_socket,ip_port = self.tcp_client_socket.accept()
            print("新客户端上线：",ip_port)
            #7接受数据  响应请求
            self.request_handler(new_client_socket,ip_port)
        


    def request_handler(self,new_client_socket,ip_port):
        """接受信息做出响应"""
        #7接受客户端发送的请求协议
        request_data = new_client_socket.recv(1024)
        #8判断协议是否为空
        if not request_data:
            print("[%s]客户端已经下线"% str(ip_port))
            new_client_socket.close()
            return
        #s使用application文件夹下的app模块的appliceation()
        response_data = app.application("/home/jiangfeng/static/",request_data,ip_port)
        
            #10发送响应报文
        new_client_socket.send(response_data)
        #关闭连接
        new_client_socket.close()

def main():
    """主入口"""

    #导入sys模块
    #获取系统传递到程序的参数
    #params_list = sys.argv()    
    #判断参数格式是否正确
    if len(sys.argv) != 2:
        print("启动失败，参数格式错误！正确格式：python3 xxx.py 端口号")
        return
    #判断端口号是否为数字
    if not sys.argv[1].isdigit():
        print("启动失败，端口号不是一个纯数字")
        return
    #获取端口号
    port = int(sys.argv[1])
    #启动web服务器的时候使用指定端口

    #创建webServer对象
    #调用对象的.start()启动web服务器
    ws = WebServer(port)
    ws.start()
    
    

if __name__ == "__main__":
    main()