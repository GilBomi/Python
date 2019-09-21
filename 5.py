l=[1,3,5]
for i in l:
    print(i)
s="성공회대학교"
for i in s:
    print(i)
for i in range(1,6,2): #1~5까지 2만큼 건너뛰면서
    print(i)
#1에서부터 100까지 합을 구하시오
sum=0
for i in range(1,101):
    sum+=i
print("합 :",sum)
#1에서 100까지 3의 배수의 합을 구하여 출력하라
sum=0
for i in range(3,100,3): # range(99,0,-3)와 같은 의미
    sum+=i
print("3의 배수 합 :",sum)
#1에서 100까지의 합을 while을 이용해서 출력
sum=0
i=0
while i<101:
    i += 1
    if i%3!=0:
        continue
    else:
        sum+=i
print("while문의 합 : ",sum)
"""
사용자로부터 입력받은 수의 모든 약수 구하기
1부터 사용자로부터 입력받은 수까지 각각의 모든 약수 구하여 리스트 형태로 출력
"""
i=0
a=int(input("값을 입력하세요 :"))
print("약수 :")
while i<=a:
    i += 1
    if a%i==0:
        print(i)
i=0
k=0
while i<a:
    i+=1
    k=0
    l = []
    print(i,"의 약수 :")
    while  k<=i:
        k+=1
        if i%k==0:
            l.append(k)
    print(l)
#pythontutor라는 사이트 이용하면 함수 진행 과정 쉽게 볼 수 있음

