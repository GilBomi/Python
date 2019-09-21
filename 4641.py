answer_list=[] #answer_list가 리스트임을 선언
while(1): #반복문
    n=input("") #n에 숫자들 입력받기
    if(n=="-1"): #만약 n이 "-1"이면
        break #탈출
    n=n.split() #n을 띄어쓰기로 나눈 값들을 리스트로 저장
    n.remove("0") #n의 요소 중 "0" 없애기
    answer=0 #answer=0으로 초기화
    for i in n: #n만큼 반복
        if(str(int(i)*2) in n): #i를 정수로 바꾼 값*2를 문자열로 바꾼게 n에 있으면
            answer+=1 #answer에 1 더하기
    answer_list.append(answer) #answer_list에 answer추가하기
for i in answer_list: #answer_list만큼 반복
    print(i) #출력