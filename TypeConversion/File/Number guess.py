# actualno = 44
# num = 0
# while num<=7:
#     guess_number = print(int(input("Enter any number:")))
#     if guess_number == 44:
#         print("Corrct Number\n")
#         print(num+1,"Number of gueses he took to finish.")
#         break

#     elif guess_number <= 54 and guess_number >= 34:
#         print("Close to the acual number:\n")
#     elif guess_number > 54:
#         print("The number you choose is large, input small number\n")
#     elif guess_number <34:
#         print("The number you choose is small, input large number\n")
#     else:
#         print("")
#         num=num+1
# if num>8:
#     print("Game Over")
#..............
# actualno= 30
# num=0
# t = True
# while t:
#     x=int(input("guess the number\t"))
#     if x<actualno:
#         print("your guess was too low")
#         num= num +1
#     elif x>actualno:
#         print("your guess was too high")
#         num= num+1
#     else:
#         num=num+1
#         print(f"your guess is correct in {num} attempt")
#         t = False

actualno = 44
num = 0
t = True
while t:
    guess_no = print(int(input("Ente any number:")))
    if(guess_no == actualno):
        print("You Won")
        num+=1
    # elif(guess_no < actualno and guess_no > actualno):
    #     print("Closer to the number")
    #     num+=1
    elif(guess_no < actualno):
        print("Number is too low as compared to the actual")
        num+=1
    elif(guess_no < actualno ):
        print("Number is too large as compared to the actual") 
        num+=1
    else:
        num+=1
        print(f"Number of attempts are {num}")

