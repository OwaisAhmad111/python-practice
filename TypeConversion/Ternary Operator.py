# ``'Ternary Operator / Single Line if``'

# <var> = <val1> if <condition> else <val2>
# food = input("you fav food :")
# food = "YES" if food == "cake" else "NO"
# print(food)

# <statement1> if <condition> else <statement2>

# food = input("your fav food:")
# print("SWEET") if food == "cake" or food == "jalaebi" else print("NOT SWEET")

# ``'Ternary Operator / Clever if``'
# <var1> = <false_value,true_value> [<condition>]
# age = int(input("Enter your age:"))
# vote = ("yes" , "no") [age < 18]
# print(vote)

# sal = float(input("Enter your sal:"))
# tax = sal*(0.1,0.2) [sal > 1000] # when the condition is true it will execute the write one which is 0.2 and vice versa.
# print(tax)

sal = float(input("Enter your sal:"))
increment = sal*(0.1,0.2) [sal < 1000]
print(increment)