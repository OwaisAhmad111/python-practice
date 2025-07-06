# info = {
#     "keys" : "Values", 
#     "name" : "owais",
#     "age" : 19,
#     12 : 43,
#     "subjects" : ["cs","programming","DLD"],
#     "topics" : ("Dictionary","Set"),
#     "salary" : 10000.98
# in keys dictionary and list are not used.
# }
# print(info)
# we can laso access only the values/answers.
# print(info["name"])
# print(info["subjects"])
# info["name"] = 19
# info["age"] = 20
# print(info)

#.....................

#.......Null Dictionary..........
# Null_Dict = {}
# Null_Dict["Name"] = "owais"
# print(Null_Dict)

#........Nested Dectionary.........

# dect = {
#     "name" : "owais",
#     "subjects" : {
#         "DLD" : 85,
#         "Pro" : 85,
#         "DM" :  85
#     },
#     "Age" : 19
    
# }
# print(dect["name"])
# print(dect["subjects"])
# print(dect["subjects"]["DLD"])

#.........Dictionary Methods.........

dict = {
    "name" : "owais",
    "subjects" : {
        "phy" : 79,
        "Pro" : 78,
        "DLD" : 90
    },
    "age" : 19
}
# print(list(dict.keys()))
# print(list(dict.values()))
#print(list(dict.items()))
#print(dict.get("name2")) # print(dict["name"])
dict.update({"city" : "peshawr"})
print(dict)
dict.update({"age" : 20})
print(dict)

# NOTE: List and Dictionarys are mutable.
