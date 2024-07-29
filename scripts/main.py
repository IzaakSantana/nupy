import os
from pynubank import Nubank
from dotenv import load_dotenv

load_dotenv()

class UserData:
    def __init__(self, cpf, passwd, cert_path):
        self._cpf = cpf
        self._passwd = passwd
        self._cert_path = cert_path


    @property
    def cpf(self):
        return self._cpf
    

    @property
    def passwd(self):
        return self._passwd
    

    @property
    def cert_path(self):
        return self._cert_path
    

user = UserData(
    cpf=os.getenv("CPF"),
    passwd=os.getenv("PASSWD"),
    cert_path=os.getenv("CERT_PATH")
)

nu = Nubank()

nu.authenticate_with_cert(user.cpf, user.passwd, user.cert_path)
print(nu.get_bills())
