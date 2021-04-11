from data import MENU
from data import resources
from data import logo
print(logo)

#function to print report
def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    
#function to check resources
def checkResources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        return "Sorry there is not enough water"
    elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
        return "Sorry there is not enough milk"
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        return "Sorry there is not enough coffee"
    else:
        return 0
    
#function to process coins
def processCoins(quarters, dimes, nickels, pennies):
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    
#function to check transaction successful
def checkTransaction(amount, coffeeType):
    if amount < MENU[coffeeType]['cost']:
        return "Sorry that's not enough money. Money refunded."
    elif amount >= MENU[coffeeType]['cost']:
        print(f"Here is ${round(amount-MENU[coffeeType]['cost'], 2)} in change.")
        resources['money'] += MENU[coffeeType]['cost']
        return 0
    
#function to make coffee
def makeCoffee(coffeeType, amount):
    transactionStatus = checkTransaction(amount, coffeeType)
    resourcesStatus = checkResources(coffeeType)
    if transactionStatus == 0 and resourcesStatus == 0:
        resources['water'] -= MENU[coffeeType]['ingredients']['water']
        resources['milk'] -= MENU[coffeeType]['ingredients']['milk']
        resources['coffee'] -= MENU[coffeeType]['ingredients']['coffee']
        print(f"Here is your {coffeeType} Enjoy!")
    else:
        print(transactionStatus)
        print(resourcesStatus)
        
#function to trigger coffee machine
def startMachine():
    coffeeType = ""
    userInput = ""
    userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    while userInput != "off": 
        if userInput == "espresso":
            coffeeType = userInput
        elif userInput == "latte":
            coffeeType = userInput
        elif userInput == "cappuccino":
            coffeeType = userInput
        elif userInput == "report":
            printReport()
            continue
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickels?: "))
        penny = int(input("How many pennies?: "))
        amount  = processCoins(quarter, dime, nickle, penny)
        makeCoffee(coffeeType, amount)
        userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()
                
startMachine()