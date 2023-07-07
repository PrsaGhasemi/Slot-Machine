MAX_LINES = 3


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
            if 0 < betAmount <= wholeDeposit:
                betAmount = int(betAmount)
                break
            else: 
                print(f"you can bet between 1$ and {wholeDeposit}$")
        else:
            print("you can only bet with money! enter number")
    return betAmount

def main() :
    userBalance = deposit()
    chosenLines = number_of_lines_toBet()
    betMoney = getBetAmount()
    totalBet = betMoney * chosenLines
    print(f"you are beting {betMoney}$ on {chosenLines} and  your total bet is {totalBet}$")

main()