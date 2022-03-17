"""
class Txt:
    def __init__(self, txt):
        self.txt = txt
    
t1 = Txt("python")
t2 = Txt("Python")
t3 = t1

print(t1 == t2, t1 == t3, t2 == t3)
Flase True False                    # '=='이라는 연산자는 magic method의 __eq__의 함수를 실행하는 것과 같음
"""


class Txt:
    def __init__(self, txt):
        self.txt = txt

    def __eq__(self, txt_obj):     # overriding
        return self.txt.lower() == txt_obj.txt.lower()
    
    def __repr__(self):            # overriding
        return "Txt(txt={}_".format(self.txt)
    
    def __str__(self):             # overriding
        return self.txt
    
t1 = Txt("python")
t2 = Txt("Python")
t3 = t1

print(t1 == t2, t1 == t3, t2 == t3)     # '==' 이라는 연산자가 __eq__라는 함수로 오버라이딩 됨
print(t1)                               # 주소값이 출력됨, <__main__.Txt object at 0x00000216F6D8A340>
                                        # 리를 overriding 한 후 출력하면 python이 출력됨(__str__)
t1                                      # Txt(txt=python) 으로 출력