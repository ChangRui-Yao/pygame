"""
#1导入模块
#2t通过match   方法，验证正则
#3加个判断  是否匹配成功
#4如果成功获取匹配的结果
"""
import re
result = re.match("^[0-9]?[0-9]$|^100$","100")
#3加个判断  是否匹配成功
if result:
    print("匹配成功")
    print("匹配结果:", result.group())
else:
    print("匹配失败")
#4如果成功获取匹配的结果