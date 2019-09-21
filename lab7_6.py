import os

p="C:\\python\\201732002"

def recursion(k): # recursion함수
    if(os.path.isfile(k)==True): # 경로 k에 있는 것이 파일일때
        os.remove(k) #파일삭제

    if (os.path.exists(k) == False):
        os.removedirs(k)
    else: #경로 k에 있는 것이 파일이 아닐때
        if (os.path.exists(k) == False):
            os.removedirs(k)
        for a in os.listdir(k): #경로 k에 있는 파일과 폴더 목록을 리스트로 만들기
            recursion(k+"\\"+a) #recursion 함수에 (k+"\\"+a)넣기

for i in os.listdir(p): #경로 p에 있는 파일과 폴더 목록을 리스트로 만들기
    recursion(p+"\\"+i) #recursion함수에 (p+"\\"+i)넣기
