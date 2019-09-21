import os # os모듈 사용

if(os.path.isfile(os.getcwd()+"\\"+"score.txt")==False): #만약 현재 작업 디렉토리에 score.txt가 없으면
    print("파일이 존재하지 않습니다.") #출력
else: #score.txt가 존재하면
    f=open("score.txt","r") #score.txt를 읽어오기
    n=0 #학생 수=0
    all=0 #전체 점수=0
    korean=0 #전체 국어 점수=0
    english=0 #전체 영어 점수=0
    math=0 # 전체 수학 점수=0

    while(1): # 무한 반복문
        a = f.readline() # a에 f.readline() 받기
        if(a==""): #만약 a가 모든 요소를 읽었을때
            break #반복문 탈출
        p=a.split(":") #p에 a를 :로 나눈 값을 리스트로 저장
        n+=1 #학생 수 1만큼 증가
        all+=int(p[1])+int(p[2])+int(p[3]) # 모든 과목 점수를 전체 점수에 더하기
        korean+=int(p[1]) #각 학생의 국어 점수 더하기
        english+=int(p[2]) # 각 학생의 영어 점수 더하기
        math+=int(p[3]) # 각 학생의 수학 점수 더하기

    print("===전체 평균===\n%.1f" %(all/(n*3))) #전체 평균 출력
    print("===각 학생 평균===") #출력
    f.seek(0) #파일 포인터를 처음으로 이동
    while(1): #무한 반복문
        a=f.readline() # a에 f.readline() 받기
        p = a.split(":") #p에 a를 :로 나눈 값을 리스트로 저장
        student = 0 #각 학생 점수=0
        if(a==""): #만약 a가 모든 요소를 읽었을때
            break #반복문 탈출
        for i in range(1,4): # i를 1~3 범위에서 반복문
            student+=int(p[i]) # 각 학생 점수에 모든 과목 점수 더하기
        print(p[0]+" %.1f" %(student/3)) #학생 이름과 각 학생 평균값 출력
    print("===각 과목 평균===") #출력
    print("국어 평균:%.1f" %(korean/n)) # 국어평균값 출력
    print("영어 평균:%.1f" %(english/n)) #영어평균값 출력
    print("수학 평균:%.1f" %(math/n)) #수학평균값 출력
    f.close() #파일 닫기