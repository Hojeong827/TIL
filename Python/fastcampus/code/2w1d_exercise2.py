# Integer 객체
class Integer:
    def __init__(self, number):
        self.number = number
        
    def __add__(self, obj):
        return self.number + obj.number
    
    def __str__(self):
        return str(self.number)
    
    def __repr__(self):
        return str(self.number)
    
num1=Integer(1)
num2=Integer(2)
print(num1+num2)
print(num1)