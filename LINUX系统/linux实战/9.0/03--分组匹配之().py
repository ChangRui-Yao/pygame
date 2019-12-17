import re
#result = re.match("\w{4,20}@(163|126|qq|sina)\.com$","hello@qq.com")
result = re.match("(\d{3,4})-(\d{7,8})","012-12345678")

if result:
    print("匹配成功",result.group())
    print("匹配的区号：",result.group(1))
    print("匹配的电话号码：",result.group(2))
else:
    print("匹配失败")