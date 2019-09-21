print("대기자 추가 : A\n")
print("대기자 호출 : C\n")
a=input("명령어(A/C):")
k=[]
while (len(a)!=0):
    if(a=="A"):
        p=input("대기자 성명 : ")
        print("==대기자 명단==\n")
        k.append(p)
        for i in k:
            print(i)
        print("대기자 추가 : A\n")
        print("대기자 호출 : C\n")
        a = input("명령어(A/C):")
        continue
    elif(a=="C"):
        q=input("호출 고객 :")
        k.remove(q)
        print("==대기자 명단==\n")
        for i in k:
            print(i)
        print("대기자 추가 : A\n")
        print("대기자 호출 : B\n")
        a = input("명령어(A/C):")
        continue
    else:
        print("A나 C입력하세요\n")
        print("대기자 추가 : A\n")
        print("대기자 호출 : C\n")
        a = input("명령어(A/C):")
        continue
