from application import utils
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
    try:
        #通过withopen读取文件
        with open(resource_path,"rb") as file:
            response_body = file.read()
            #调用utils模块的这个函数 拼接响应协议
        response_data = utils.create_http_response("200 OK",response_body)
        
    except Exception as e:
        response_body = "Error! (%s)" % str(e)
        #将字符串转换为二进制
        response_body = response_body.encode()        
    
        #--响应全体拼接
        #调用utils模块的这个函数 拼接响应协议
        response_data = utils.create_http_response("404 Not found", response_body)

    return response_data

    

    