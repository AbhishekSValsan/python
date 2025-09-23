list_fruit = ["apple","orange","mango"]
list_veg = ["cucumber","carrot","tomato"]
list_bev = ["tea","coffee","juice","water"]

list_fruit.append("pineapple")
print(list_fruit)

list_veg.insert(1, "pumpkin")
print(list_veg)

del list_bev[2]
print(list_bev)

inventory = list_veg + list_fruit + list_bev
print(inventory)

print(list_fruit[0:2])

print(list_veg[-1])

print(len(list_veg))
list_veg = [4**x for x in range(4)]
print(list_veg)

if "water" in list_bev:
    print("yes, 'water' is in the list")

    my_tuple = ("apple","cucumber","tea")
    print(my_tuple)