import random

#Function to check if player won
def check_game(op, random_variable):
    rules = {
        "rock": {"rock": "tie", "scissors": "wins", "paper": "loses"},
        "paper": {"paper": "tie", "rock": "wins", "scissors": "loses"},
        "scissors": {"scissors": "tie", "paper": "wins", "rock": "loses"}
    }
    
    return rules[op][random_variable]

#Function to return CPU choice
def cpu_choice():
    variables = ["rock", "paper", "scissors"]

    return random.choice(variables).lower()
    
#User input (game option) with verification
while True:
    print("Rock, paper, scissors...")
    op = input("\nChoose your option: ").lower()
    if op in ["rock", "paper", "scissors"]:
        break
    else:
        print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.\n")

print("User Choice: " + op)

#Call function CPU_choice
random_variable = cpu_choice()

print("\nCPU choose " + random_variable)

#Call function check_game
result = check_game(op, random_variable)

#Output match result
match result:
    case "wins":
        print("\nUser wins!")
    case "loses":
        print("\nCPU wins!")
    case _:
        print("\nTie!")
    

