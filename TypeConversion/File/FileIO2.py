f = open("E:\projects\OWII  PYTHON\TypeConversion\File\sample.txt","r+")# "r+" overright at the starting pf the file.
f.write("Hello")
print(f.read())
f.close()

# "w+" used for read and write but will first truncate (wipedout) the file first and then we can write something.

f = open("E:\projects\OWII  PYTHON\TypeConversion\File\sample.txt","w+")
f.write("Hello")
print(f.read())
f.close()

# ..."a+" append at the end of the file...

f = open("E:\projects\OWII  PYTHON\TypeConversion\File\sample.txt","a+")
f.write("Hello")
print(f.read())# if we use print than it will also show something in the terminal.
f.close()

# ...With Syntax...

with open("E:\projects\OWII  PYTHON\TypeConversion\File\sample.txt","r") as f:
    data = f.read()
    print(data)
with open("E:\projects\OWII  PYTHON\TypeConversion\File\sample.txt","w") as f:
    data = f.write("Hello")
    print(data)

# ...Import OS...

import os
os.remove("E:\projects\OWII  PYTHON\TypeConversion\File\garbage.txt")