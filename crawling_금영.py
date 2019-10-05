from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

# html=urlopen("http://www.ikaraoke.kr/isong/search_newsong.asp?page=1&s_date=201908")

html = urlopen("http://www.ikaraoke.kr/isong/search_musictitle.asp?page=2&sch_sel=0&sch_txt=Beyonce")
bsObject = BeautifulSoup(html, "html.parser")
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=2&s_date=201908
# http://www.ikaraoke.kr/isong/search_newsong.asp?page=3&s_date=201908
title1 = []
num1 = []
singer1 = []
# 가수 출력
for cover in bsObject.find_all('td', {'class', 'tit pl8'}):
    arr = str(cover).split('>')
    singer = str(arr[2]).split('<')[0].split(' ')[0]
    singer1.append(singer)

#  제목 출력(띄어쓰기 없앰)
for cover in bsObject.find_all('a', {'class', 'b'}):
    title = cover.get('title')
    # arr = str(title).split(' ')
    # title = ''
    # for i in arr:
    #     title += i
    title1.append(title)

# title1.insert(5, str('asada'))
# title1.insert(11, str('sfdfsf'))

# 곡 번호 출력
# for cover in bsObject.find_all('td', {'class', 'ac'}):
#     arr = cover.find_all('input')
#     for j in arr:
#         if not len(j):
#             num1.append(j.get('value'))
for cover in bsObject.find_all('em'):
    num1.append(str(cover).split('>')[1].split('<')[0])
# #
num1.remove(str(61242))
# num1.remove(str(44254))
# num1.remove(str(43279))

conn = pymysql.connect(host='localhost', user='root', password='test123', db='songs', port=3306)
curs = conn.cursor()

for i in range(len(num1)):
    print(num1[i] + " " + title1[i])

# # # #
for i in range(len(num1)):
    curs = conn.cursor()
    sql = "insert into ky(num,name,singer) values(%s,%s,'Beyonce');"
    curs.execute(sql,(num1[i],title1[i]))
    conn.commit()



# conn.close()
