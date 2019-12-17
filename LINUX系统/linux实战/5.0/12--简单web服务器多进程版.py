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
import multiprocessing
"""
1在类的初始化方法中配置当前的项目
{"2048":"./2048"}
2给类增加初始化项目配置的方法init__porject()
        2.1显示可以可以发布的所有游戏 菜单
        2.2接受用户的选择
        2.3根据用户的选择发布指定的项目{保存用户选择的游戏选择的目录}
3更改web服务器打开的文件目录


"""

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
        #定义类的实例属性    字典为空
        self.projects_dict = dict()

        #定义实例属性，保存要发布的项目的路径
        self.current_dir = ""
        #
        self.projects_dict["植物大战僵尸--普通版"] = "zwdzjs-vl"
        self.projects_dict["植物大战僵尸--外挂版"] = "zwdzjs-v2"
        self.projects_dict["保卫萝卜"] = "tafang"
        self.projects_dict["读心术"] = "dxs"
        self.projects_dict["2048"] = "2048"
        print(self.projects_dict)
        
        #调用初始化游戏项目的方法
        self.init__porject()

    #-定义一个初始化项目的方法
    def init__porject(self):
        # 2.1 显示所有可以发布的游戏菜单
        # list(self.projects_dict.keys()) 取出字典的key 并且转换为列表
        keys_list = list(self.projects_dict.keys())
        # 遍历显示所有的key
        # enumerate(keys_list)
        # [(0,'植物大战僵尸v1'), (1, '植物大战僵尸v2') ...]
        for index, game_name in enumerate(keys_list):
            print("%d.%s" % (index,game_name))
        # 2.2 接收用户的选择
        sel_no = int(input("请选择要发布的游戏序号:\n"))
        # 2.3 根据用户的选择发布指定的项目 （保存用户选择的游戏对应的本地目录）
        #  根据用户的选择，得到游戏的名称（字典的key）
        key = keys_list[sel_no]
        #  根据字典的key 得到项目的具体路径
        self.current_dir = self.projects_dict[key]

    
    def start(self):
        #启动服务器
        print("web服务器已经启动，等待客户端连接中....")
        #6接受客户端的连接   
        while True:
            new_client_socket,ip_port = self.tcp_client_socket.accept()
            print("新客户端上线：",ip_port)
            #7接受数据  响应请求
            #self.request_handler(new_client_socket,ip_port)


            #进程使用三步
            #导入模块
            #创建进程对象
            p1 = multiprocessing.Process(target=self.request_handler,args=(new_client_socket,ip_port))
            #子进程启动
            p1.start()
            
            new_client_socket.close()


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
        response_data = app.application(self.current_dir,request_data,ip_port)
        
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