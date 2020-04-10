import requests
from selenium import webdriver


class Climb_to_God:
    def __init__(self):
        '''
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            Accept-Encoding: gzip, deflate
            Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7
            Cache-Control: max-age=0
            Connection: keep-alive
            Cookie: name=value; ASP.NET_SessionId=gtprwhr5w1hqgz2cx0bgygq0; name=value
            Host: jwgl.wfust.edu.cn
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
        '''
        self.url = "http://jwgl.wfust.edu.cn/znpk/Pri_StuSel.aspx"
        self.headers = {
            "Cookie": "name=value; ASP.NET_SessionId=gtprwhr5w1hqgz2cx0bgygq0; name=value",
            "Host": "jwgl.wfust.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }

    def todo(self):
        res = requests.get(url=self.url, headers=self.headers).content.decode("gb2312")
        print(res)


if __name__ == '__main__':
    ctg = Climb_to_God()
    ctg.todo()
