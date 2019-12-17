"""
一、功能
1、发送信息
2、接收信息
3、退出系统

二、框架的设计
1、发送信息 send_msg()
2、接收信息 recv_msg()
3、程序的主入口 main()
4、当程序独立运行的时候，才启动聊天器

三、实现步骤
1、发送信息 send_msg()
1) 定义变量接收用户与输入的接收方的IP地址
2）定义变量接收用户与输入的接收方的端口号
3)定义变量接收用户与输入的接收方的内容
4）使用socket的sendto() 发送信息

2、接收信息 recv_msg()
1) 使用socket 接收数据
2）解码数据
3）输出显示

3、主入口main()
1）创建套接字
2）绑定端口
3）打印菜单（循环）
4）接收用户输入的选项
5）判断用户的选择，并且调用对应的函数
6）关闭套接字

"""
import socket
import threading


def send_msg(udp_socket):
    """发送信息的函数"""
    # 1) 定义变量接收用户与输入的接收方的IP地址
    ipaddr = input("请输入接收方的IP地址：\n")
    # 判断是否需要默认
    if len(ipaddr) == 0:
        ipaddr = "192.168.150.93"
        print("当前接收方默认IP设置为[%s]" % ipaddr)
    # 2）定义变量接收用户与输入的接收方的端口号
    port = input("请输入接收方的端口号：\n")
    if len(port) == 0:
        port = "8080"
        print("当前接收方默认端口设置为[%s]" % port)
    # 3)定义变量接收用户与输入的接收方的内容
    content = input("请输入要发送的内容：\n")
    # 4）使用socket的sendto()发送信息
    udp_socket.sendto(content.encode(), (ipaddr, int(port)))


def recv_msg(udp_socket):
    """接收信息的函数"""

    while True:
        # 1) 使用socket接收数据
        # (b'\xe4\xbc\x91\xe6\x81\xaf\xe4\xbc\x91\xe6\x81\xaf\xe6\x89\x80', ('192.168.150.93', 8080))
        recv_data, ip_port = udp_socket.recvfrom(1024)
        # 2）解码数据
        recv_text = recv_data.decode()
        # 3）输出显示
        print("接收到[%s]的消息：%s" % (str(ip_port), recv_text))


def main():
    """程序的主入口"""
    # 1）创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2）绑定端口
    # address ---> ("ip地址", 端口号)
    # udp_socket.bind(address)
    udp_socket.bind(("", 8080))

    # 创建子线程，单独接收用户发送的信息
    thread_recvmsg = threading.Thread(target=recv_msg, args=(udp_socket, ))
    # 设置子线程守护主线程
    thread_recvmsg.setDaemon(True)
    # 启动子线程
    thread_recvmsg.start()

    while True:
        # 3）打印菜单（循环）
        print("\n\n***************************")
        print("******  1、发送信息  *******")
        print("******  2、退出系统  *******")
        print("***************************")
        # 4）接收用户输入的选项
        sel_num = int(input("请输入选项:\n"))
        # 5）判断用户的选择，并且调用对应的函数
        if sel_num == 1:
            # print("您选择的是发送信息")
            # 调用发送信息的函数
            send_msg(udp_socket)

        elif sel_num == 2:
            print("系统正在退出中...")
            print("系统退出完成!")
            break
    # 6）关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    # 程序独立运行的时候，才去启动聊天器
    main()