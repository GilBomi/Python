a=input("수 입력:").split() #띄어쓰기를 기준으로 리스트로 나누기
print("a:",a)
n=0
for i in a:
    n+=1
print("n:",n)

p=0
i=0
j=0
if(n==1):
    print("single")
elif(n>=2):
    while(p+1<n):
        if(int(a[p])>=int(a[p+1])):
            i+=1
        elif(int(a[p])<=int(a[p+1])):
            j+=1
        else:
            break
        p+=1
    print(i)
    print(j)
    if(i==n-1):
        print("descending")
    elif(j==n-1):
        print("ascending")
    else:
        print("mixed")
