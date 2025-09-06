# define the menu of restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'burger' : 60,
     'salad ': 70,
    'coffee' : 80 ,
}

# greet
print("Welcome To Python Restaurant") 
print(" Pizza: Rs 40 \nPasta : Rs 50\n Burger: Rs 60 \n salad: Rs 70\n coffee: Rs 80 ")

order_total = 0
# 80 + 70 = 150 

item_1 = input ("Enter the name of item you want to order = ")
if item_1 in menu:
      order_total += menu[ item_1] 
      print(f"Your item {item_1}has been added to your order") 

else:
      print(f"Your item { item_1} is not avaialable yet!")   

another_order = input("Do you want to add another item ? (Yes/No)")               
if another_order ==  "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
         order_total += menu[item_2]
         print(f"Item{item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!") 

print(f"The total amount of items to pay is {order_total}")             
