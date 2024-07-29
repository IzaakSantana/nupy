import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Pluggy:
    def __init__(self, client_id, client_secret):
        self._url = "https://api.pluggy.ai"
        self._headers = {"accept": "application/jason", "content-type": "application/jason"}
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

        self._api_key = requests.post(self._url + endpoint, headers=self._headers, json=payload).text

         

pluggy = Pluggy(getenv("CLIENT_ID"), getenv("CLIENT_SECRET"))
pluggy.create_api_key()
print(pluggy.api_key)
