#.......Practice on Functions.......

# Q1 WAF to print the length of the list (list is the parameter) ? 

names = ["owais","ahmad","muhammad","khalil"]
name2 = ["peshawar","karachi","punjab","balochistan",".."]
def fun_name(list):
    print(len(list))

fun_name(names)
fun_name(name2)

# Q2 WAF to print the elements of a list in a single line (list is the parameter) ?

names = ["owais","ahmad","muhammad","khalil"]
name2 = ["peshawar","karachi","punjab","balochistan",".."]
def fun_name(list):   # also use print(names[0]),....
    print(len(list))
def fun_list(list):
    for item in list:
        print(item,end=" ")
fun_list(names)
fun_name(names)
fun_list(name2)

# Q3 WAF to find the factorial of n.(n is the parameter) ?

def fun_name(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fun_name(5)

# Q4 WAF to convert USD to PKR ?

def converter(USD):
    pkr = USD*283
    print(USD,"USD = ",pkr,"pkr")
converter(2)

# Q5 WAF to find even or odd number ?

num = int(input("Enter a number:"))
def fun_name(num):
    if num%2 == 0:
        print("even no")
    else:
        print("Odd no")
fun_name(num)

    
    

    