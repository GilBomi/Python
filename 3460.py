n=int(input()) #몇번 테스트 할건지 입력
for i in range(0,n): #그 수만큼 반복해서
    k=int(input()) # 입력받기
    l=[] #l이 리스트임을 선언
    m="" #m이 문자열임을 선언
    while(1): #무한반복문
        l.append(k%2) #l에 k를 2로 나눈 나머지 저장
        k=k//2 #k에 2로 나눈 몫 저장
        if(k==0): #만약 몫이 0이면
            break #탈출
    for i in range(0,len(l)): #l의 크기만큼 반복
        if(l[i]==1): #만약 l[i]가 1이면
            m+=str(i)+" " #m에 더하기
    print(m) #출력
