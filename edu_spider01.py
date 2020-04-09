import requests
from selenium import webdriver


class Climb_to_God:
    def __init__(self):
        '''
            Cookie: name=value; ASP.NET_SessionId=gtprwhr5w1hqgz2cx0bgygq0; name=value
            Host: jwgl.wfust.edu.cn
            Referer: http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=TGTki6XqpxHrKkW
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
        '''
        self.url = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_Drawimg.aspx?type=1&w=1100&h=500&xnxq=20191"
        self.headers = {
            "Cookie": "name=value; ASP.NET_SessionId=gtprwhr5w1hqgz2cx0bgygq0; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel_rpt.aspx?m=ktIITewQmXzy7VK",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }

    def todo(self):
        res = requests.get(url=self.url, headers=self.headers).content.decode("gb2312")
        print(res)


if __name__ == '__main__':
    ctg = Climb_to_God()
    ctg.todo()
