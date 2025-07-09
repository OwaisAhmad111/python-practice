# Q1 WAP to ask the user to enter the names their 3 fav movies and stored them in a list? In my version

mov1 = input("Enter your 1st fav movie:")
mov2 = input("Enter your 2nd fav movie:")
mov3 = input("Enter your 3rd fav movie:")

list = [mov1,mov2,mov3]
print(list)

# True version
movies = []
mov1 = input("Enter your 1st fav movie:")
mov2 = input("Enter your 2nd fav movie:")
mov3 = input("Enter your 3rd fav movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# Q2 WAP to check if a list contains a palidrome of elements? In my version

list = [1,2,3,2,1]
c = list.copy()
c.reverse()
print(list)
print(c)

# True version
list1 = ['m','a','m']
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# Q3 WAP to count the number of students with "A" grade in the following touple?

grade = ('C','D','A','A','B','B','A')
#grade.count('A')
print(grade.count('A'))


# Q4 Store the above values in a list and sort them from "A" to "D"?

list = ['C','D','A','A','B','B','A']
list.sort()
print(list)


