class car:
    color = "White"
    name = "i7"
    brand = "BMW"
    
c1 = car()  # Object / instance
print(c1.color,c1.name,c1.brand)

#...'``constructors``'...

# Default Constructor

def __init__(self):
    pass

# Parameterized constructor

class student:
    college_name = "Govt Degree college" # class attribute

    def __init__(self,fullname,marks): # constructor
       self.name = fullname # object/instance attribute > class attr
       self.marks = marks
       print("Adding new student to the database.")
st1 = student("owais",89)
print(st1.name,st1.marks)# variables/attributes
print(st1.college_name)
st2 = student("Ahmad",78)
print(st2.name,st2.marks)
print(st2.college_name)

# ...Methods...

class student:

    def __init__(self,fullname,marks):
       self.name = fullname # object/instance attribute
       self.marks = marks
    
    def welcome(self): # Method
        print("welcome",self.name)
    
    def hello(self): # Method
        print("here is your marks",self.marks)

st1 = student("owais",85)
st1.welcome()
st1.hello()

#... Decorator...

class space:
    @staticmethod # decorator
    def stars():
        print("stars in sky")
s1 = space()
s1.stars()



