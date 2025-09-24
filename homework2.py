items = ["milk", "eggs", "bread"]

def add_item(item):
    items.append(item)
    return items
print("item", add_item("butter"))

def remove_item(item):
    items.pop()
    return items
print("item", remove_item("butter"))

#lambda for display
display = lambda items: print(f"items",{items})
for x in items:
    print(x)

#recursive characetre

def count_characters(grocery_list):
    if not grocery_list:
        return 0
    else:
        return len(grocery_list[0]) + count_characters(grocery_list[1:])
print("Total characters in items:", count_characters(items))
       
  


