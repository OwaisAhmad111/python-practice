# Project (1)  ..'``Calculator``'..

# operator = input("Enter any operator (+ - * / %):")
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter 2nd number:"))

# if(operator == '+'):
#     print(num1+num2)
# elif(operator == '-'):
#     print(num1-num2)
# elif(operator == '*'):
#     print(num1 * num2)
# elif(operator == '/'):
#     print(num1/num2)
# elif(operator == '%'):
#     print(num1%num2)
# else:
#     print("Invalid input ")

# Project (2)..'``Convert kgs to pounds and pounds to pounds to kgs``'..

# weight = float(input("Enter your weight::"))
# unit = input("Is this in kgs or pounds(K,L):")

# if(unit == 'K'):
#     weight = weight * 2.205
#     print(f"Your weight is {round(weight,2)} lbs:")
# elif(unit == 'L'):
#     weight = weight/2.205
#     print(f"Your weight is {round(weight,2)} kgs: ")
# else:
#     print(f"invalid input {unit}")

# Project (3)..'``Convert celsius to fahrenheit to celius ``'..

# temp = float(input("Enter any temperature:"))
# unit = input("Is this temp in Celsius or fahreheit(C,F):")

# if(unit == 'C'):
#     temp = (temp * 9) / 5 + 32
#     print(f"Yous temp in fahrenheit is {temp} F")
# elif(unit =='F'):
#     temp = (temp - 32) * 5 / 9
#     print(F"Your temperature in celsius is {temp} C")
# else:
#     print(f"Invalid input {unit}:")

# Project (4)..'``In email split the username and domain``'..

# email = input("Enter you email:")

# index = email.index('@')

# username = email[:index]
# domain = email[index:]
# print(f"Your user name is {username} and the domain is {domain}")

# Project (5)..'``Python compound interest calculator``'..

# principal = 0
# rate = 0
# time = 0

# while principal <= 0:
#     principal = float(input("Enter you principal  amount:"))
# if principal <= 0:
#     print("Principal is not lass than or equal to 0:") 

# while rate <= 0:
#     rate = float(input("Enter you interest rate:"))
# if rate <= 0:
#     print("rate is not lass than or equal to 0:")

# while time <= 0:
#     time = float(input("Enter you interest time:"))
# if time <= 0:
#     print("time is not lass than or equal to:")
# total = principal * pow((1 + rate/100),time)
# print(print(f"your total balance is {total}"))

# Project (6)..'``Countdown timer``'..

# import time

# my_time = int(input("Enter any time in sec:"))
# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's up")

# Project (7)..'``Shoping Cart Progrm``'..

# prices = []
# foods = []
# total = 0

# while True:
#     food = input("Enter any food to buy (press q to quit):")
#     if food.lower() =="q":
#         break
#     else:
#         price = int(input(f"Enter the price of {food} Rs:"))
#         foods.append(food)
#         prices.append(price)

# print("-----Your Cart-----")
# for food in foods:
#     print(food,price)
# for price in prices:
#     total+=price
# print(f"Your total amount is {total}:")

# Project (8)..'``Python Quiz Game``'..

# questions = ("Which one is the IDE:",
#             "Which one is hardware:",
#             "1 Byte =",
#             "1 GB =")
# options = (("A. GitHub","B. VsCode","C. Memu","D. youtube"),
#            ("A. Mouse","B. facebook","C. imulator","D. brush"),
#            ("A. 2 Bits","B. 4 Bits","C. 6 Bits","D. 8 Bits"),
#            ("A. 1000 Mb","B. 1024 Mb","C. 999 Mb","D. 899 Mb"))
     
# answers = ("B","A","D","B")
# guesses = []
# score = 0
# question_no = 0
# for question in questions:
#     print("---------------")
#     print(question)
#     for option in options [question_no] :
#         print(option)
#     guess = input("Enter(A,B,C,D):")
#     guesses.append(guess)
#     if(guess == answers[question_no]):
#         print("Correct option")
#         score+=1
#     else:
#         print("Incorrect option")
#         print(f"{answers[question_no]} is the correct answer")
#     question_no+=1

# print("-------------")
# print("    Result   ")
# print("-------------")

# print("answers:",end="")
# for answer in answers:
#     print(answer,end=" ")
# print()

# print("guesses:",end="")
# for guess in guesses:
#     print(guess,end=" ")
# print()

# score = int(score/len(questions)*100)
# print(f"you total score is {score}%")

# Project (9)..'``Concession Stand Program``'..

# menu = {
#     "pepsi": 200,
#     "soda": 100,
#     "chips": 70,
#     "popcorn": 100,
#     "pizza": 500,
#     "burger":350,
#     "sandwitch":100
# }
# cart = []
# total = 0

# print("-----Your Menu-----")
# for key,val in menu.items():
#     print(f"{key:10}:Rs {val}")
# print("-------------------")

# while True:
#     food = input("Select you item (Q to quit):").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print("------Your order-----")
# for food in cart:
#     total += menu.get(food)
#     print(food,end=" ")

# print()
# print(f"Your total amount is: {total} Rs")

# Project (10)..'``Python Number Guessing Game``'..

# import random
# lowest_num = 1
# largest_num = 100
# answer = random.randint(lowest_num,largest_num)
# guesses = 0
# is_running = True

# print("---- Python Number Guessing Game -----")
# print(f"-- select a number between {lowest_num} to {largest_num} --")

# while is_running:
#      guess = input("Enter your guess:")

#      if guess.isdigit():
#             guess = int(guess)
#             guesses+=1
        
#             if guess < lowest_num or guess > largest_num:
#                 print("OUT OF RANGE")
#                 print(f"plz select a number between {lowest_num} to {largest_num}")
                
#             elif guess > answer:
#                 print("guess is Too high,Try again")

#             elif guess < answer:
#                 print("guess is Too low,Try again")
            
#             else:
#                 print(f"Corect! it is: {answer}")
#                 print(f"Number of guesses: {guesses}")
#                 is_running = False
    
#      else:
#        print("invalid guess")
#        print(f"plz select a number between {lowest_num} to {largest_num}")

# Project (11)..'``Rock,Paper,Scissors Game``'..

import random
options = ("rock","paper","scissrors")
# player = None
# computer = random.choice(options)
running = True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter any (rock,paper,scissrors):")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if(player == computer):
        print("Match Tie")
    elif(player == "rock" and computer == "scissors"):
        print("You Win")
    elif(player == "paper" and computer == "rock"):
        print("You Win")
    elif(player == "scissrors" and computer == "paper"):
        print("you win")
    else:
        print("You Lose")

    play_again = input("you want to play more(y/n):").lower()

    if not play_again == "y":
        running = False
print("--Thanks for Game--")



    

   





