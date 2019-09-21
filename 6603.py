"""
맞게는 나오나 sort썼는데 문자열로 sort되서 그런지
숫자 크기순이 아니라 문자열 순서대로 나옴.
나머지는 다 맞으나 백준에서 시간초과됨
"""
import random
l=[]
while(1):
    k=input()
    if(k=="0"):
        break
    l.append(k)
for i in l:
    s1=int(i[0])
    s2=i[2:]
    s2=s2.split()
    s3=s1
    sum=1
    p=0
    while(1):
        sum*=s3
        s3-=1
        p+=1
        if(p==6):
            break
    for i in range(1,7):
        sum=sum//i
    s_final=[]
    while(1):
        s_list = []
        s_list2=[]
        s_str=""
        while(1):
            r=random.randint(0,s1-1)
            s_list.append(s2[r])
            s_list2=set(s_list)
            if(len(s_list2)==6):
                break
        s_list2=list(s_list2)
        s_list2.sort()
        for i in s_list2:
            s_str+=i+" "
        s_final.append(s_str)
        if(len(set(s_final))==sum):
            s_final=list(set(s_final))
            s_final.sort()
            for i in s_final:
                print(i)
            break
    print("\n")