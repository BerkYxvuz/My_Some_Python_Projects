import json
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "a3ba5f63a01651642bbf0a8d088cc97b"
    def getPops(self):
        popmovs_url = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return popmovs_url.json()
    def getInVisions(self):
        InVisMovs_url = requests.get(f"{self.api_url}movie/now_playing?api_key={self.api_key}")
        return InVisMovs_url.json()
    def getTopRated(self):
        TopRatedMovs = requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}")
        return  TopRatedMovs.json()

machine = theMovieDb()

while True:
    secim = input("1- Popuüler Filmler: \n2- Vizyon'daki filmler: \n3- En Fazla Puan Alan Filmler: ")
    if secim == '1':
        result = machine.getPops()
        for i in result['results']:
            print(i['title'])
    if secim == '2':
        request = machine.getInVisions()
        for i in request['results']:
            print(i['title'])
    if secim == '3':
        request = machine.getTopRated()
        for i in request['results']:
            print(f"{i['title']} | imdb: {i['vote_average']}")
    else:
        break