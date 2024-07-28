import os
from pynubank import Nubank
from dotenv import load_dotenv


load_dotenv()

user = {
    "cpf" : os.getenv("CPF"),
    "passwd" : os.getenv("PASSWD"),
    "cert_path" : os.getenv("CERT_PATH")
}

nu = Nubank()

nu.authenticate_with_cert(user["cpf"], user["passwd"], user["cert_path"])
print(nu.get_account_balance())