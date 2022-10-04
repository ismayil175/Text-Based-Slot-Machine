import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count= {
    "A": 2, #how many letter should consist in the final, to assign we can simply write number next to letter
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value= {
    "A": 5, #how many letter should consist in the final, to assign we can simply write number next to letter
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines




def get_slot_machine_spin(rows,cols,symbols):
    #basically this will put the words to our array
    all_symbols = [] 
    for symbol, symbol_count in symbols.items(): #The view object contains the key-value pairs of the dictionary,so we can decide which we need to put our array
        for _ in range(symbol_count): 
            all_symbols.append(symbol) #this will put only letters to all_symbols array

    #what values will go in every single column and row 
            
    columns = []
    for _ in range(cols):

        column = []
        current_symbols = all_symbols[:] #[:] creates a copy of the original sequence
        for _ in range(rows):
            value = random.choice(current_symbols) #auto will choice number from the list
            current_symbols.remove(value)#The chosen value will be deleted not to get same value again
            column.append(value) #this will add every row for specific column
        columns.append(column) #final result of all column will be added to final one. using last columns, we can print our letters
    
    return columns 


def print_slot_machine(columns):
    for row in range(len(columns[0])):#is one less than the number of columns.
        for i, column in enumerate(columns): #using enumerate we can count how many of there are
            if i != len(columns) -1:  #thanks to -1 it wont put "|" to end 
                print(column[row], end=" | ") #this will basically put | between rows, D|D
            else:
                print(column[row], end="")  #this will basically put nothing beacuse in if statment its wanted to -1 
        print()


def deposit(): #collecting user input that gets the deposit from the user 
    while True: #the reason for while is, we will be asking the money until user enters valid amount
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit(): #this function determines if this number is valid
            amount = int(amount) 
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between{MIN_BET} - {MAX_BET}') #we assign MIN_BET and MAX_BET in the beganing so we do not have to assign 
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
        

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()