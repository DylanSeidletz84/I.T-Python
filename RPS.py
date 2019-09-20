from banner import banner
banner ("Rock,Paper,Scissors" , " By Dylan Seidletz")
print (" Welcom to a friendly game of Rock, Paper, Sicssors")
print (" The first to win two out of the three rounds gets to be the winner")

the_number = random.randint(1,99)

guess = -1

while guess != the_number:
    guess_text = input("What is your guess? ")
    guess = int(guess_text)

    if guess > 100 or guess < 0:
        print("Please choose a number that is between 0 and 100.")
    elif guess > the_number:
        print(f"Sorry {name}, but your guess is too HIGH. Try again.")
    elif guess < the_number:
        print(f"Sorry {name}, but your guess is too LOW. Try again.")
    else:
        print(f"You guessed it! Congratulations, {name}!")

print("Thanks for playing!")
