# .....File IO.....

f = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#..........

f = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","r")
data = f.read(5) # when the data is read than it cant be read line by line,exept f.read(5).  
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close()

#......Writing to a file......

file = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","w") # Write
data = file.write("I want to learn DSA")
print(data)

#....Append....

file = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","a") # Write
data = file.write("\nBut currently practice in Python")
print(data)

# If you mention a file name but it doesnt exist then the compiler made it automaticaly in "w" and "a" mode.

f = open("sample.txt","w")
data = f.write("owais")
print(data)
