import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

music_info = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0

for music in music_info:
    title_el = music.select('td.info >a')
    singer_el = music.select('a.artist.ellipsis')
    if len(title_el) > 0:
        rank += 1
        title = title_el[0].text
        singer = singer_el[0].text

        print(rank, title.strip(), '/', singer)
