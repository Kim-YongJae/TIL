from AbstractSMTPConnetor import *
class DaumConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        print('Daum SMTP 서버에 연결되었습니다.')