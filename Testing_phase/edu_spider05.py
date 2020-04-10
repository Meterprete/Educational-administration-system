import requests
import re


class Climb_to_God:
    def __init__(self):
        from Testing_phase.test_execjs02 import GET_EXECJS
        get_execjs = GET_EXECJS()
        ASP_NET_SessionId = get_execjs.run()
        url_3 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx"
        cookie = "name=value; ASP.NET_SessionId={}; name=value".format(ASP_NET_SessionId)
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        self.headers_3 = {
            "Cookie": cookie,
            "Host": "jwgl.wfust.edu.cn",
            "User-Agent": useragent
        }

        '''获取 hidyzm hidsjyzm s'''
        res = requests.get(url=url_3, headers=self.headers_3).content.decode("gb2312")
        hidyzm = re.findall(r'''name="hidyzm" value="(.*?)"''', res)[0]
        from Testing_phase.test_execjs import GET_EXECJS
        ge = GET_EXECJS()
        rpe = ge.run()

        self.url_1 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m={}".format(rpe["s"])
        self.url_2 = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191"
        self.headers_1 = {
            "Cookie": cookie,
            "Host": "jwgl.wfust.edu.cn",
            "Origin": "http://jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx",
            "User-Agent": useragent
        }
        self.headers_2 = {
            "Cookie": cookie,
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m={}".format(rpe["s"]),
            "User-Agent": useragent
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
