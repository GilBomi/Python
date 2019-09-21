a=input("수를 입력하세요:")
k=int(a)
if(k==0):
    print("afdfa")
a=list(a)
a.reverse()
l=""

k=0
for i in range(0,len(a)):
    k+=int(a[i])
    l+=a[i]

print("역 :", l)
print("합 :",k)