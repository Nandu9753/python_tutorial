import random,sys
def get_choices():
    player_choice = input("Enter a choice (rock,scissor,paper):")
    lst = ["scissor","rock","paper"]
    computer_choice = random.choice(lst)
    choice = {"player_choice":player_choice,"computer_choice":computer_choice}
    return choice
    
def check_win(player_choice,computer_choice):
    if(player_choice == computer_choice):
        return "Its a tie!s"
    elif player_choice == "rock":
        if(computer_choice=="scissor"):
            return "You are Win"
        else:
            return "You are lose"
    elif player_choice == "paper":
        if(computer_choice=="rock"):
            return "You are Win"
        else:
            return "You are lose"
    elif player_choice == "scissor":
        if(computer_choice=="paper"):
            return "You are Win"
        else:
            return "You are lose"   
    else:
        return "Input Not Correct"     
            
menu = '''
---------------------- Welcome To The Game ----------------------
Please Select Option :
1. Start Game
2. Exit
'''
while(True):
    print(menu)
    menuOption = input("Enter a Option:")
    if menuOption == "1":
        request  = get_choices()
        response = check_win(request['player_choice'],request['computer_choice'])
        print(response)
    elif menuOption == "2":
        sys.exit()
    else:
        print("Please Put Correct Option")