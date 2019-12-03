import hashlib
import random
import time
import requests
import json

"""
向有道翻译发送data，得到翻译结果
"""

class Youdao:
    def __init__(self, msg):
        self.msg = msg
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

    def get_result(self):
        Form_Data = {
            'i': self.msg,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'c6b8c998b2cbaa29bd94afc223bc106c',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
        }

        headers = {
            'Cookie': 'JSESSIONID=abcI8vi85BiXY6-VC7d6w; OUTFOX_SEARCH_USER_ID=329906099@123.113.30.232; _ntes_nnid=72d661d48d8b1683840b81a7a767ec62,1574171433290; OUTFOX_SEARCH_USER_ID_NCOO=1108813591.6937714; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; ___rl__test__cookies=1574174850663',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.post(self.url, data=Form_Data, headers=headers).text
        translate_results = json.loads(response)
        # 找到翻译结果
        if 'translateResult' in translate_results:
            translate_results = translate_results['translateResult'][0][0]['tgt']
            print("翻译的结果是：%s" % translate_results)
        else:
            print(translate_results)


if __name__ == "__main__":
    # m = hashlib.md5()
    #     # m.update(value)
    # m.update("2.1".encode('utf-8'))
    # str = m.hexdigest()
    while True:
        strdata = input("输入内容")
        if strdata == "ok":
            break
        y = Youdao(strdata)
        y.get_result()
