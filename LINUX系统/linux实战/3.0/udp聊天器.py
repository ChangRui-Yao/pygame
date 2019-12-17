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
import socket
def send_msg():
    """发送信息"""
    pass
def recv_msg():
    """接受信息"""
    pass
def main():
    """程序的主入口"""
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",8080))
    while True:
        print("\n\n**************************")
        print("*******1,发送信息*********")
        print("*******2,接受信息*********")
        print("*******3,退出系统*********")
        print("**************************")
        sel_num = int(input("请输入选项:\n"))
        if sel_num ==1:
            print("你选择地是发送信息")
        elif sel_num ==2:
            print("你选择地是接收接收信息")
        elif sel_num ==3:
            print("系统正在退出中....")
            print("系统退出完成！")
            break
        
    udp_socket.close()
if __name__ == "__main__":
    
    main()