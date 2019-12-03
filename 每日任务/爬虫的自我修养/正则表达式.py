import re
s = "I love jiangfeng iiiiii.love 123 123"
#-----search  是用于在字符串中搜索正则表达式模式第一次出现的位置

print(re.search(r"jiangfeng",s))


#---元字符.点号可以匹配任何字符
print(re.search(r".","I love jiangfeng iiiiii.love123123"))

#---匹配点号本身则需要加上转义字符反斜杠\

print(re.search(r"\.","I love jiangfeng iiiiii.love123123"))

#---反斜杠可以使的别的字符有特殊含义

print(re.search(r"\d","I love jiangfeng iiiiii.love123123"))

#----多个\d    就会匹配连续式三个字符的数

print(re.search(r"1*","I love jian111111gfeng iiiiii.love123111111123"))

#---[]可以用元字符中括号  生成一个字符串 []里面的所有元字符都会失去他原来的功能 除了几个特殊的   匹配到字符串的中任意一个  就会返回他
                                                                #----   -小横杠  表示一个范围
print(re.search(r"[jiang]","I love jiangfeng iiiiii.love123123"))

#---在[]中括号中  你可以给他一个-短横杠   表示给他一个范围

print(re.search(r"[a-z]","I love jiangfeng iiiiii.love123123"))

#----可以设置某个字符匹配的次数
print(re.search(r"ab{3}c","I love jiangfeng iiiiii.love123123  abbbbbbbc  abbbc"))

#----可以设置某个字符重复的次数 {}大括号   {0,1}{3,9}
print(re.search(r"ab{3,10}c","I love jiangfeng iiiiii.love123123  abbbbbbbc  abbbc"))

#----------------------问题怎么匹配255之内的某一个数
print(re.search(r"[0-2][0-5][0-5]","I love jiangfeng iiiiii.321255love123123  abbbbbbbc  abbbc"))

#---------------------怎么匹配一个ip地址
print(re.search(r"(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])","266.266.266.266   255.255.255.255   254.254.254.254  192.168.0.1"))

print(re.search(r"(([0-2][0-5][0-5])\.){3}([0-2][0-5][0-5])"," 255.255.255.255"))

print(re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])","1.1.1.1"))
print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',' 1.1.1.1'))

