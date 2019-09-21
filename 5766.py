"""
잘 돌아가나 백준에서는 런타임에러 뜸
뭐가 문제?
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
    l_no_overlap=set(l)
    num_map={}
    for i in l_no_overlap:
        n=0
        for j in range(0,len(l)):
            if (i==l[j]):
                n+=1
        num_map[i]=n
    max=num_map[l[0]]
    for i in num_map.values():
        if(max<=i):
            max=i
    for key,value in num_map.items():
        if(value==max):
            first=key
    del num_map[first]
    max = num_map[l[0]]
    for i in num_map.values():
        if(max<=i):
            max=i
    for key,value in num_map.items():
        if(value==max):
            answer.append(key)
    answer.sort()
    answer_final=""
    for i in answer:
        answer_final+=str(i)+" "
