"""
#1导入模块
#2t通过match   方法，验证正则
#3加个判断  是否匹配成功
#4如果成功获取匹配的结果
"""
import re
#2t通过match   方法，验证正则
    #re.match(正则表达式，要验证的字符串)
    #match()方法如果匹配成功，返回match_object对象
    #如果失败  返回None
#result = re.match("<([a-zA-Z0-9]+)>.*</\\1>","<html>textdsds</html>")
result = re.match("<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>","<html><h1>hihiiu</h1></html>")
#3加个判断  是否匹配成功
if result:
    print("匹配成功")
    print("匹配结果:", result.group())
else:
    print("匹配失败")
#4如果成功获取匹配的结果