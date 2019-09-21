l=[] #l이 리스트임을 선언
while(1): #반복문
    n=int(input()) #n에 정수 입력받기
    if(n==0): #만약 n이 0이면
        break #탈출
    l.append(n) #l에 n 저장하기
for i in l: #l만큼 반복
    k=str(i) #k에 i를 문자열로 저장
    a=0 #a=0
    while(1): #무한반복문
        a=0 #a=0
        for j in k: #k만큼 반복
            a+=int(j) #a에 j를 정수형으로 바꾼 값 계속 더하기
        if(a<10): #만약 a<10이면
            break #탈출
        else: #그 외
            k=str(a) #k에 a를 문자열로 저장
    print(a) #출력





