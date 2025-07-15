# Q1 Create a new file practice.txt in python, Add the following in it ?

# { Hi everyone
# we are learning File I/O
# Using Java
# i like programming in Java }

f = open("practice.txt","w")
f.write("Hi everyone\nwe are learning File I/O\nUsing Java\ni like programming in Java ")

# Q2 WAF that replaces all the occurences of Java with python in the above file ?

def fun():
  f = open("practice.txt","r")
  data = f.read()
  new_data = data.replace("Java","Python")
  print(new_data)

  f = open("practice.txt","w")
  f.write(new_data)
fun()

# Q3 Search if the word "learning" exists in the above file ?

def check_for_word():
   f = open("practice.txt","r")
   data = f.read()
   if data.find("learning") != -1:
     print("Found")
   else:
     print("Not found")
check_for_word()

# Q4 WAF to find in which line of the file does the word "learning" occue first, print -1 if the word not found ?

def check_for_line():
  word = "programming"
  data = True
  lineno = 1
  f = open("practice.txt","r")
  while data:
      data = f.readline()
      if(word in data):
        print(lineno)
        return
      lineno+=1
  return -1
print(check_for_line())

 # Q5 Find the even no from the file?
count = 0
with open("Practice.txt","r") as f:
 data = f.read()
 print(data)
nums = data.split(",")
for val in nums:
 if(int(val) %2 ==0):
  count+=1
print(count)

