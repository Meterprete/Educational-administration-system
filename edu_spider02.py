import requests

'''
    需要分别伪造两个请求：
        1. post: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=lq1Kk6XbZgUjUl2
        2.  get: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191
'''


class Climb_to_God:
    def __init__(self):
        self.url_1 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=lq1Kk6XbZgUjUl2"
        self.url_2 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191"
        self.headers_1 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "115",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "name=value; ASP.NET_SessionId=3k2ghr55504nvrqc4sfreim0; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Origin": "http://jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.headers_2 = {
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7",
            "Connection": "keep-alive",
            "Cookie": "name=value; ASP.NET_SessionId=3k2ghr55504nvrqc4sfreim0; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=lq1Kk6XbZgUjUl2",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.data = {
            "Sel_XNXQ": "20191",
            "rad": "0",
            "px": "0",
            "txt_yzm": "",
            "hidyzm": "a922b47c8c34e4a4a8152bc00d19bfz",
            "hidsjyzm": "1F7992283ABBA56EF61994093E8E706B"
        }

    def todo(self):
        # ses = requests.session()
        mr = requests.post(url=self.url_1, headers=self.headers_1, data=self.data)
        res = requests.get(url=self.url_2, headers=self.headers_2).content
        with open("test3.jpg", "wb") as f:
            f.write(res)
        print("ok")


if __name__ == '__main__':
    ctg = Climb_to_God()
    ctg.todo()
