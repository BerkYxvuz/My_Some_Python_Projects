import requests
import json
class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
    def getUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    def getRepos(self,username):
        response = requests.get(self.api_url + '/users/' + username + '/repos/')
        return response.json()
    def createRepos(self, name):
        response = requests.post(self.api_url + '/user/repos?access_token=' + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
github = Github()
while True:
    print('Menü'.center(50, '='))
    secim = input('1- Find User\n2- Get Repository\n3- Create Repository\n4- Exit\nSeçim: ')
    if secim == '4':
        break
    else:
        if secim == '1':
            username = str(input('Kullanıcı Adını Giriniz: '))
            result = github.getUser(username=username)
            print(result)
            print(f'name: {result["login"]} \npublic repos: {result["public_repos"]} \nfollowers: {result["followers"]}')
        if secim == '2':
            username = str(input('Kullanıcı Adını Giriniz: '))
            result = github.getRepos(username=username)
            for i in result:
                print(i)
        if secim == '3':
            name = input("Repository'nin ismi: ")
            result = github.createRepos(name=name)
            print(result)