a=input("수 입력:").split() #띄어쓰기를 기준으로 리스트로 나누기
print("a:",a)
n=0
for i in a:
    n+=1
print("n:",n)

p=0
i=0
j=0
mm=0
nn=0
if(n==1):
    print("single")
elif(n>=2):
    while(p+1<n):
        if(int(mm)>=int(a[p+1])):
            mm=a[p]
        elif(int(a[p])<=int(nn)):
            nn=a[p+1]
        else:
            break
        p+=1
    print(nn)
    print(mm)
    if(mm==a[0]):
        print("descending")
    elif(nn==a[n-1]):
        print("ascending")
    else:
        print("mixed")
