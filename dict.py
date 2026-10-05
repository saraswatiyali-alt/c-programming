# dictionary is a collection of key:value pairs. 
# Each key is associated with each value and we can retrive and manipulate data using key.

dict1 = {"name" : "laxmi","age": 20,"Degree":"BE"}
print(dict1)
print(type(dict1))

print(dict1["name"])# Accessing value

dict1["age"] = "39" # Updating the age
print(dict1) 

dict1["Friend"] = "nagaveni" # Adding a key value to the dictionary
print(dict1)

del dict1["age"] # Deleting the age by "del"
print(dict1)

dict1.pop("Degree") # Deleting key by "pop()"
print(dict1)

dict1.get("my heart")
print(dict1)

print(dict1.keys()) # return all the keys
print(dict1.values()) # Return all the values 
print(dict1.items()) # Return all key value pairs


new_dict = {"city":"gadag",}
dict1.update(new_dict)
print(dict1)

dict2 = {"gadag":"good","hubli":"bad"}
print(dict2)
dict3 = {"Mysure":"dosa","koppal":"vada"}

dict_total = [dict2, dict3,]
print(dict_total)

print(f"best food : {dict3["Mysure"] + " & "  + dict3["koppal"]}")

mix = {"city":"gadag",
       2 : "near sabarmati ashram",
       "list1" :{"ragi","rice"},
       "new dict":{"home":"hubli"},
       "weight" :"38.9 kg"}
print(mix)



