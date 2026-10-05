my_list = ["apple","banana","orange","mango"]
print(my_list[3])

num = [2,3,5,7,4,9]
print(num)
print("numbers:",num[0: :2])

print(my_list)

list = ["laxmi","janu",45,["monisha",67,[False]]]
print(list[-1][-1])
print(list[3][0])


print(list*2)

list2 = [5,6,8,64,0]*3
print(list2)

items = ['sugre','coffee','milk','marigold']
items[1] = "bread"
print(items)

items.append("butter")
print(items)

items.insert(4,"mixture")
print(items)

items.remove("milk")
print(items)

items.pop()
print(items)

items.pop(1)
print(items)

items.clear()
print(items)

item1 = [1,2,3,4]
item2 = [5,6,7,8,9]
c_items = item1+item2
print(c_items)

print(len(c_items))
print(sum(c_items))

fruits = ['pinaple','paru','chikku','kivi','chikku']

print(sorted(fruits))
print(fruits)

print(fruits.index("chikku"))
print(fruits.count("chikku"))

numbers = [6,5,3,9,5,7,2]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

print(matrix[2][1])
print(matrix[-1])

