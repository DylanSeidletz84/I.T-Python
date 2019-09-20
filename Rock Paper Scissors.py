from random import randint
from banner import banner
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
banner("Let's Play RPS" , "By Dylan Seidletz")

print("We are going to play a friendly game of Rps.")
print("First to win 2 out of 3 wins")
print("")
name = input("What is your name? ")
#create  options
t = ["Rock", "Paper", "Scissors"]

#assign a random player vs. computer
computer = t[randint(0,2)]
play_again = "yes"
player = False
player_score = 0
computer_score = 0

while play_again == "yes":

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score = computer_score + 1
        else:
            print("You win!", player, "smashes", computer)
            player_score = player_score + 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    play_again = input("Want to play again(yes/no): ")
def print_score(p_score, c_score):  # Identifies the result and print the total score
    print("Score:""\nPlayer:", p_score, "\nComputer:", c_score)

    #player = false makes game loop
    player = True
    computer = t[randint(0,2)]
from banner import banner
