import requests
import shutil
import getcode


class getVerificationCode:

    def __init__(self,url,headers):
        self.url = url
        self.headers = headers

    def save_verification_code_to_local(self):
        session = requests.Session()
        resp = session.get(self.url,headers=self.headers,stream=True)
        if resp.status_code == 200:
            with open("VerificationCode.png",'wb') as f:
                shutil.copyfileobj(resp.raw,f)
        else:
            raise Exception("status_code是{}".format(resp.status_code))


    def get_verification_code(self):
        getVerificationCode.save_verification_code_to_local(self)
        rc = getcode.RClient('若快平台用户名', '若快平台用户密码', '若快平台开发者加的项目对应id', '若快平台开发者加的项目对应key')
        im = open(r'VerificationCode.png', 'rb').read()
        print (rc.create(im, 3040))
        return rc.create(im, 3040)



if __name__ == '__main__':
    url = "你们获取验证码的链接"
    headers = {
        'Connection': 'Keep-Alive',
        'Expect': '100-continue',
        'User-Agent': '你的用户信息'
    }
    gc = getVerificationCode(url,headers)
    # gc.save_verification_code_to_local()
    gc.get_verification_code()
