# Project (1)  ..'``Calculator``'..

operator = input("Enter any operator (+ - * / %):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter 2nd number:"))

if(operator == '+'):
    print(num1+num2)
elif(operator == '-'):
    print(num1-num2)
elif(operator == '*'):
    print(num1 * num2)
elif(operator == '/'):
    print(num1/num2)
elif(operator == '%'):
    print(num1%num2)
else:
    print("Invalid input ")

# Project (2)..'``Convert kgs to pounds and pounds to pounds to kgs``'..

weight = float(input("Enter your weight::"))
unit = input("Is this in kgs or pounds(K,L):")

if(unit == 'K'):
    weight = weight * 2.205
    print(f"Your weight is {round(weight,2)} lbs:")
elif(unit == 'L'):
    weight = weight/2.205
    print(f"Your weight is {round(weight,2)} kgs: ")
else:
    print(f"invalid input {unit}")

# Project (3)..'``Convert celsius to fahrenheit to celius ``'..

temp = float(input("Enter any temperature:"))
unit = input("Is this temp in Celsius or fahreheit(C,F):")

if(unit == 'C'):
    temp = (temp * 9) / 5 + 32
    print(f"Yous temp in fahrenheit is {temp} F")
elif(unit =='F'):
    temp = (temp - 32) * 5 / 9
    print(F"Your temperature in celsius is {temp} C")
else:
    print(f"Invalid input {unit}:")

# Project (4)..'``In email split the username and domain``'..

email = input("Enter you email:")

index = email.index('@')

username = email[:index]
domain = email[index:]
print(f"Your user name is {username} and the domain is {domain}")

# Project (5)..'``Python compound interest calculator``'..

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter you principal  amount:"))
if principal <= 0:
    print("Principal is not lass than or equal to 0:") 

while rate <= 0:
    rate = float(input("Enter you interest rate:"))
if rate <= 0:
    print("rate is not lass than or equal to 0:")

while time <= 0:
    time = float(input("Enter you interest time:"))
if time <= 0:
    print("time is not lass than or equal to:")
total = principal * pow((1 + rate/100),time)
print(print(f"your total balance is {total}"))

# Project (6)..'``Countdown timer``'..

import time

my_time = int(input("Enter any time in sec:"))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up")

