#首先导入模块
import yagmail
#--使用yagmail对象发送邮件（发送人，登陆码，发送的服务器）
ya_obj = yagmail.SMTP(user="1520288462@qq.com",password="bbbdivmhlndajdij",host="smtp.qq.com")
content = "你好啊"

#--发送邮件，（收件人，主题，内容）
ya_obj.send("1564285867@qq.com", "测试", content)