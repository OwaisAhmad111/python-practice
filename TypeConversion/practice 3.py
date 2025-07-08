# Q1.``'WAP to make a simple calculator``'?
operator = input("Enter any given operator:")
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))

if(operator == "+"):
    result = num1+num2
    print(round(result,3))
elif(operator == "-"):
    result = num1-num2
    print(round(result,3))
elif(operator == "*"):
    result = num1*num2
    print(round(result,3))
elif(operator == "/"):
    result = num1/num2
    print(round(result,3))
else:
    print("Invalid")

# Q2 Write a program to check if a number entered by the user is odd or even?

num = int(input("Enter any number :"))
# rem = num%2
if(num%2 ==0):
    print("Even")
else:
    print("odd")

#  Q3 WAP to find the greatest of 3 numbers entered by the user?

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if(a>=b and a>=c):
    print("1st is largest",a)

elif(b>=a and b>=c):
    print("2nd is largest",b)

else:
    print("Third is largest:",c)


#  Q4 WAP to find the greatest of 4 numbers entered by the user?

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = int(input("Enter 4th number:"))

if(a>=b and a>=c):
    print("1st is largest",a)

elif(b>=a and b>=c):
    print("2nd is largest",b)

elif(c>=a and c>=b and c>=d):
    print("Third is largest",c)

else:
    print("4th is largest:",d)

#  Q5 WAP to check if a number is multiple of 7 or not?

num = int(input("Enter a number:"))

if(num % 7 == 0):
    print("Multiple of 7")

else:
    print("Not multiple")
