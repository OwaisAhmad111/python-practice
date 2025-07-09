# Q1 Store the following meaning of words in a python dictionary ?

dict = {
    # "table" : "a piece of funiture" "list of facts and figures", Note: 2 values in a single key uese if we use list or touple in bw of values.
    "cat" : "a small animal",
    "table" : ["a piece of funiture","list of facts and figures"]
}
print(dict)

# Q2 You are given a list of students for subjects,Assume 1 classroom is required for 1 subject, how many classrooms are needed for a all students?
#"Python","java","c++","python","javascipt",
#"java","python","java","c++","c"

set = {"python","java","c++","python","javascipt","java","python","java","c++","c"}
print(len(set))

# Q3 WAP to enter marks of 3 subjects from the user and store them in a dictionary,start with an empty dictionary and add one by one, use subject
# name as key and marks as values

x = int(input("Enter DLD  marks:"))
y = int(input("Enter DM  marks:"))
z = int(input("Enter Pro  marks:"))

dict = {}
dict["DLD"]  =  x
dict["DM"] = y
dict["Pro"] = z

print(dict)

# ......OR......

dict = {}

x = int(input("Enter DLD marks:"))
dict.update({"DLD" : x})
y = int(input("Enter DM marks:"))
dict.update({"DM" : y})
z = int(input("Enter Pro marks:"))
dict.update({"Pro" : z})
print(dict)

# Q4 Figure out a way to store 9 and 9.0 as separate values in the set,(you can take help of built in data types)

set = {9,9.0}
print((set))

SetTuple = {
    ("float" , 9.0), # we only use tuple inside set bcz of dicts and lists are mutable
    ("int" , 9)
         }
print(SetTuple)




