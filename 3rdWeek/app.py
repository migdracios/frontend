from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbjungle                    


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:

    rank = music.select_one('td.number')
    title = music.select_one('td.info > a.title.ellipsis')
    artist = music.select_one('td.info > a.artist.ellipsis')

    if rank is not None:
        rank = rank.text[0:2]
        title = title.text.strip()
        artist = artist.text.strip()
        print(rank, title, artist)
        
