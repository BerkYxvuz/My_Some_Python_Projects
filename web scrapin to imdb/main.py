import requests, json
from bs4 import *

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

content = requests.get(url).content # html içeriğini böylece çektik

soup = BeautifulSoup(content, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).findAll("tr") #limit= ile kaç tane tr alacağımızı belirleyebilriz
                                                                # süslü parantez ile alacağımız divin classını belli ettik
                                                              # ve findAll ile tr lere filtereledik.
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text # filtreleri ekleyerek aradığımızı aldık
    since = tr.find("span",{"class":"secondaryInfo"}).text
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).text
    print(f"{title}\nSince: {since} \nRating: {rating}")