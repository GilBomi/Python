k=1000 #k=1000
while(k<=9999): #k<=9999일때만 반복
    s=str(k) #s에 k를 문자열로 저장
    n1=0 #n1이 숫자형임을 정의
    for i in range(0,len(s)): #0부터 len(s)만큼 반복
        n1+=int(s[i]) #n1에 k 문자열 각 자리수 더하기
    l=[] #l이 리스트임을 정의
    n2=0 #n2가 숫자형임을 정의
    n3=0 #n3가 숫자형임을 정의
    k1=k #k1에 k 저장
    k2=k #k2에 k 저장
    while(1): #무한반복문
        l.append(k1%12) #l에 k1을 12로 나눈 나머지 저장
        k1=k1//12 #k1에 k1을 12로 나눈 몫 저장
        if(k1==0): #만약 몫이 0이면
            break #탈출
    for i in range(0,len(l)): #len(l)만큼 반복
        n2+=l[i] #n2에 각 자리 수 더하기
    l=[] #l초기화
    while (1): #무한반복문
        l.append(k2 % 16) #l에 k2을 16로 나눈 나머지 저장
        k2 = k2 // 16 #k2에 k2을 16로 나눈 몫 저장
        if (k2 == 0): #만약 몫이 0이면
            break #탈출
    for i in range(0, len(l)): #len(l)만큼 반복
        n3 += l[i] #n3에 각 자리 수 더하기
    if(n1==n2 and n2==n3): #n1==n2==n3이면
        print(k) #출력
    k+=1 #k 증가
