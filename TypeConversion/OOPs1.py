class car:
    color = "White"
    name = "i7"
    brand = "BMW"
    
c1 = car()  # Object / instance
print(c1.color,c1.name,c1.brand)

#...constructor...

class student:
    def __init__(self,fullname,marks):
       self.name = fullname
       self.marks = marks
       print("Adding new student to the database.")
st1 = student("owais",89)
print(st1.name,st1.marks)
st2 = student("Ahmad",78)
print(st2.name,st2.marks)