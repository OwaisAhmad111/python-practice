# list = [1,2,3,4,5]

# for el in list:
#     print(el)

#........................

# list2 = "owaisahmad"
# for el in list2:
#     print(el)

#......................


# list3 = ("owais","ahmad","talha","mustafa")
# for el in list3:
#     print(el)

#...........................

# list3 = ["owais","ahmad","talha","mustafa"]
# for el in list3:
#     if(el == "ahmad"):
#         print("``Ahmad found``")
#         break
#     print(el)
# else: # if we use print("End") than in case of break it wouldn't skip.
#     print("End")

#........For Loop practice question.......
    
# Q1 print the elements of the following list using for loop.[1,4,9,16,25,36,49,64,81,100]
# list = [1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     print(el)

# Q2 Search for a number x in this touple using for loop,[1,4,9,16,25,36,49,64,81,100]

# list = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# idx = 0
# for el in list:
#     if(el == 49):
#         print("found at index :",idx)
#     idx+=1

#........................

# seq = range(7)
# for i in seq:
#     print(i)

#.....OR.....

# for i in range(7):
#     print(i)

#.................

# for i in range(0,11,2):
#     print(i)

#.............Practice.............

# Q1 print the numbers from 1 to 100 using for and range()? 

# for i in range(1,101,1):
#     print(i)

# Q2 print the numbers from 100 to 0 ?

# for i in range(100,0,-1):
#     print(i)

# Q3 print the multiplication table of number n ?

# num = int(input("Enter a number to make a table:"))

# for i in range(1,11,1):
#     print(num ,"*",i,"=",num*i)

# Q4 WAP to print the sum of n natural numbers ?

#.........BY USING WHLE LOOP.........

# num = int(input("Enter any number:"))
# sum = 0
# i = 1
# while i<=num :
#     sum+=i
#     i+=1
# print("Total sum",sum)

#.....USING FOR LOOP.....    

# num = int(input("Enter any number:"))
# sum = 0
# for i in range(1,num+1):
#     sum+=i
# print("Total sum",sum)

# Q5 WAP to find the factorial of n number using for loop?

num = int(input("Enter any number:"))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("FACTORIAL:",fact)


#.....Pass Statement.....

# for i in range(5):
#     pass
# print("Some usefull work")





