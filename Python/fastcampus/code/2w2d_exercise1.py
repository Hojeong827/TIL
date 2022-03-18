# 계좌 클래스 만들기
# 변수 : 자산(asset), 이자율(interest)
# 함수 : 인출(draw), 입금(insert), 이자추가(add_interest)
# 인출시 자산이상의 돈을 인출할 수 없습니다.

class Account:
    
    def __init__(self, asset=0, interest=1.05):
        self.asset = asset
        self.interest = interest
    
    def draw(self, money):
        if self.asset >= money:
            self.asset -= money
            print("{}원이 인출되었습니다.".format(money))
        else:
            print("인출금이 {}원 부족합니다.".format(money-self.asset))
    
    def insert(self, money):
        self.asset += money
        print("{}원이 입금되었습니다.".format(money))
    
    def add_interest(self):
        self.asset *= self.interest
        print("이자가 지급되었습니다.")
        
    def __repr__(self):
        return "Account(asset:{}, interest:{})".format(self.asset, self.interest)

account1=Account(10000)
print(account1.asset, account1.interest)
print(account1)
account1.draw(12000)
account1.draw(3000)
account1.insert(5000)
account1.add_interest()