class coordinate:
    '''
    좌표를 표현하는 클래스 정의
    '''
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def print(self):
        print("좌표<"+str(self.x)+','+str(self.y)+">")

    def distance(self,c):
        sum=((((self.x-c.x)**2+(self.y-c.y)**2)**0.5))
        return sum

    def __str__(self):
        """
        :return: __str__은 문자열을 반환함
        """
        return "문자열 좌표<"+str(self.x)+','+str(self.y)+">"
c1=coordinate(2,3)
c2=coordinate(3,5)
print("== :",c1.__eq__(c2))
c1.print()
c2.print()

#__str__가 정의되었기 때문에 아래와 같이 출력 가능
print(c1) # return 문자열 되는 부분을 출력함

print(c1.distance(c2))
print(c2.distance(c1))

print(coordinate.distance(c1,c2)) #coordinate.으로 하면 self에 자동으로 들어가는게 없어서 직접 c1,c2로 적어서 self로 c1,c에 c2를 넣는다