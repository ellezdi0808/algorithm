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
            with open("yanzhengma.png",'wb') as f:
                shutil.copyfileobj(resp.raw,f)
        else:
            raise Exception("status_code是{}".format(resp.status_code))


    def get_verification_code(self):
        getVerificationCode.save_verification_code_to_local(self)
        rc = getcode.RClient('wualisa', '13681656881weu', '86839', '9c25b878b71544f681256c3819dacd1d')
        im = open(r'yanzhengma.png', 'rb').read()
        print (rc.create(im, 3040))
        return rc.create(im, 3040)



if __name__ == '__main__':
    url = "http://webapi.ecloud.shfc999.com/tool/get_code/2132313"
    headers = {
        'Connection': 'Keep-Alive',
        'Expect': '100-continue',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    gc = getVerificationCode(url,headers)
    # gc.save_verification_code_to_local()
    gc.get_verification_code()