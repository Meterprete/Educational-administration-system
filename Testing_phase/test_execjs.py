import execjs
import os


class GET_EXECJS:
    def run(self):
        os.environ["EXECJS_RUNTIME"] = "PhantomJS"
        # print(execjs.get().name)
        with open("md5.js", "r") as f:
            jsData = f.read()

        # res = execjs.compile(jsData).call('ChkVal')
        try:
            res = execjs.compile(jsData).call("ChkVal")
            return res
        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_execjs = GET_EXECJS()
    get_execjs.run()
