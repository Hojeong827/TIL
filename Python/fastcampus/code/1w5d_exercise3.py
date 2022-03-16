# 아이폰 1, 2, 3
# 아이폰 1 : calling : print("calling")
# 아이폰 2 : send msg : print("msg")
# 아이폰 3 : internet : print("internet")

class Iphone1:
    def calling(self):
        print("calling")

class Iphone2(Iphone1):
    def send_msg(self):
        print("send msg")

class Iphone3(Iphone2):
    def internet(self):
        print("internet")
        
iphone3 = Iphone3()
iphone3.calling()
iphone3.send_msg()
iphone3.internet()

class Galuxy:
    def show_img(self):
        print("show img")

class DssPhone(Iphone3, Galuxy):
    def camera(self):
        print("camera")

dss_phone = DssPhone()
[func for func in dir(dss_phone) if func[:2] !="__"]