n=int(input()) #몇개 입력받을지 입력
c_name=[] #c_name이 리스트임을 선언
final_answer=[] # final_answer가 리스트임을 선언
for i in range(0,n): # i가 0부터 n-1까지 반복
    c=input() #c에 알파벳 입력
    c_name.append(c) #c_name에 c를 추가함
    answer=[] #answer가 리스트임을 선언
    final="" #final이 문자열 임을 선언
    for j in c_name[i]: #c_name[i]만큼 반복
        if(ord(j)==90): #ord는 문자열을 아스키코드 숫자로 바꿔줌,Z일때
            answer.append(chr(65)) #answer에 65를 아스키코드로 바꾼 A 추가
        else: # 그 외
            answer.append(chr(ord(j)+1)) #아스키코드 숫자에 1을 더한 값을 가진 아스키코드를 추가
    for i in answer: #answer만큼 반복
        final+=i #final에 i를 계속 더해서 문장 만들기
    final_answer.append(final) #final_answer에 final추가
for i in range(0,n): #0부터 n-1까지 반복
    print("String #%d" %(i+1)) #출력
    print(final_answer[i]+"\n") #출력

