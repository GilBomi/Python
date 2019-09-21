"""
이것도 다른 방법으로 풀어서 잘 돌아가는데
백준에서는 런타임에러뜸
왜?
"""
while(1):
    answer=[]
    nm=input("")
    if(nm=="0 0"):
        break
    nm=nm.split()
    l=[]
    for i in range(0,int(nm[0])):
        p=input("")
        p=p.split()
        for j in p:
            l.append(int(j))
    l.sort()
    l_no_overlap=list(set(l))
    num_list=[]
    for i in l_no_overlap:
        n=0
        for j in range(0,len(l)):
            if (i==l[j]):
                n+=1
        num_list.append(n)
    max=num_list[0]
    for i in num_list:
        if(max<=i):
            max=i
    k=0
    for i in num_list:
        if(max==i):
            del l_no_overlap[k]
        k+=1
    num_list.remove(max)
    max = num_list[0]
    for i in num_list:
        if (max <= i):
            max = i
    k = 0
    for i in num_list:
        if (max == i):
            answer.append(l_no_overlap[k])
        k += 1
    answer.sort()
    final_answer=""
    for i in answer:
        final_answer+=i+" "
    print(final_answer)