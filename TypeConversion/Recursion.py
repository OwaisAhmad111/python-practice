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