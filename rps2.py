from random import randint
from banner import banner

banner("Let's Play RPS" , "By Dylan Seidletz")

print("We are going to play a friendly game of Rps.")
print("First to win 2 out of 3 rounds is the winner")
print("")

#create  options
t = ["Rock", "Paper", "Scissors"]

#assign a random player vs. computer

play_again = "yes"

while play_again == 'yes':
    player_score =  0
    computer_score =  0

    while player_score < 2 and computer_score < 2:
        player_choice = input("Rock, Paper, Scissors?")
        computer = t[randint(0,2)]
        if player_choice == computer:
            print("Tie!")
        elif player_choice.lower() == "rock":
            if computer == "Paper":
                print(f"You lose! {computer} covers {player_choice}")
                computer_score = computer_score + 1
            else:
                print(f"You win! {player_choice} smashes {computer}")
                player_score = player_score + 1
        elif player_choice.lower() == "paper":
            if computer == "Scissors":
                print(f"You lose! {computer} cut {player_choice}")
                computer_score = computer_score + 1
            else:
                print(f"You win! {player_choice} covers {computer}")
                player_score = player_score + 1
        elif player_choice.lower() == "scissors":
            if computer == "Rock":
                print(f"You lose... {computer} smashes {player_choice}")
                computer_score = computer_score + 1
            else:
                print(f"You win! {player_choice} cut {computer}")
                player_score = player_score + 1
        else:
            print("That's not a valid play. Check your spelling!")
        print("Score: Player:",player_score,"Cpu:",computer_score,)

    if player_score == 2:
        print("Good game you've won")
        play_again = input("Want to play again(yes/no): ")
    if computer_score == 2 :
        print( "Good game, Try again")
        play_again = input("Want to play again(yes/no): ")
