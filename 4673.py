n=1 #n은 1부터 시작
l=[] #l이 리스트임을 선언
while(n<=10000): #n<=10000이면 반복
    p = str(n) #p에 n 문자열로 바꿔서 저장
    sum=n #sum에 n 저장
    for i in p: #문자열 p만큼 반복
        sum+=int(i) #sum에 문자 각 자리를 정수로 바꿔서 더하기
    l.append(sum) #l에 sum값을 넣기
    n+=1 #n을 1만큼 증가
l=set(l) #l의 요소 중 중복되는것을 없애기 위해 set 사용
for i in range(1,10001): #1부터 10000까지 반복
    if(i not in l): #l에 i가 없으면
        print(i) #i 출력

