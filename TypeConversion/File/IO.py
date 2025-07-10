# .....File IO.....
# f = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#..........

f = open("E:\projects\OWII  PYTHON\TypeConversion\demo.txt","r")
data = f.read(5)# when the data is read than it cant be read line by line,exept f.read(5).  
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()