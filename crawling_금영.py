from urllib.request import urlopen
from bs4 import BeautifulSoup
#html=urlopen("http://www.ikaraoke.kr/isong/search_newsong.asp?page=1&s_date=201908")

html=urlopen("https://www.tjmedia.co.kr/tjsong/song_monthPopular.asp")
bsObject=BeautifulSoup(html,"html.parser")
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=2&s_date=201908
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=3&s_date=201908
book_page_urls = []
#곡 제목 출력
# for cover in bsObject.find_all('', {'class','left'}):
#     #link = cover.get('title')
#     book_page_urls.append(cover)
#
# for i in book_page_urls:
#     print(i)

for cover in bsObject.find_all('td'):
    #link = cover.get('title')
    book_page_urls.append(cover)

for i in book_page_urls:
    print(i)


