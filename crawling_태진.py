from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
#html=urlopen("http://www.tjmedia.co.kr/tjsong/song_search_list.asp")

html = urlopen("https://www.tjmedia.co.kr/tjsong/song_search_list.asp?strType=2&strText=beyonce&strCond=0&searchOrderType=&searchOrderItem=&intPage=2")
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

# del title[8]
# del title[8]

conn = pymysql.connect(host='localhost', user='root', password='test123', db='songs', port=3306)
curs = conn.cursor()

for i in range(len(title)):
    print(number[i]+" "+title[i])
#
# # #
for i in range(len(title)):
    curs = conn.cursor()
    sql = "insert into tj(num,name,singer) values(%s,%s,'Beyonce');"
    curs.execute(sql,(number[i],title[i]))
    conn.commit()

