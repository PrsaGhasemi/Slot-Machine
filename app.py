import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def slotMachineGenerator(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        availableSymbols = allSymbols[:]
        for _ in range(rows):
            generatedValue = random.choice(allSymbols)
            availableSymbols.remove(generatedValue)
            column.append(generatedValue)
        columns.append(column)
    return columns

def showGeneratedMachine(columns):
    for row in range(len(columns[0])):
        for i, coloumn in enumerate(columns):
            if i != len(columns) - 1:
                print(coloumn[row], end= " | ")
            else: 
                print(coloumn[row])


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("you should at least deposit the minimum")
        else :
            print("your deposit must be a number")

    return amount

def number_of_lines_toBet():
    while True:
        lines = input("how many lines do you wanna bet on between (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else :
                print("you must chose valid lines!")
        else :
            print("you must enter numbers")

    return lines
            
def getBetAmount():
    while True:
        betAmount = input("how much do you wanna bet on each line? $")
        if betAmount.isdigit():
            betAmount = int(betAmount)
            if MIN_BET < betAmount <= MAX_BET:
                betAmount = int(betAmount)
                break
            else: 
                print(f"you can bet between {MIN_BET}$ and {MAX_BET}$")
        else:
            print("you can only bet with money! enter number")
    return betAmount

def main() :
    userBalance = deposit()
    chosenLines = number_of_lines_toBet()
    while True:
        betMoney = getBetAmount()
        totalBet = betMoney * chosenLines
        if totalBet > userBalance:
            print(f"you can't bet more than what you have, your balance is ${userBalance}")
        else:
            break
    print(f"you are beting {betMoney}$ on {chosenLines} lines and  your total bet is {totalBet}$")

slots = slotMachineGenerator(ROWS, COLS , symbols_count)
kir = showGeneratedMachine(slots)
print(kir)
 
main()