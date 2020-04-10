import execjs
import os
import requests
import re


class GET_EXECJS:
    def __init__(self):
        useragnt = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

        url_first = "http://jwgl.wfust.edu.cn/home.aspx"
        self.session = requests.session()
        self.session.get(url=url_first)
        # print(self.session.cookies["ASP.NET_SessionId"])

        '''获取VIEWSTATE'''
        verty_url = "http://jwgl.wfust.edu.cn/_data/login_home.aspx"
        headers_Verty = {
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/home.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": useragnt
        }
        res = self.session.get(url=verty_url, headers=headers_Verty).content.decode("gb2312")
        self.VIEWSTATE = re.findall(r'''name="__VIEWSTATE" value="(.*?)"''', res)[0]
        # print(self.VIEWSTATE)

        '''获取验证码和登录的headers'''
        self.getCode_loginHeaders = {
            "Host": "jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/_data/login_home.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": useragnt
        }

        '''登录的login的url'''
        self.login_url = "http://jwgl.wfust.edu.cn/_data/login_home.aspx"

        '''请求验证码的url'''
        self.Vcode_url = "http://jwgl.wfust.edu.cn/sys/ValidateCode.aspx"

    def run(self):
        os.environ["EXECJS_RUNTIME"] = "PhantomJS"
        with open("md5.js", "r") as f:
            jsData = f.read()

        try:
            userid = input("请输入学号：\n")
            pwd = input("请输入密码\n")
            res = execjs.compile(jsData).call("usermd5", userid, pwd)
            # # resrc = execjs.compile(jsData).call("changeValidateCode")
            # img = self.session.get(url=resrc, headers=self.headers).content
            '''获取验证码'''
            img = self.session.get(url=self.Vcode_url, headers=self.getCode_loginHeaders).content
            with open("vertify.jpg", "wb") as f:
                f.write(img)

            '''输入验证码'''
            verty_text = input("请输入验证码：\n")
            rem = execjs.compile(jsData).call("usermmdd55", verty_text)
            # print(verty_text)
            # print(rem)

            post_data = {
                "__VIEWSTATE": self.VIEWSTATE,
                "pcInfo": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 SN:NULL",
                "txt_mm_expression": "",
                "txt_mm_length": "",
                "txt_mm_userzh": "",
                "typeName": "(unable to decode value)",
                "dsdsdsdsdxcxdfgfg": res,
                "fgfggfdgtyuuyyuuckjg": rem,
                "Sel_Type": "STU",
                "txt_asmcdefsddsd": userid,
                "txt_pewerwedsdfsdff": "",
                "txt_psasas": "(unable to decode value)"
            }
            self.session.post(url=self.login_url, headers=self.getCode_loginHeaders,
                              data=post_data).content.decode("gb2312")
            return self.session.cookies["ASP.NET_SessionId"]

        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_execjs = GET_EXECJS()
    get_execjs.run()
