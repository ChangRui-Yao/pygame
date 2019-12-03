import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")


    return html


def get_img(html):
    p = r'<img class="BDE_Image" pic_type="\d" width="\d\d\d" height="\d\d\d" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)


    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)

##    for each in imglist:
##        print(each)
##    
##



if __name__ == "__main__":
    url = "https://tieba.baidu.com/p/6341789574"
    get_img(open_url(url))
