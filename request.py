import requests


class Api_Request():

    def __init__(self):
        self.api_key = "9d9e18b102dec353e319318f6b37d47a773052aa"
        self.secret_key = "6248cf811947f519a87276bccf47375a24292fbf"
        self.phone_base_url = "https://cleaner.dadata.ru/api/v1/clean"
        self.inn_base_url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById"
        self.headers = {"Content-Type": "application/json",
                   "Authorization": f"Token {self.api_key}",
                   "X-Secret": f"{self.secret_key}"}


    def phone_request(self, phone):
        endpoint = "/phone"
        body = phone
        response = requests.post(self.phone_base_url+endpoint, headers=self.headers, data=body).json()

        if response is not None:
            return response[0]
        else:
            raise ValueError


    def inn_request(self, inn):
        endpoint = "/party"
        body = inn

        response = requests.post(self.inn_base_url+endpoint, headers=self.headers, data=body).json()

        if response is not None:
            return response
        else:
            raise ValueError