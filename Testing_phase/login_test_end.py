import requests


class Login:
    def __init__(self):
        self.data = {
            "__VIEWSTATE": "356iN5YCZIVw8L2ZvbnRcPidcOwogICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidHh0X3Bld2Vyd2Vkc2Rmc2RmZiIpLnZhbHVlID0gJydcOwogZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInR4dF9zZGVydGZnc2Fkc2N4Y2Fkc2FkcyIpLnZhbHVlID0gJydcOyAKIHJldHVybiB0cnVlXDt9CiB9CmZ1bmN0aW9uIFNlbFR5cGUob2JqKXsKIHZhciBzPW9iai5vcHRpb25zW29iai5zZWxlY3RlZEluZGV4XS5nZXRBdHRyaWJ1dGUoJ3VzcklEJylcOwogJCgnVUlEJykuaW5uZXJIVE1MPXNcOwogc2VsVHllTmFtZSgpXDsKfQpmdW5jdGlvbiBvcGVuV2luTG9nKHRoZVVSTCx3LGgpewp2YXIgVGZvcm0scmV0U3RyXDsKZXZhbCgiVGZvcm09J3dpZHRoPSIrdysiLGhlaWdodD0iK2grIixzY3JvbGxiYXJzPW5vLHJlc2l6YWJsZT1ubyciKVw7CiBpZih0aGVVUkwuaW5kZXhPZignUmVTZXRfUGFzc1dvcmQuYXNweCcpXD4tMSAmJiAnLDEwNDgyLDEwNDY2LDEyNDI1LDEwNDU5LCcuaW5kZXhPZignLDEyODQzLCcpIFw8PSAtMSApIHsKIHBhcmVudC5kb01vYmlsZVJlc2V0KClcOyB9IGVsc2Ugewpwb3A9d2luZG93Lm9wZW4odGhlVVJMLCd3aW5LUFQnLFRmb3JtKVw7IC8vcG9wLm1vdmVUbygwLDc1KVw7CmV2YWwoIlRmb3JtPSdkaWFsb2dXaWR0aDoiK3crInB4XDtkaWFsb2dIZWlnaHQ6IitoKyJweFw7c3RhdHVzOm5vXDtzY3JvbGxiYXJzPW5vXDtoZWxwOm5vJyIpXDsKcG9wLm1vdmVUbygoc2NyZWVuLndpZHRoLXcpLzIsKHNjcmVlbi5oZWlnaHQtaCkvMilcO2lmKHR5cGVvZihyZXRTdHIpIT0ndW5kZWZpbmVkJykgYWxlcnQocmV0U3RyKVw7Cn0KfQpmdW5jdGlvbiBzaG93TGF5KGRpdklkKXsKdmFyIG9iakRpdiA9IGV2YWwoZGl2SWQpXDsKaWYgKG9iakRpdi5zdHlsZS5kaXNwbGF5PT0ibm9uZSIpCntvYmpEaXYuc3R5bGUuZGlzcGxheT0iIlw7fQplbHNle29iakRpdi5zdHlsZS5kaXNwbGF5PSJub25lIlw7fQp9CmZ1bmN0aW9uIHNlbFR5ZU5hbWUoKXsKICAkKCd0eXBlTmFtZScpLnZhbHVlPSROKCdTZWxfVHlwZScpWzBdLm9wdGlvbnNbJE4oJ1NlbF9UeXBlJylbMF0uc2VsZWN0ZWRJbmRleF0udGV4dFw7Cn0Kd2luZG93Lm9ubG9hZD1mdW5jdGlvbigpewoJdmFyIHNQQz1NU0lFP3dpbmRvdy5uYXZpZ2F0b3IudXNlckFnZW50K3dpbmRvdy5uYXZpZ2F0b3IuY3B1Q2xhc3Mrd2luZG93Lm5hdmlnYXRvci5hcHBNaW5vclZlcnNpb24rJyBTTjpOVUxMJzp3aW5kb3cubmF2aWdhdG9yLnVzZXJBZ2VudCt3aW5kb3cubmF2aWdhdG9yLm9zY3B1K3dpbmRvdy5uYXZpZ2F0b3IuYXBwVmVyc2lvbisnIFNOOk5VTEwnXDsKdHJ5eyQoJ3BjSW5mbycpLnZhbHVlPXNQQ1w7fWNhdGNoKGVycil7fQp0cnl7JCgndHh0X2FzbWNkZWZzZGRzZCcpLmZvY3VzKClcO31jYXRjaChlcnIpe30KdHJ5eyQoJ3R5cGVOYW1lJykudmFsdWU9JE4oJ1NlbF9UeXBlJylbMF0ub3B0aW9uc1skTignU2VsX1R5cGUnKVswXS5zZWxlY3RlZEluZGV4XS50ZXh0XDt9Y2F0Y2goZXJyKXt9Cn0KZnVuY3Rpb24gb3BlbldpbkRpYWxvZyh1cmwsc2NyLHcsaCkKewp2YXIgVGZvcm1cOwpldmFsKCJUZm9ybT0nZGlhbG9nV2lkdGg6Iit3KyJweFw7ZGlhbG9nSGVpZ2h0OiIraCsicHhcO3N0YXR1czoiK3NjcisiXDtzY3JvbGxiYXJzPW5vXDtoZWxwOm5vJyIpXDsKd2luZG93LnNob3dNb2RhbERpYWxvZyh1cmwsMSxUZm9ybSlcOwp9CmZ1bmN0aW9uIG9wZW5XaW4odGhlVVJMKXsKdmFyIFRmb3JtLHcsaFw7CnRyeXsKCXc9d2luZG93LnNjcmVlbi53aWR0aC0xMFw7Cn1jYXRjaChlKXt9CnRyeXsKaD13aW5kb3cuc2NyZWVuLmhlaWdodC0zMFw7Cn1jYXRjaChlKXt9CnRyeXtldmFsKCJUZm9ybT0nd2lkdGg9Iit3KyIsaGVpZ2h0PSIraCsiLHNjcm9sbGJhcnM9bm8sc3RhdHVzPW5vLHJlc2l6YWJsZT15ZXMnIilcOwpwb3A9cGFyZW50LndpbmRvdy5vcGVuKHRoZVVSTCwnJyxUZm9ybSlcOwpwb3AubW92ZVRvKDAsMClcOwpwYXJlbnQub3BlbmVyPW51bGxcOwpwYXJlbnQuY2xvc2UoKVw7fWNhdGNoKGUpe30KfQpmdW5jdGlvbiBjaGFuZ2VWYWxpZGF0ZUNvZGUoT2JqKXsKdmFyIGR0ID0gbmV3IERhdGUoKVw7Ck9iai5zcmM9Ii4uL3N5cy9WYWxpZGF0ZUNvZGUuYXNweD90PSIrZHQuZ2V0TWlsbGlzZWNvbmRzKClcOwp9CmZ1bmN0aW9uIGNoa3B3ZChvYmopIHsgIGlmKG9iai52YWx1ZSE9JycpICB7ICAgIHZhciBzPW1kNShkb2N1bWVudC5hbGwudHh0X2FzbWNkZWZzZGRzZC52YWx1ZSttZDUob2JqLnZhbHVlKS5zdWJzdHJpbmcoMCwzMCkudG9VcHBlckNhc2UoKSsnMTI4NDMnKS5zdWJzdHJpbmcoMCwzMCkudG9VcHBlckNhc2UoKVw7ICAgZG9jdW1lbnQuYWxsLmRzZHNkc2RzZHhjeGRmZ2ZnLnZhbHVlPXNcO30gZWxzZSB7IGRvY3VtZW50LmFsbC5kc2RzZHNkc2R4Y3hkZmdmZy52YWx1ZT1vYmoudmFsdWVcO31jaGtMeHN0cihvYmoudmFsdWUpXDsgfSAgZnVuY3Rpb24gY2hreXptKG9iaikgeyAgaWYob2JqLnZhbHVlIT0nJykgeyAgIHZhciBzPW1kNShtZDUob2JqLnZhbHVlLnRvVXBwZXJDYXNlKCkpLnN1YnN0cmluZygwLDMwKS50b1VwcGVyQ2FzZSgpKycxMjg0MycpLnN1YnN0cmluZygwLDMwKS50b1VwcGVyQ2FzZSgpXDsgICBkb2N1bWVudC5hbGwuZmdmZ2dmZGd0eXV1eXl1dWNramcudmFsdWU9c1w7fSBlbHNlIHsgICAgZG9jdW1lbnQuYWxsLmZnZmdnZmRndHl1dXl5dXVja2pnLnZhbHVlPW9iai52YWx1ZS50b1VwcGVyQ2FzZSgpXDt9fSBmdW5jdGlvbiBjaGtMeHN0cihzdHIpIAogewogaWYgKHN0ciE9JycpIHsgdmFyIGFyciA9IHN0ci5zcGxpdCgnJylcOwpmb3IgKHZhciBpID0gMVw7IGkgXDwgYXJyLmxlbmd0aC0xXDsgaSsrKSB7CiAgIHZhciBmaXJzdEluZGV4ID0gYXJyW2ktMV0uY2hhckNvZGVBdCgpXDsKICAgdmFyIHNlY29uZEluZGV4ID0gYXJyW2ldLmNoYXJDb2RlQXQoKVw7CiAgIHZhciB0aGlyZEluZGV4ID0gYXJyW2krMV0uY2hhckNvZGVBdCgpXDsKICAgdGhpcmRJbmRleCAtIHNlY29uZEluZGV4ID09IDFcOwogICAgc2Vjb25kSW5kZXggLSBmaXJzdEluZGV4PT0xXDsKICAgaWYoKCh0aGlyZEluZGV4IC0gc2Vjb25kSW5kZXggPT0gMSkmJihzZWNvbmRJbmRleCAtIGZpcnN0SW5kZXg9PTEpICkgfHwgKHRoaXJkSW5kZXg9PXNlY29uZEluZGV4ICYmIHNlY29uZEluZGV4PT1maXJzdEluZGV4KSl7CiAgICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCd0eHRfbW1fbHhwZCcpLnZhbHVlPScxJ1w7IAogICB9CiB9CiB9Cn0KClw8L3NjcmlwdFw",
            "pcInfo": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 SN:NULL",
            "txt_mm_expression": "",
            "txt_mm_length": "",
            "txt_mm_userzh": "",
            "typeName": "(unable to decode value)",
            "dsdsdsdsdxcxdfgfg": "CD7155BE1BD820588D8F111A55C752",
            "fgfggfdgtyuuyyuuckjg": "AE89B082D386F238A850D238823EA5",
            "Sel_Type": "STU",
            "txt_asmcdefsddsd": "2018253328",
            "txt_pewerwedsdfsdff": "",
            "txt_psasas": "(unable to decode value)"
        }
        self.headers = {
            "Cookie": "name=value; name=value; ASP.NET_SessionId=jdy45miiakkz23v2jozu2455",
            "Host": "jwgl.wfust.edu.cn",
            "Origin": "http://jwgl.wfust.edu.cn",
            "Referer": "http://jwgl.wfust.edu.cn/_data/login_home.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.url = "http://jwgl.wfust.edu.cn/_data/login_home.aspx"

    def run(self):
        res = requests.post(url=self.url, headers=self.headers, data=self.data).content.decode("gb2312")
        print(res)


if __name__ == '__main__':
    login = Login()
    login.run()
