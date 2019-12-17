def create_http_response(status,response_body):
        #9拼接响应报文
        #响应行
    response_line = "HTTP/1.1 %s\r\n" % status
        #响应头
    request_header = "Server:Python/30WS\r\n"
    request_header += "Content-Type: text/html\r\n"
        #响应空行
    request_blank = "\r\n"
        #响应主体
        #response_body = "helloworld!"
        #返回 指定页面
            
    response_data = (response_line + request_header +request_blank).encode() + response_body
    return response_data