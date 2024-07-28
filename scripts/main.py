import os
from pynubank import Nubank
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

os.chdir("M:\\Documentos\\Nubank")

user = {
    "cpf" : os.getenv("CPF"),
    "passwd" : os.getenv("PASSWD"),
    "cert_path" : os.getenv("CERT_PATH")
}

nu = Nubank()

nu.authenticate_with_cert(user["cpf"], user["passwd"], "./cert.p12")
print(nu.get_account_balance())
#print(user["cert_path"])