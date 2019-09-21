"""
주제 : 매개변수로 넘어오는 x번째 피보나치 수를 반환하는 함수 fibo를 정의하라. recursion으로.
(0번째부터 시작한다고 가정한다.)
작성자 학번 : 201732002
작성일 : 2017.10.24
"""

def fibo(n):  #fibo함수 정의(변수 n)
    """
    :param n: 피보나치 수의 순서를 0부터 시작해서 n번째를 구하기 위해 필요한 n
    :return:fibo(n-1)
    """

    if(n==0): #만약 n이 0이면
        return 0 #0을 반환
    elif(n==1): #만약 n이 1이면
        return 1 #1을 반환
    elif(n>=2): # 만약 n이 2 이상이면
        return fibo(n-1)+fibo(n-2) #fibo(n-1)+fibo(n-2)반환

print(fibo(6)) # fibo함수에 6을 넣어서 출력