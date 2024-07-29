import requests
import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Pluggy:
    def __init__(self, client_id, client_secret):
        self._url = "https://api.pluggy.ai"
        self._headers = {"accept": "application/json", "content-type": "application/json"}
        self._connector_id = 200 # MeuPluggy
        self._api_key = None
        self._client_id = client_id
        self._client_secret = client_secret


    @property
    def api_key(self):
        return self._api_key


    @property
    def url(self):
        return self._url


    def create_api_key(self):
        endpoint = "/auth"

        payload = {
            "clientId": self._client_id,
            "clientSecret": self._client_secret
        }

        response = requests.post(self._url + endpoint, json=payload, headers=self._headers)

        if response.status_code == 200:
            self._api_key = response.json().get('apiKey')
        else:
            print(f"Erro {response.status_code}: {response.text}")


pluggy = Pluggy(getenv("CLIENT_ID"), getenv("CLIENT_SECRET"))
pluggy.create_api_key()

