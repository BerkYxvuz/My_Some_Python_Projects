html_doc = """<html>
<head>
   <title>
   The Dormouse's story
  </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link3">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
  <p class="story">
    ...
   </p>
   <ul>
   <li>Berk</li>
   <li>Asrın</li>
   <li>Baran</li>
   </ul>
  </body>
 </html>  """

from bs4 import *

soup = BeautifulSoup(html_doc, 'html.parser')# değeri verdik , den sonra incelenme şeklini seçtik.
'''
result = soup.prettify() #console da düzenlenmiş şekilde görmemizi sağlayacak
result = soup.title # title kısmı gelir
result = soup.head # head kısmı gelir
result = soup.body # body kısmı gelir
result = soup.title.name # title'ın adı gelir
result = soup.title.string # title'ın yazısı gelir
result = soup.h1 #h1 in yazısı gelir fakat sadece ilk'i gelir
result = soup.find_all('h1')#[0] gibi yazarak sırasıyla da seçebilirsin # artık bütün hepsi gelecektir.
result = soup.div # ilk div gelir
result = soup.find_all('div')#[0] yine bu şekilde seçilebilir # tüm divler gelir
result = soup.find_all('div').ul #içindek ilk ul gelir
result = soup.find_all('div').ul.find_all('li') # bu kodla hepsi gelir
'''

# result = soup.div.findChildren() # bütün alt elemanları getirir
# result = soup.div.findNextSibling() # sonraki kaynağa atlayıp onu yazdırır
result = soup.find_all('a') # bütün a etiketlerini listeler for ile yazdırabilirsin.
print(result)