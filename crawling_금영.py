from urllib.request import urlopen
from bs4 import BeautifulSoup

# html=urlopen("http://www.ikaraoke.kr/isong/search_newsong.asp?page=1&s_date=201908")

html = urlopen("http://www.ikaraoke.kr/isong/hit_song.asp")
bsObject = BeautifulSoup(html, "html.parser")
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=2&s_date=201908
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=3&s_date=201908
book_page_urls = []

# 제목 출력(띄어쓰기 없앰)
# for cover in bsObject.find_all('a', {'class','b'}):
#     title = cover.get('title')
#     arr = str(title).split(' ')
#     title=''
#     for i in arr:
#         title += i
#     book_page_urls.append(title)
#
# for i in book_page_urls:
#     print(i)

#가수 출력
# for cover in bsObject.find_all('td', {'class', 'tit pl8'}):
#     arr = str(cover).split('>')
#     singer = str(arr[2]).split('<')[0].split(' ')[0]
#     book_page_urls.append(singer)
#
# for i in book_page_urls:
#     print(i)

#곡 번호 출력
# for cover in bsObject.find_all('td', {'class', 'ac'}):
#     arr = cover.find_all('input')
#     for j in arr:
#         if not len(j):
#             book_page_urls.append(j.get('value'))
# for i in book_page_urls:
#     print(i)






# 메타 정보로부터 요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.
# for index, book_page_url in enumerate(book_page_urls):
#     html = urlopen(book_page_url)
#     bsObject = BeautifulSoup(html, "html.parser")
#     title = bsObject.find('meta', {'property':'rb:itemName'}).get('content')
#     author = bsObject.select('span.name a')[0].text
#     image = bsObject.find('meta', {'property':'rb:itemImage'}).get('content')
#     url = bsObject.find('meta', {'property':'rb:itemUrl'}).get('content')
#     originalPrice = bsObject.find('meta', {'property': 'rb:originalPrice'}).get('content')
#     salePrice = bsObject.find('meta', {'property':'rb:salePrice'}).get('content')
#     print(index+1, title, author, image, url, originalPrice, salePrice)
# print(bsObject)


# import pymysql
# db = pymysql.connect(host='localhost',
#                    port=3306,
#
#                    user='root',
#
#                    passwd='test123',
#
#                     db='test_table',
#
#                    charset='utf8')
# cursor = db.cursor()
# sql = """INSERT INTO test_table(num, name)
#         VALUES('test_num', 'test_name');"""
# cursor.execute(sql)
# db.commit()
