#**** finding Palindrom ****
# while True:
#     var = input("Enter a word to check the palindrom:")
#     if(var == var[::-1]):
#         print("Palindrom")
#     else:
#         print("Not palindrom")

# **** finding vowel ****

# def count_vowel(input):
#     vowel = "aeiou"
#     count = 0
#     for char in input:
#         if char in vowel:
#             count+=1
#     return count
            
# input = input("Enter any word/sentence to count the vowel:")
# print(f"Number of vowels:{count_vowel(input)}")

'''Q1 define a circle class to create a circle with radius r using the constructor ,define an
area() method of the class which calulates the area of the circle,define a perimeter() method
of the class which allows you to calculate the perimeter of the circle.'''

# class circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = circle(21)
# print(c1.area())
# print(c1.perimeter())

'''Q2 '''
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role = ",self.role,"\n"
              "dept = ",self.dept,"\n"
              "salary = ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("ceo", "IT", "700000")
    
    def details(self):
        print("name = ",self.name,"\n"
              "age = ",self.age)

eng1 = Engineer("owais","19")
eng1.showDetails()
eng1.details()