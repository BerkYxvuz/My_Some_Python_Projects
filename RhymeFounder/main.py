from bs4 import BeautifulSoup
import requests, os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Dosya adını belirleyin
dosya_adı = 'lyrics.txt'

# Dosya yolunu oluşturun
dosya_yolu = os.path.join(current_dir, dosya_adı)

url = 'https://genius.com/Sehinsah-and-cotard-galvanize-lyrics'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

lyric_divs = soup.find_all('div', class_ = 'Lyrics__Container-sc-1ynbvzw-5 Dzxov')

lyrics_list = []

for div in lyric_divs:
    div = list(div)
    for x in div:
        lyrics_list.append(x.text)
with open(dosya_yolu, 'w', encoding='utf-8') as file:
    for line in lyrics_list:
        file.write(str(line) + '\n')
    
def is_rhyme(word1, word2):
    min_length = min(len(word1), len(word2))
    for i in range(min_length, 0, -1):
        if word1[-i:] == '(' or word1[-i:] == ')' or word2[-i:] == '(' or word2[-i:] == ')':
            return False
        if word1[-i:] != word2[-i:]:
            return False
    return True

with open('lyrics.txt', 'r', encoding='utf-8') as file:
    lyrics = file.read().split()  # Şarkı sözlerini tüm kelimelerine ayır
    for i in range(len(lyrics)):
        word1 = lyrics[i]
        for j in range(i+1, len(lyrics)):
            word2 = lyrics[j]
            if is_rhyme(word1, word2):
                print(word1, "ve", word2, "rhyme.")
                i += 2
            else:
                i += 2