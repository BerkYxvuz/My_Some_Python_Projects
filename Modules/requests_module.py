import requests
import json

data = requests.get("https://www.instagram.com/berkyxvuz/")
data = data.text
print(data)