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
class WebServer(object):
    def __init__(self):
            #2创建套接字
        tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #3设置地址重用
                                    #当前套接字          地址重用            地址重用
        tcp_client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        #4绑定端口
        tcp_client_socket.bind(("",8080))
        #5设置监听   让套接字由主动变为被动
        tcp_client_socket.listen(128)
        #定义实例属性保存套接字对象
        self.tcp_client_socket = tcp_client_socket
    def start(self):
        #启动服务器
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
        #s使用application问价加的的app模块的appliceation()
        response_data = app.application("G:/GitPro/pygame/LINUX系统/linux实战/5.0/static/",request_data,ip_port)
        
            #10发送响应报文
        new_client_socket.send(response_data)
        #关闭连接
        new_client_socket.close()

def main():
    """主入口"""
    #创建webServer对象
    #调用对象的.start()启动web服务器
    ws = WebServer()
    ws.start()
    
    

if __name__ == "__main__":
    main()