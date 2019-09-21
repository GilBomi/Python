"""
답은 나오는데 n에 입력받는 숫자가 어느정도 커지면 실행했을때
반복을 많이해야되서 그런지 아얘 실행되지 않음.
백준에서는 시간초과됨
"""
num_time=int(input(""))
k=1
answer=[]
while(k<=num_time):
    n=int(input(""))
    zero_num=0
    sum=1
    all=0
    for i in range(1,n+1):
        sum*=i
    for i in str(sum):
        all+=1
    for i in range(all-1,0,-1):
        if(str(sum)[i]=="0"):
            zero_num+=1
            if(str(sum)[i-1]!="0"):
                break
    answer.append(zero_num)
    k+=1
for i in answer:
    print(i)