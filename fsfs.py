k=int(input("숫자를 입력하세요:"))

p=str(k)
print("역:",p[::-1])
l=0
for i in range(0,len(p)):
    l+=int(p[i])
print("합:",l)