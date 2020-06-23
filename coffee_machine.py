#V5 OOP
class Coffee_Machine:


    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.action = ""


    def remaining(self):
        print(
            "\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money".format(
                self.water, self.milk, self.coffee_beans, self.cups, self.money))


    def write_action(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")
        self.input_method()


    def input_method(self):
        self.inputstring = input()


    def buy(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.input_method()
        buy_type = self.inputstring
        if buy_type == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.cups -= 1
        elif buy_type == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.cups -= 1
        elif buy_type == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.cups -= 1
        elif buy_type == "back":
            return


    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


mycoffee = Coffee_Machine()

program_is_running = True
while program_is_running:
    mycoffee.write_action()
    if mycoffee.inputstring == "buy":
        mycoffee.buy()
    elif mycoffee.inputstring == "fill":
        mycoffee.fill()
    elif mycoffee.inputstring == "take":
        mycoffee.take()
    elif mycoffee.inputstring == "remaining":
        mycoffee.remaining()
    elif mycoffee.inputstring == "exit":
        program_is_running = False
