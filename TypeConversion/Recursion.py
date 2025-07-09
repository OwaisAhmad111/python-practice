num = int(input("Enter no"))
def show(num):
    if(num == 0): # base case
        return
    print(num)
    show(num-1)
show(num)

#............

def fact(n):
    if(n ==1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(5))

# Practice, Write a recursive function to calculate the sum of first n natural numbers ?

num = int(input("Enter a number:"))
def fun_name(num):
    if(num == 0):
        return 0
    return fun_name(num-1) + num
sum = fun_name(5)
print(sum)

# Practice, Write a recursive function to print all the elements in a list,use list and index as parameter ?

def fun_name(list,idx=0):
    if idx == len(list):
        return 0
    print(list[idx])
    fun_name(list,idx+1)
fruits= ["mango","banana","apple"]
fun_name(fruits)