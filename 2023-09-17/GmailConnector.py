from AbstractSMTPConnetor import *
class GmailConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        print('GMAIL SMTP 서버에 연결되었습니다.')