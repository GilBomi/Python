correct_number_list=[] #correct_number_list를 리스트로 정의
sum=0 #합을 0으로 정의
print("lab0_2: 길보미") #이름 출력
print("10개의 정수를 입력하세요:") #출력문 출력
for i in range(0,10): #i를 0~9까지 반복
    number=int(input()) #number에 정수입력받기
    if number>=1 and number<=100: #number가 1이상 100이하면
        correct_number_list.append(number) #그 값을 correct_number_list에 추가하기
for i in correct_number_list: #i가 correct_number_list만큼 돌면서
    sum+=i #sum에 i를 더하기
print("1~100 범위 값들의 합=",sum) #합 출력하기