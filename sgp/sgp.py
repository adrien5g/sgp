from sgp import utils

import requests

class Sgp:
    def __init__(self):
        self.config = utils.read_config(required=True)
        self.token = ''


    def login(self):
        self.token = utils.get_access_token_file()
        if not self.token:
            request = requests.post('https://api.sgp.al.senai.br/oauth/token', json=self.config['credentials'])
            if not request.status_code == 200:
                quit('Login failed')
            self.token = request.json()['access_token']
            utils.gen_access_token_file(self.token)
        return True


    def request(self, url, header = {}, method='get'):
        request = requests.get if method == 'get' else requests.post
        header['authorization'] = f'Bearer {self.token}' if self.token != '' else quit('Please, run sgp.login()')
        response = request(url, headers=header)
        return response


    def get_cards(self):
        response = self.request('https://api.sgp.al.senai.br/api/service/search/Todos/Eu')
        utils.output_to_file(response.json())
        return response.json()