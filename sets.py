# Tuple Home work
My_tuple = ("rose","hibiskus","silly","niyas","tom")
"""My_tuple[0]="flower"
print(My_tuple)

My_tuple.append("lotus") # tuple method don't have "append" attribute
print(My_tuple)"""

print(My_tuple[2:4])

tuple2 = (1,2,3,4)
print(My_tuple + tuple2)

# Sets Homework
set1 = {"apple","banana","mango","orange"}
set2 = {"grapes","chikku","lemon","mango"}

print(set1|set2)
print(set1-set2)
print(set1&set2)

set1.add("dates")
print(set1)

set1.discard("mango")
print(set1)

set1.discard("pinaple")
print(set1)

set1.remove("banana")
print(set1)

set1.pop()
print(set1)

"""set1.remove("grapes")
print(set1)"""

list1 = ["laxmi","anjali",[1,2,"monika"]]
print(tuple(list1))

list2 = [26,785,938,7,53]

print(set(list2))
print(len(list1))

set1.add("l")
print(set1)

set3 = {"rohan","nirmala","vani"}

set3.pop()
print(set3)

empty_set = set()
print(type(empty_set))