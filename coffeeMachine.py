from data import MENU
from data import resources

#function to print report
def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    

#function to check resources
def checkResources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water")
    elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
        print("Sorry there is not enough milk")
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
    else:
        return 0
    
#function to process coins
def processCoins(quarters, dimes, nickels, pennies):
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    
#function to check transaction successful
def checkTransaction(amount, coffeeType):
    if amount < MENU[coffeeType]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        exit
    elif amount >= MENU[coffeeType]['cost']:
        print(f"Here is ${amount-MENU[coffeeType]['cost']} in change.")
        resources['money'] += MENU[coffeeType]['cost']
    

#function to make coffee
def makeCoffee(coffeeType):
    resources['water'] -= MENU[coffeeType]['ingredients']['water']
    resources['milk'] -= MENU[coffeeType]['ingredients']['milk']
    resources['coffee'] -= MENU[coffeeType]['ingredients']['coffee']

#function to trigger coffee machine
def startMachine():
    coffeeType = ""
    userInput = ""
    while userInput != "off":
        userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
        if userInput == "espresso":
            coffeeType = userInput
        elif userInput == "latte":
            coffeeType = userInput
        elif userInput == "cappuccino":
            coffeeType = userInput
        elif userInput == "report":
            printReport()
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickels?: "))
        penny = int(input("How many pennies?: "))
        amount  = processCoins(quarter, dime, nickle, penny)
        checkTransaction(amount, coffeeType)
        print(f"Here is your {coffeeType} Enjoy!")

        
startMachine()
    