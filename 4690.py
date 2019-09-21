a=2 #a는 2부터 시작
while(a<=100): #a<=100까지 반복
    b = 2 #b=2로 초기화
    c = 2 #c=2로 초기화
    d = 2 #d=2로 초기화

    while(b<=100): #b<=100까지 반복
        c=b #b,c,d순으로 크기가 커져야 돼서 정의
        if (a * a * a == b * b * b + c * c * c + d * d * d): #세제곱
            print("Cube = %d, Triple = (%d,%d,%d)" %(a, b, c, d)) #출력
        while(c<=100): #c<=100까지 반복
            d=c #b,c,d순으로 크기가 커져야 돼서 정의
            if (a * a * a == b * b * b + c * c * c + d * d * d): #세제곱
                print("Cube = %d, Triple = (%d,%d,%d)" %(a, b, c, d)) #출력
            while(d<=100): #d<=100까지 반복
                if (a * a * a == b * b * b + c * c * c + d * d * d): #세제곱
                    print("Cube = %d, Triple = (%d,%d,%d)" %(a, b, c, d)) #출력
                d+=1 #d 1만큼 증가
            c+=1 #c 1만큼 증가
        b+=1 #b 1만큼 증가
    a+=1 #a 1만큼 증가