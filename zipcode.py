from banner import banner
banner("Zip Code Sorter" , "By Dylan Seidletz")
play_again = "yes" or "no"

# areas for zips
area_codes = ["Bitely", "Brohman", "Croton", "Fremont", "Grant", "Newaygo", "White Cloud"]
zip_codes = ["49309", "49312", "49337", "49412", "49413", "49327", "49349"]
while play_again == 'yes':
player_choice = input("Please enter a zip code:")
    if player_choice == zip_codes[0]:
        print("The zip code 49309 is for Bitely")
        play_again = input("Want to play again(yes/no): ")
    elif player_choice == zip_codes[1]:
        print("The zip code 49312 is for Brohman")
        play_again = input("Want to play again(yes/no): ")
    elif player_choice == zip_codes[2]:
        print("The zip code 49337 is for Croton and Newaygo")
        play_again = input("Want to play again(yes/no): ")
    elif player_choice == zip_codes[3]:
        print("The zip code 49412 is for Fremont")
        play_again = input("Want to play again(yes/no): ")
    if player_choice == zip_codes[4]:
        print("The zip code 49413 is for Fremont")
        play_again = input("Want to play again(yes/no): ")
    if player_choice == zip_codes[5]:
        print("The zip code 49327 is for Grant")
        play_again = input("Want to play again(yes/no): ")
    if player_choice == zip_codes[6]:
        print("The zip code 49349 is for White Cloud")
        play_again = input("Want to play again(yes/no): ")
    else :
        print("That zip code is not in Newaygo County, try again.")

while play_again == "no":
    print("Thank you for using the newaygo county Zip Code Sorter. Goodbye!")
