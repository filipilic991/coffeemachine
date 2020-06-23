
'''
#V3_4 NO OOP
# current supplies
money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9
action = ""


def remaining():
    print("\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money".format(
        water, milk, coffee_beans, cups, money))


def write_action():
    global action
    print("\nWrite action (buy, fill, take, remaining, exit):")
    action = input()


def buy():
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    buy_type = input()
    global water, milk, coffee_beans, cups, money
    if buy_type == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif coffee_beans < 16:
            print("Sorry, not enough coffee!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee_beans -= 16
            money += 4
            cups -= 1
    elif buy_type == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif coffee_beans < 20:
            print("Sorry, not enough coffee!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            cups -= 1
    elif buy_type == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif coffee_beans < 12:
            print("Sorry, not enough coffee!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            cups -= 1
    elif buy_type == "back":
        return


def fill():
    global water, milk, coffee_beans, cups, money
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())


def take():
    global money
    print("I gave you ${}".format(money))
    money = 0


program_is_running = True
while program_is_running:
    write_action()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        program_is_running = False
'''

''' V2
# Write your code here
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups_of_coffee = int(input())
residue = int(min(water/200, milk/50, beans/15))
print(residue)

if (water < 200 or milk < 50 or beans < 15) and cups_of_coffee > 0:
    print("No, I can only make 0 cups of coffee")
elif cups_of_coffee <= residue:
    if cups_of_coffee == int(residue):
        print("Yes, I can make that amount of coffee")
    elif cups_of_coffee == 0 or residue / cups_of_coffee > 1:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(int(residue - cups_of_coffee)))
elif cups_of_coffee > residue:
    print("No, I can only make {} cups of coFFee".format(int(residue)))


#print("Yes, I can make that amount of coffee and even {} more than that".format(residue-cups_of_coffee))
'''


''' V1
print("Write how many cups of coffee you will need:")
cups_of_coffee = int(input())
water = 200 * cups_of_coffee
milk = 50 * cups_of_coffee
beans = 15 * cups_of_coffee
print("For {} cups of coffee you will need:\n{} ml of water\n{} ml of milk\n{} g of coffee beans".format(cups_of_coffee,
water, milk, beans))
starting = "Starting to make a coffee"
grinding = "Grinding coffee beans"
boiling = "Boiling water"
mixing = "Mixing boiled water with crushed coffee beans"
pouring_coffee = "Pouring coffee into the cup"
pouring_milk = "Pouring some milk into the cup"
ready = "Coffee is ready!"
print(starting)
print(grinding)
print(boiling)
print(mixing)
print(pouring_coffee)
print(pouring_milk)
print(ready)'''