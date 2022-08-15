import random



#ask to choose number of rounds
rounds = int(input("Enter number of rounds:\n"))

# creating a list of choices
choices = ['rock', 'paper', 'scissors']

# store scores of both computer and player
comp_score = 0
player_score = 0

while True:
    # Taking player name

    name = input("Enter your name:\n")

    for i in range(rounds):

        print("\nRound "+ str(i+1))
        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("\nEnter your choice (rock, paper, scissors):\n").lower()

        if player == "rock":
            if computer == "paper":
                print("Computer: " + computer)
                print(name +": "+ player)
                print("Computer Wins!")
                comp_score +=1
                print("-----Scores-----")
                print("Computer: "+ str(comp_score) + " || "+ name +": " + str(player_score))
            elif computer == "scissors":
                print("Computer: " + computer)
                print(name +": " + player)
                print(name +" Wins!")
                player_score += 1
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
            elif computer == "rock":
                print("Computer: " + computer)
                print(name +": " + player)
                print("Tie!")
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
        elif player == "paper":
            if computer == "paper":
                print("Computer: " + computer)
                print(name +": " + player)
                print("Tie!")
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
            elif computer == "scissors":
                print("Computer: " + computer)
                print(name +": " + player)
                print("Computer Wins!")
                comp_score += 1
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
            elif computer == "rock":
                print("Computer: " + computer)
                print(name +": " + player)
                print(name +" Wins!")
                player_score += 1
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
        elif player == "scissors":
            if computer == "paper":
                print("Computer: " + computer)
                print(name +": " + player)
                print(name +" Wins!")
                player_score += 1
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
            elif computer == "scissors":
                print("Computer: " + computer)
                print(name +": " + player)
                print("Tie!")
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))
            elif computer == "rock":
                print("Computer: " + computer)
                print(name +": " + player)
                print("Computer Wins!")
                comp_score += 1
                print("-----Scores-----")
                print("Computer: " + str(comp_score) + " || " + name +": " + str(player_score))


    #Show final score and winner
    print("--------------------------------------------------------------")
    if player_score>comp_score:
        print(name.upper() +" WON!! :)")
    elif comp_score>player_score:
        print("YOU LOSE!! :(")
    else:
        print("IT'S A TIE!! XD")
    print("--------------------------------------------------------------")
    continue_game = input("Do you wish to play again? (yes/no)").lower()

    if continue_game != "yes":
        break;