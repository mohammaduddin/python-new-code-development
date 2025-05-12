# shopping list manager functionality

shopping_list = []

while True:
    item = input("enter an item to add to the shopping list"   " "
                 "type 'done' when adding items are completed: ")
    if item.lower()=='done':
        break
    shopping_list.append(item)

if shopping_list:
    print(f"your shopping list:")
    for i, item in enumerate(shopping_list):
        print(f"{i+1}). {item}")
else:
    print("Your shopping list is empty")

# OUTPUT:
# your shopping list:
# 1). Bread
# 2). Egg
# 3). Banana
# 4). Bread
# 5). Coffee