"""
#1把WEB服务器返回固定内容，代码拷贝
#2把原本返回的固定内容改为从数据库动态读取
        #1导入pymysql
        #2连接数据库查询所有影片信息
        #3遍历查询的结果集 ，拼接相应的主体


"""
import socket
import pymysql

def request_handler(new_client_socket,ip_port):
    """接受信息做出响应"""
    #7接受客户端发送的请求协议
    request_data = new_client_socket.recv(1024)
    #print(request_data)
    #8判断协议是否为空
    if not request_data:
        print("[%s]客户端已经下线"% str(ip_port))
        new_client_socket.close()
        return
    #9拼接响应报文
    #响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    #响应头
    request_header = "Server:123.465\r\n"
    request_header +="Content-Type:text/html;charset=utf-8\r\n"
    #响应空行
    request_blank = "\r\n"
    #响应主体
    response_body = ""
    #2把原本返回的固定内容改为从数据库动态读取
        #1导入pymysql
        #2连接数据库查询所有影片信息
    conn = pymysql.connect(host="192.168.43.153",user="jiangfeng",password="123456",port=3306,database="movie_db")
    cur = conn.cursor()
    cur.execute("select * from movie_link order by id desc")
    result_list = cur.fetchall()
    for row in result_list:
        response_body += "%d.%s     下载地址:[<a href='%s'>%s</a>] <br>" % (row[0],row[1],row[2],row[2])
    cur.close()
    conn.close()
        #3遍历查询的结果集 ，拼接相应的主体

    response_data = response_line + request_header +request_blank +response_body
    #10发送响应报文
    new_client_socket.send(response_data.encode())

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