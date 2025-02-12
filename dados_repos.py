import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
class DadosRepositorios:
    def __init__(self, owner):
        self.access_token = os.getenv("API_TOKEN")
        self.owner = owner
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
           'X-GitHub-Api-Version': '2022-11-28'}
        self.api_url = 'https://api.github.com'
    
    repos_list = []
    repos_name = []
    repos_language = []
    data = None

    def listRepo(self):
        page = 1
        while True:
            url_page = f'{self.api_url}/users/{self.owner}/repos?page={page}'
            response = requests.get(url_page, headers=self.headers)
            self.repos_list.append(response.json())
            if len(response.json())==0:
                break
            page += 1


    def nameRepo(self):
        if len(self.repos_list) == 0:
            self.listRepo()
        for sub_page in self.repos_list:
            for repo in sub_page:
                self.repos_name.append(repo['name'])
    
    def languageRepo(self):
        if len(self.repos_list) == 0:
            self.listRepo()
        for sub_page in self.repos_list:
            for repo in sub_page:
                self.repos_language.append(repo['language'])

    def checkRepos(self):
        checked = False
        self.languageRepo()
        self.nameRepo()
        if self.repos_language and self.repos_name:
            checked = True
        return checked


    def createData(self):
        if self.checkRepos():
            self.data = pd.DataFrame()
            self.data['name_repository'] = self.repos_name
            self.data['language_repository'] = self.repos_language
        else:
            print('Usuário não encontrado ou não existe repositórios para serem listados')

    def createFile(self):
        if isinstance(self.data, pd.DataFrame):
            return self.data.to_csv(f'{self.owner}.csv')
        else:
            raise('O arquivo DataFrame não foi criado, tente chamar a função "createData" primeiro.')