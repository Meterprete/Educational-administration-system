import requests
import re

'''
    需要分别伪造两个请求：
        3. get: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx
        1. post: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=lq1Kk6XbZgUjUl2
        2. get: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191
'''


class Climb_to_God:
    def __init__(self):
        url_3 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx"
        self.headers_3 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "name=value; ASP.NET_SessionId=tczfnpzsjksmpg55eih3by55; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        '''获取 hidyzm hidsjyzm s'''
        res = requests.get(url=url_3, headers=self.headers_3).content.decode("gb2312")
        hidyzm = re.findall(r'''name="hidyzm" value="(.*?)"''', res)[0]
        from Testing_phase.test_execjs import GET_EXECJS
        ge = GET_EXECJS()
        rpe = ge.run()
        # print(type(rpe))
        # print({"hidyzm": hidyzm})

        self.url_1 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m={}".format(rpe["s"])
        self.url_2 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191"
        self.headers_1 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "115",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "name=value; ASP.NET_SessionId=tczfnpzsjksmpg55eih3by55; name=value",
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
            "Cookie": "name=value; ASP.NET_SessionId=tczfnpzsjksmpg55eih3by55; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m={}".format(rpe["s"]),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }

        self.data = {
            "Sel_XNXQ": "20191",
            "rad": "0",
            "px": "0",
            "txt_yzm": "",
            "hidyzm": "{}".format(hidyzm),
            "hidsjyzm": "{}".format(rpe["hidsjyzm"])
        }

    def todo(self):
        '''获取课程表'''
        requests.post(url=self.url_1, headers=self.headers_1, data=self.data)
        res = requests.get(url=self.url_2, headers=self.headers_2).content
        with open("test3.jpg", "wb") as f:
            f.write(res)
        print("ok")


if __name__ == '__main__':
    ctg = Climb_to_God()
    ctg.todo()
