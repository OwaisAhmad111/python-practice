# set = {1,2,3,2,4,"owii","ahmad","owii"}
# print(len(set)) # duplicate values are ignored
# print(type(set))

#....Empty Set....
# collection = set()
# print(type(collection))

#........Set Methods..........

# set = {1,2,3,4}
# set.add(5)
# set.remove(2)
# print(set)
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add((3,4,5))# touple
# collection.add("owais")
# #collection.add([1,2,3]) lists are mutable , it doesnt use in a sets
# collection.remove(2)

# collection.pop() # pop the elements randomly.
# collection.clear()
# print(collection)

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))