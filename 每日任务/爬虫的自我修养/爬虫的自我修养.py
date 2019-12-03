#-----如何访问互联网
import urllib.request
import urllib.parse
import json
import time
import random
class Youdao:
    def __init__(self, msg):
        self.msg = conter
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.D = "n%A-rKaT5fb[Gy?;N5@Tj"
        self.salt = self.get_salt()
        self.sign = self.get_sign()
        self.ts = self.get_ts()

    def get_md(self, value):
        
        # md5加密
        m = hashlib.md5()
        # m.update(value)
        m.update(value.encode('utf-8'))
        return m.hexdigest()
    def get_salt(self):
        # 根据当前时间戳获取salt参数
        s = int(time.time() * 1000) + random.randint(0, 10)
        return str(s)

    def get_sign(self):
        # 使用md5函数和其他参数，得到sign参数
        s = "fanyideskweb" + self.msg + self.salt + self.D
        return self.get_md(s)

    def get_ts(self):
        # 根据当前时间戳获取ts参数
        s = int(time.time() * 1000)
        return str(s)


conter = input("请输入要翻译的内容")
r = Youdao(conter)

data = {}
data["i"] = self.msg
data["from"] = " AUTO"
data["to"] = " AUTO"
data["smartresult"] = " dict"
data["client"] = " fanyideskweb"
data["salt"] = r.self.salt,
data["sign"] = r.self.sign,
data["ts"] = r.self.ts
data["bv"] = " 140f03b6cc43b5b1fabe089d78dc366f"
data["doctype"] = " json"
data["version"] = " 2.1"
data["keyfrom"] = " fanyi.web"
data["action"] = " FY_BY_CLICKBUTTION"
data = urllib.parse.urlencode(data).encode("utf-8")

head = {}
head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
head["Cookie"] = "OUTFOX_SEARCH_USER_ID=1107576775@10.168.8.63; JSESSIONID=aaaqfllQWZNda_0ZSid6w; OUTFOX_SEARCH_USER_ID_NCOO=195122552.92085916; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; ___rl__test__cookies=1574224187831"
head["Referer"] = "http://fanyi.youdao.com/"


req = urllib.repuest.Request(url,data,head)
response = urllib.request.urlopen(url,data)
html = response.read().decode("utf-8")


target = json.loads(html)
target = target['translateResult'][0][0]['tgt']
print(target)
