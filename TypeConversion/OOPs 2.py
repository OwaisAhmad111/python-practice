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

# del Keyword is used to deleate the object or its attributes.

# class ceo:
#     def __init__(self,name):
#         self.name = name
    
# c1 = ceo("junaid")
# print(c1.name)
# del c1.name # c1
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
# #print(a1.acc_pass) # it will throw an error bcz it is private inside a constructor.
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
#         super().__init__(brand)# super method is used to access method of the parent class.

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




        



