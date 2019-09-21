class fraction: # 이름이 fraction인 class 정의
    def __init__(self,a,b): #__init__함수 정의(자기자신,매개변수a와 b)
        self.x=a #self.x에 a저장
        self.y=b #self.y에 b 저장
    def __add__(self,other): #__add__함수 정의(자기자신, 매개변수 other)
        p=self.x*other.y+self.y*other.x #p에 self.x*other.y+self.y*other.x를 저장
        q=self.y*other.y #q에 self.y*other.y 저장
        return fraction(p,q) #fraction(p,q)를 반환
    def __sub__(self,other): #__sub__함수 정의(자기자신, 매개변수 other)
        p = self.x * other.y-self.y * other.x #p에 self.x * other.y-self.y 저장
        q = self.y * other.y #q에 self.y * other.y저장
        return fraction(p, q) #fraction(p,q)반환
    def __eq__(self,other): #__eq__함수 정의(자기자신, 매개변수 other)
        p=self.x*other.y # p에 self.x*other.y 저장
        q=self.y*other.x # q에 elf.y*other.x 저장
        return p==q # p와 q가 같은지 여부 반환
    def __lt__(self,other):#__lt__함수 정의(자기자신, 매개변수 other)
        p = self.x * other.y #p에 self.x * other.y 저장
        q = self.y * other.x #q에 self.y * other.x 저장
        return p < q #p가 q보다 작은지 여부 반환
    def __gt__(self,other):  #__gt__함수 정의(자기자신, 매개변수 other)
        p = self.x * other.y #p에 self.x * other.y 저장
        q = self.y * other.x #q에 self.y * other.x 저장
        return p > q #p가 q보다 큰지 여부 반환
    def __ne__(self,other): #__ne__함수 정의(자기자신, 매개변수 other)
        p = self.x * other.y #p에 self.x * other.y 저장
        q = self.y * other.x #q에 self.y * other.x 저장
        return p != q #p가 q하고 다른지 여부 반환
    def __str__(self): #__str__함수 정의(자기자신)
        return str(self.x)+"/"+str(self.y) #문자열로 self.x/self.y 분수 반환

c1=fraction(2,4) #c1에 fraction(2,4) 저장
c2=fraction(4,7) #c2에 fraction(4,7) 저장

print("c1+c2 :",c1.__add__(c2)) #c1+c2f를 c1.__add__(c2)을 이용해서 출력
print("c1-c2 :",c1.__sub__(c2)) #c1-c2f를 c1.__sub__(c2)을 이용해서 출력
print("c1==c2 :",c1.__eq__(c2)) #c1==c2f를 c1.__eq__(c2)을 이용해서 출력
print("c1>c2 :",c1.__gt__(c2)) #c1>c2f를 c1.__gt__(c2)을 이용해서 출력
print("c1<c2 :",c1.__lt__(c2)) #c1<c2f를 c1.__lt__(c2)을 이용해서 출력
print("c1!=c2 :",c1.__ne__(c2)) #c1!=c2f를 c1.__ne__(c2)을 이용해서 출력
