#..."Abstraction", hiding the implementation details of a class and only showing the essential features to the user...

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.brk = True
#         self.clutch = True
#         print("Car is started")

# c1 = car()
# c1.start()

# Encapsulation, Wraping data and function in to single unit (object).

# class ceo:
#     def __init__(self,name):
#         self.name = name
    
# c1 = ceo("owais")
# print(c1.name)
# del c1.name # c1,  del Keyword is used to deleate the object or its attributes.
# print(c1.name)

# ...Private attributes and methods...

# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # "__" sign of private.
    
#     def reset(self):
#         print(self.__acc_pass)
    
# a1 = account(1234,"abcd")
# print(a1.acc_no)
# # print(a1.acc_pass), it will throw an error bcz it is private inside a constructor.
# a1.reset()

# ...'``Single inheritance``'...

# class car:
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
#     @staticmethod
#     def relibility():
#         print("features of relibility")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name = name

# tc1 = toyotacar("GLi corola")
# print(tc1.name)
# tc1.start()
# tc1.stop()
# tc1.relibility()

# ...'``Multilevel inheritance``'...

# class car:
#     @staticmethod
#     def start():
#         print("Car is started")
#     @staticmethod
#     def stop():
#         print("Car is stopped")
#     @staticmethod
#     def relibility():
#         print("features of relibility")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(toyotacar):
#     def __init__(self,varient,type,brand):
#         self.varient = varient
#         self.type = type
#         super().__init__(brand)# super method is used to access method of the parent class(toyotacar).

# c1 = Fortuner("sigma","diesel",2024)
# print(c1.type)
# print(c1.varient)
# c1.start()
# c1.stop()
# c1.relibility()
# print(c1.brand)

#..``'Multiple inheritance``'..

# class supra:
#    s = "sports car"

# class Lexus:
#    l = "Luxiary car"

# class Crown_RS(supra,Lexus):
#    cr = "Luxiary with speed"

# c1 = Crown_RS()
# print(c1.s)
# print(c1.l)
# print(c1.cr)

#.........................

# class student:
#     def __init__(self,DLD,Pro,netw):
#         self.DLD = DLD
#         self.Pro = Pro
#         self.netw = netw
#         self.percentage = str((DLD + Pro + netw) /3) + " % " #it doesn't gives the updated value.

#     def improve(self):
#         self.percentage = str((self.DLD + self.Pro + self.netw) /3) + " % "

# st1 = student(85,85,78)
# print(st1.percentage)

# st1.netw = 80
# print(st1.netw)
# st1.improve()
# print(st1.percentage)

#..........OR............

# class student:
#     def __init__(self,DLD,Pro,netw):
#         self.DLD = DLD
#         self.Pro = Pro
#         self.netw = netw
#         self.percentage = str((DLD + Pro + netw) /3) + " % " # it doesn't gives the updated value.

#     def improve(self):
#          return str((self.DLD + self.Pro + self.netw) /3) + " % "

# st1 = student(85,85,78)
# print(st1.percentage)
# st1.netw = 80
# print(st1.netw)
# print(st1.improve())

#..........OR............

#.......@property........
# class student:
#     def __init__(self,DLD,pro,netw):
#         self.DLD = DLD
#         self.pro = pro
#         self.netw = netw
    
#     @property
#     def improve(self):
#         return str((self.DLD + self.pro + self.netw) / 3) + "%"
# st1 = student(85,85,78)
# print(st1.improve)
# st1.netw = 81
# print(st1.netw)
# print(st1.improve)

# Polymorphism:

# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNum(self):
#         print(self.real,"i +", self.img,"j")
    
#     def add(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal,newImg)

# num1 = complex(-1,4)
# num1.showNum()
# num2 = complex(7,3)
# num2.showNum()
# print(".........")
# num3 = num1.add(num2)
# num3.showNum()

#... Using Dunder Functions ...

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNum(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal,newImg)
    

num1 = complex(3,6)
num1.showNum()
num2 = complex(5,2)
num2.showNum()
print("..........")
# num3 = num1 + num2
# num3.showNum()
num3 = num1 - num2
num3.showNum()




         



        



