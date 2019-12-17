def parse_request(request_data,ip_port):
    #---解析请求报文返回客户端资源路径
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
    return file_path




def application(current_dir,request_data,ip_port):
    file_path = parse_request(request_data,ip_port)
    resource_path = current_dir + file_path
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
        with open(resource_path,"rb") as file:
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
    
    return response_data
