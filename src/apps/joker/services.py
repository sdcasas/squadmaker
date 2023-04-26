import random

import requests

from apps.joker.models import Joker


class JokerService:

    def __init__(self, type):
        # api url
        self.URLS = {
            'chuck': "https://api.chucknorris.io/jokes/random",
            'dad': "https://icanhazdadjoke.com/"
        }
        self.METHODS = {
            'chuck': self.get_value_chuck,
            'dad': self.get_value_dad
        }
        self.TYPE = type

    def __validate_url(self, url):
        try:
            response = requests.get(url, timeout=3)
        except Exception as e:
            print('error connection')

    # "/jokes/search?query={query}"
    # "/jokes/random?category={category}"
    def get_chuck_categories(self):
        try:
            url = self.URL_CHUCK + "jokes/categories"
            response = requests.get(url, timeout=3)
            return response.json()
        except Exception as e:
            print(e)
            return []

    def get_value(self):
        get_value = self.METHODS.get(self.TYPE) if self.TYPE else random.choice(list(self.METHODS.values()))
        try:
            return get_value()
        except Exception as e:
            return None

    def get_value_chuck(self):
        url = "https://api.chucknorris.io/jokes/random"
        try:
            response = requests.get(url, timeout=3)
            result = response.json()
            joker, _ = Joker.objects.get_or_create(
                value=result.get("value"),
                joker_id=result.get('id'),
                joker_type='CHUCK'
            )
            return joker
        except Exception as e:
            return None

    def get_value_dad(self):
        url = "https://icanhazdadjoke.com/"
        try:
            response = requests.get(url, headers={"Accept": "application/json"}, timeout=3)
            result = response.json()
            joker, _ = Joker.objects.get_or_create(
                value = result.get("joke"),
                joker_id = result.get('id'),
                joker_type = 'DAD'
            )
            return joker
        except Exception as e:
            return None
