def extent_function(base_line,height): #삼각형의 밑변과 높이를 매개변수로 받아 면적을 계산하는 함수 선언
    triangle_extent=base_line*height/2 #삼각형의 면적 계산해서 triangle_extent에 저장
    return triangle_extent #triangle_extent리턴
print("lab0_3: 길보미") #이름출력
base_line=int(input("밑변 입력:")) #base_line에 정수 입력
height=int(input("높이 입력:")) #height에 정수 입력
print("면적 =",extent_function(base_line,height)) #위의 함수 이용해서 면적 출력