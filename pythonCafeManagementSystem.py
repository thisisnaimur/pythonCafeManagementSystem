# code by rahat 
a = "Restaurant"
menu = {
    "Pizza": 40,
    "Burger": 50,
    "Lacci": 30,
    "Salad": 20,
    "Coffee": 10,
    "Tea": 5,
    "Nan": 40,
    "Ice-creem": 100,
}

#Greet
print("Welcome to Python Program by Rahat")
print("Pizza:     Rs40$\nBurger:    Rs50$\nLacci:     Rs30$\nSalad:     Rs20$\nCoffee:    Rs10$\nTea:       Rs5$\nNan:       Rs40$\nIce-creem: Rs100$\n")

orderTotal = 0

item_1 = input("Enter the name of item you want to order : ").capitalize()
if item_1 in menu:
    orderTotal += menu[item_1]
    print(f"Your order item price is {orderTotal}$")
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available in {a} yet!")

anotherOrder = input("Do You want to add another item? (Yes/No)").capitalize()
if anotherOrder == "Yes":
    item_2 = input("Enter second item :").capitalize()
    if item_2 in menu:
        orderTotal += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avaialable!")

print(f"The total amount of items is {orderTotal}$")