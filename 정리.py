"""
주제 : data type
작성일 : 2017년 9월 4일
작성자 : 길보미
"""
# float형 변수 f에 3.4를 저장,출력
f=3.4 # 파이썬은 정의할때 정해진 그릇 없으므로 int f이렇게 쓸 필요 없이 그냥 쓰기
print("f=",f) #파이썬에서 ','는 연결해주는 도구

# int형 변수 i에 1을 저장, 출력
i=1
print("i=" , i)

#bool형 변수 b에 True 저장, 출력
b=True # 대,소문자 지키기
print("b=",b)

# str형 변수 s에 '1'을 저장,출력
s="1"
print("s=",s)

# f와 i를 더해서 출력
print("f+i=",f+i)

# s와 i를 더해서 출력
# print("s+i:",s+i) 문자열과 int형은 자동적 변환이 불가능하므로 수동적인 변환으로.
#s를 int형으로 변환하여 i와 더하여 출력
print("int(s)+i=",int(s)+i)

#i를 문자열(str)로 변환하여 s와 더하여 출력
print("s+str(i)=",s+str(i))
#문자열+문자열은 그냥 문자열의 연결

#복소수 k를 정의해서 5+7j를 저장,출력
k=5+7j
#5는 실수(real), 7j는 허수(imag)
print("k=",k)
print("k.real=",k.real) # 실수(real) 출력
print("k.imag=",k.imag) # 허수(imag) 출력
print("켤레 복소수=",k.conjugate()) #켤레 복소수는 conjugate() 괄호까지 다 쓰기

#j에 28을 입력,i에 59를 입력
j=28
i=59

#i를 j로 나눈 값을 출력
print("i나누기 j=",i/j) # int형을 나누기(/)를 하면 flaot형으로 모든 결과값이 출력됨

print("i//j=",i//j) # //는 몫을 출력
print("i%j=",i%j)

#j의 세제곱 출력
print("j**3=",j**3)

# j에 -29 저장 후 j의 절대값(absolute) 출력
j=-29
print("abs(j)=",abs(j)) #줄여서 abs

#b(True) or False 출력
print("b or False=",b or False)

#b(True) and True 출력
print("b and True=",b and True)

#o에 8진수의 16을 저장하고 변수 그대로 출력
o=0o16 #8진수는 0o붙이기(o안붙이면 숫자 0이 헷갈리므로), 0o에 붙이는 숫자는 8진수로 환산된 값
print("o=",o) # 그냥 아무것도 안붙이고 o하면 10진수 값으로 출력됨
print("o=%o"%(o)) #8진수로 출력하기

#x에 16진수의 A5 대입, 변수 그대로 출력
x=0XA5 # 0x에 붙여서 쓴 값은 16진수로 환산된 값
print("x=",x)
#x를 16진수로 출력, 10진수로 출력, 8진수로 출력
print("x=%x" %x) #16진수로 출력
print("x=%d" %x) #10진수로 출력
print("x=%o" %x) # 8진수로 출력