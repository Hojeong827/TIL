# 스타크래프트의 마린을 클래스로 설계
# 체력(health : 40), 공격력(attack_pow : 5), 공격(attack())
# 마린 클래스로 마린 객체 2개를 생성해서 마린 1이 마린 2를 공격하는 코드를 작성
# attack(self, unit)
class Marine:
    
    def __init__(self):
        self.health = 40
        self.attack_pow = 5
    
    def attack(self, unit):
        unit.health -= self.attack_pow
        
        if unit.health <= 0:
            unit.health = 0
            print("사망")
    
marine_1=Marine()
marine_2=Marine()
marine_1.attack(marine_2)
print(marine_1.health, marine_2.health)

# 메딕 : heal_pow, heal(unit)
class Medic:
    def __init__(self, health=50, heal_pow=6):
        self.health = health
        self.heal_pow = heal_pow
    
    def heal(self, unit):
        if unit.health >0:
            unit.health += self.heal_pow
            if unit.health >= 40:
                unit.health = 40
        else:
            print("이미 사망")
            
medic = Medic()
medic.heal(marine_2)
print(marine_1.health, marine_2.health)


