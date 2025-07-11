
actualno = 96
num = 0
t = True
while t:
    guessno = int(input("Enter any number:"))
    if(guessno > actualno):
        print("Number is too high")
        num = num+1
    elif(guessno < actualno):
        print("Number is too small")
        num = num+1
    else:
        num = num+1
        print(f"Corect in {num} attempts")
        t = False
    




