from bs4 import BeautifulSoup
import requests
import os
import random
from colorama import init, Fore

# Colorama'nın başlatılması
init(autoreset=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
dosya_adı = 'lyrics.txt'
dosya_yolu = os.path.join(current_dir, dosya_adı)

url = 'https://genius.com/Sehinsah-and-cotard-galvanize-lyrics'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

lyric_divs = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-5 Dzxov')

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

with open(dosya_yolu, 'r', encoding='utf-8') as file:
    lyrics = file.read().split()

rhyme_colors = {}  # Rhyme olan kelimelerin renklerini saklamak için bir sözlük oluştur
highlighted_lines = []  # Renklendirilmiş satırları saklamak için bir liste oluştur

for line in lyrics:
    words = line.split()
    highlighted_words = []

    for word in words:
        if word not in rhyme_colors:
            rhyme_colors[word] = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

        if highlighted_words and len(highlighted_words) > 0:
            last_word = highlighted_words[-1]
            if is_rhyme(word, last_word):
                color_code = rhyme_colors[word]
                highlighted_words.append(f'{color_code}{word}')
            else:
                highlighted_words.append(word)
        else:
            highlighted_words.append(word)

    highlighted_line = ' '.join(highlighted_words)
    highlighted_lines.append(highlighted_line)

# Renklendirilmiş satırları yazdır
for line in highlighted_lines:
    print(line)
