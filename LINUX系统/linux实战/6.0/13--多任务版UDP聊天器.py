"""
一，功能
1发送信息
2接受信息
3退出系统
二，框架设计
1，发送信息 send_msg()
2，接受信息 recv_msg()
3，程序的主入口  main()
4，当程序独立运行的时候 才启动聊天器
三，实现步骤
1发送信息send_msg()
        1)定义变量接受用户输入的IP地址
        2）定义变量接受用户输入的端口号
        3）定义变量接受用户输入的内容
        4）sendto()发送信息
2接受信息recv_msg()
        1）使socket接收数据
        2）解码数据
        3）显示数据
3主入口main()
        1）创建socket
        2）绑定端口
        3）打印菜单（循环多次）
        4）接收用户输入的选项
        5）判断用户的选择调用对应的函数
        6）关闭套接字
"""
import threading
import socket
def send_msg(udp_socket):
    """发送信息"""
    ipaddr = input("请输入接收方的ip地址:\n")
    if len(ipaddr) == 0:
        ipaddr = "192.168.3.19"
        print("当前默认接收地址为[%s] " % ipaddr)
    port = input("请输入接收方的端口:\n")
    if len(port) == 0:
        port = "8070"
        print("当前默认接收端口为[%s]" % port)
    content = input("请输入发送内容:\n")
    udp_socket.sendto(content.encode("gbk"),(ipaddr,int(port)))


def recv_msg(udp_socket):
    """接受信息"""
    while True:
        recv_data,ip_post = udp_socket.recvfrom(1024)
        recv_text = recv_data.decode()
        print("接收到[%s]的消息:%s" % (str(ip_post),recv_text))


    
def main():
    """程序的主入口"""
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",8080))
    print("\n\n**************************")
    print("*******1,发送信息*********")
    print("*******2,退出系统*********")
    print("**************************")
    #创建子线程 ，单独接受用户信息
    t1 = threading.Thread(target = recv_msg,args=(udp_socket, ))
    #子线程守护主线程
    t1.setDaemon(True)
    #启动子线程
    t1.start()
    while True:
        sel_num = int(input("请输入选项:\n"))
        if sel_num ==1:
            print("你选择地是发送信息")
            send_msg(udp_socket)
        #elif sel_num ==2:
            #print("你选择地是接收2信息")
            #recv_msg(udp_socket)
        elif sel_num ==2:
            print("系统正在退出中....")
            print("系统退出完成！")
            exit()
        else:
            print("你的输入有误")
        
    udp_socket.close()
if __name__ == "__main__":
    
    main()