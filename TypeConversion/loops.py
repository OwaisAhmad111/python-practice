#.....While Loop.......

i = 1
while i<=8:
    print("owais",i)
    i+=1

#.....................

x = 10
while x>=1:
    print("owais",x)
    x-=1

#.....................

x = 1
while x<=10:
    print("3 *" ,x ,"=", 3*x)
    x+=1

# ................

i = 1
n = int(input("Enter value to make a table:"))
while i<=10:
    print(n,"*",i,"=",n*i) 
    i+=1
#...........

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx<len(nums):
    print(nums[idx])
    idx+=1

#..............

num = int(input("Enter a number:"))
touple = (1,4,9,16,25,36,64,81,100)

idx = 0
while  idx<len(touple):
    print(touple[idx] == num)
    idx+=1

#.........OR..........

tuple = (1,4,9,16,25,36,64,81,100)
x = 16
i = 0
while i<len(tuple):
    if(tuple[i] == x):
        print("Found at index",i)
        break
    else:
        print("Founding...")
    i+=1

#.....Break and Continue.....

i = 0
while i<=5:
    if(i ==3):
        break
    print(i)
    i+=1 

#.................

i = 0
while i<=5:
    if(i ==3):
        i+=1
        continue
    print(i)
    i+=1







   

    