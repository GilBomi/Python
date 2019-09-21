import os
a=input("이동할 디렉토리:")
b=input("생성할 디렉토리:")
os.chdir("C:\\"+a) #사용자가 입력한 디렉토리로 이동
os.makedirs(a+"\\"+b) # 사용자가 입력한 이름의 새 디렉토리 만들기
os.makedirs(a+"\\"+"test") #test디렉토리 만들기
os.getcwd() #현재 디렉토리 출력
for name in os.listdir(a): #현재 디렉토리 아래에 있는 디렉토리 목록 출력
    print(name)
os.removedirs(a+"\\"+"test") #test 디렉토리 삭제
os.removedirs(a+"\\"+b) #생성한 디렉토리 삭제
for name in os.listdir(a): # 생성한 디렉토리의 부모 디렉토리 목록을 출력
    print(name)





 