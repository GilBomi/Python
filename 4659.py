answer=[] #모든 입력받는 값들 저장하기 위해서
not_answer=[] #입력받는 값들중 조건에 안맞는 것들 저장하기 위해서
while(1): #반복문
    seperation = [] #seperation이 리스트임을 선언
    s=input("") #s에 문자열 입력받기
    if(s=="end"): #s=="end"이면
        break #탈출
    for i in s: #s만큼 반복
        seperation.append(i) #문자열을 모두 나눠서 seperation에 추가
    vowels=["a","e","i","o","u"] #모음 정의
    answer.append(s) #answer에 s 추가
    num_time=0 #num_time 0으로 초기화
    for i in vowels: #vowels만큼 반복
        if i not in seperation: #만약 i가 seperation에 없으면
            num_time+=1 #num_time 1만큼 증가
    if(num_time==5): #만약 num_time이 5이면
        not_answer.append(s) #not_answer에 s 추가
    else: #그 외
        for i in range(0,len(seperation)-2): #0~len(seperation)-3만큼 반복
            if(seperation[i] in vowels): #만약 seperation[i]가 모음이면
                if(seperation[i+1] in vowels): #seperation[i+1}이 모음이면
                    if(seperation[i+2] in vowels): #seperation[i+2}이 모음이면
                        not_answer.append(s) #not_answer에 s추가
            else: #seperation[i]가 자음이면
                if(seperation[i+1] not in vowels): #seperation[i+1]이 자음이면
                    if (seperation[i + 2] not in vowels):#seperation[i+2]이 자음이면
                        not_answer.append(s) #not_answer에 s 추가
        for i in range(0,len(seperation)-1): #0~len(seperation)-2만큼 반복
            if(seperation[i]==seperation[i+1]): #seperation[i]와 [i+1]이 같다면
                if(seperation[i]!="e" and seperation[i]!="o"): #seperation[i]가 "e"이고 "o"가 아니면,F and T
                    not_answer.append(s) #not_answer에 s추가
for i in answer: #answer만큼 반복
    if(i not in not_answer): #i가 not_answer에 없다면
        print("<%s> is acceptable." %i) #출력
    else: #not_answer에 있으면
        print("<%s> is not acceptable." %i) #출력