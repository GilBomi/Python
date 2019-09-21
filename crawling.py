from urllib.request import urlopen
from bs4 import BeautifulSoup
#html=urlopen("http://www.ikaraoke.kr/isong/search_newsong.asp?page=1&s_date=201908")

html=urlopen("http://www.tjmedia.co.kr/tjsong/song_monthNew.asp")
bsObject=BeautifulSoup(html,"html.parser")
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=2&s_date=201908
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=3&s_date=201908
book_page_urls = []
for cover in bsObject.find_all('', {'class','left'}):
    #link = cover.get('title')
    book_page_urls.append(cover)

for i in book_page_urls:
    print(i)

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
#
#     print(index+1, title, author, image, url, originalPrice, salePrice)
#
# print(bsObject)


#import pymysql
#db = pymysql.connect(host='localhost',
#                    port=3306,
#
 #                    user='root',
#
 #                    passwd='test123',
#
#                     db='test_table',
#
 #                    charset='utf8')
#cursor = db.cursor()
#sql = """INSERT INTO test_table(num, name)
#         VALUES('test_num', 'test_name');"""
#cursor.execute(sql)
#db.commit()
