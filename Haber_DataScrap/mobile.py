import kivy
from bs4 import *
import time, requests, telegram, telebot, asyncio, os
haberler = []
def VeriCek():
    global haberler
    url = "https://www.haberler.com/son-dakika/"

    get_url = requests.get(url).content

    soup = BeautifulSoup(get_url, "html.parser")

    filtre = soup.find("div", {"class": "hbInRow boxStyle boxRadius hbLastNews"}).find("div", {"class": "hblnBox"})
    resim = filtre.find("div", {"class": "hblnImage"}).select_one('img')['src']
    resim = requests.get(resim)
    file = resim.content
    title = filtre.span.text
    saat = filtre.find().text
    return [file, saat, title]


bot_token = "6013324787:AAEfE0oj-utHI6Irgv4R1kBrzfO47VCHr0w"

# Kanal kimliğini buraya ekleyin
channel_id = "@sondak1kahaberler"

# Telegram botunu başlat
bot = telegram.Bot(token=bot_token)

# Kanala göndermek istediğiniz mesaj
message = "Merhaba, kanal!"
file = ""
async def main():
    await bot.send_photo(chat_id=channel_id, photo=file, caption=f'{message}')

class MyApp():
    def build(self):
        screen = Screen()
MyApp().run()
while True:
    try:
        text = VeriCek()
        yazi = str(text[1] + ' ' + text[2])
        file = text[0]
        if yazi in haberler:
            time.sleep(6)
            pass
        else:
            message = yazi
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            haberler.append(message)

    except:
        pass
