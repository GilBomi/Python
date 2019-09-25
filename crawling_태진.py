from urllib.request import urlopen
from bs4 import BeautifulSoup
#html=urlopen("http://www.tjmedia.co.kr/tjsong/song_search_list.asp")

html = urlopen("http://www.tjmedia.co.kr/tjsong/song_search_list.asp?strType=2&strText=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8&strCond=0&searchOrderItem=&searchOrderType=")
bsObject = BeautifulSoup(html,"html.parser")
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=2&s_date=201908
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=3&s_date=201908
book_page_urls = []

#곡 제목 출력(영어제목만 띄어쓰기 되어있고 한글은 안되어있음)
# for cover in bsObject.find_all('td', {'class', 'left'}):
#     arr = str(cover).split('>')[1]
#     title = str(arr).split('<')[0]
#     book_page_urls.append(title)
#
# for i in book_page_urls:
#     print(i)

#가수 출력
data = enumerate(bsObject.find_all('td'))
number = []
title = []
singer = []
for i, cover in data:
    #link = cover.get('title')
    if i < 44:
        continue
    arr = str(cover).split('>')[1]
    arr = str(arr).split('<')[0]
    if len(arr) == 0:
        continue
    if ((i-44) % 6) == 0:
        number.append(arr)
    if ((i-45) % 6) == 0:
        title.append(arr)
    if ((i-46) % 6) == 0:
        singer.append(arr)

for i in title:
    print(i)

#
