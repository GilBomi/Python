html="""
<html>
    <head>
        <title>test web</title>
    </head>
    <body>
    <p align="center">text contents</p>
    <img src="C:\python\R1280x0.jpg" width="500" height="300">
    </body>
</html>
"""
from bs4 import BeautifulSoup
bs=BeautifulSoup(html)
print(bs.prettify())
print(bs.find("title"))