print("n e") #출력
print("- -----------") #출력
n=0 #n은 0부터 시작
while(n<=9): #n을 9까지 반복
    sum = 1 #sum=1로 초기화
    if(n==0): #만약 n이 0이면
        answer=1 #answer은 1
    else: #그 외
        for i in range(1,n+1): #1부터 n까지 반복
            sum*=i #sum에 i를 계속 곱해줌
        answer+=1/sum #answer에 1/sum을 더함
    if(n==0 or n==1):
        print("%d %d" % (n, answer))  # n과 answer값 출력
    elif(n==2):
        print("%d %.1f" % (n, answer))  # n과 answer값 출력
    else:
        print("%d %.9f" %(n,answer)) #n과 answer값 출력
    n+=1 #n을 1 증가
