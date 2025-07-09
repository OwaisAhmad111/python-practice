light = input("Enter colour:")
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")

#..................

marks = int(input("Enter yor marks:"))
if(marks >=84 and marks <= 100):
    print("4 GPA")
elif(marks >=73 and marks <84):
    print("3 GPA")
elif(marks >=60 and marks <73):
    print("2 GPA")
elif(marks >=50 and marks <60):
    print("1 GPA")
else:
    print("Fail")

#....................

# Nesting

age = int(input("Enter your age:"))

if(age>=18):
    if(age>=80):
        print("Cannot Drive")
    else:
        print("Can drive")
else:
    print("can drive")


