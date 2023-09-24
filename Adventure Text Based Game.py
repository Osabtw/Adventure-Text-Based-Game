# Entry Prompts
name = input('Enter Your Name! ')
pronoun = input('Preferred Pronoun! ')
print(f'Welcome {name}!')
start = input(" Would you rather play The Game of Love or Perish? ")
if start == 'play':
    print('Great! Follow me!')
    setting = input('London or New York? ')
else:
    print('My hands are Tied: Now your watch has ended!')
    quit()

#London officially starts
if setting == 'London':
    print('Welcome to the Lands of Royals and Brexit! You will be going on a blind date with Meave to officially start The Game of Love!.... ')
    response = input('You get to pick the Restaurant for the first date.... Fine Dining or Casual?! ')
    if response == 'Fine Dining':
        print(f'We are going to La Dame de Pic London where you and Meave will have an hour to eat and ask each other 20 questions about each other in hopes of falling in love - Have fun {name}')
        response = input(f"Host: We will now watch as {name} embarks on his date will Meave. We will have a check in at the end of the date with {name} hoping for {pronoun}\'s thoughts ")
        response = input("Have you concluded the date, Yes or No")
        #Date Concluded
        if response == "Yes":
            print(f"Host: You seemed to be smiling throughout the date. {name}, would you say the date went well? - Yes or No")
            if response == "Yes":
                print("Hopefully you and Maeve have exchanged numbers; It is nice to see the show fufilling it\'s purpose. ")
                response = input("Thank you for playing Play The Game of Love or Perish; until next time! ")
                quit()
        elif response == "No":
            print("Host: Not the outcome neither you or i wished for but hope you can stay another day in London to get some good memories. ")
            response = input("Thank you for playing Play The Game of Love or Perish; until next time! ")
            quit()
        else:
            print("You\'ve gotten yourself banished! ")
            
    elif response == 'Casual':
        print(f'We are going to Nandos where you and Meave will have an hour to eat and ask each other 20 questions about each other in hopes of falling in love - Have fun {name}')
        response = input(f"Host: We will now watch as {name} embarks on his date will Meave. We will have a check in at the end of the date with {name} hoping for {pronoun}\'s thoughts ")
        response = input("Have you concluded the date, Yes or No ")
        #Date Concluded
        if response == "Yes":
            print(f"Host: You seemed to be smiling throughout the date. {name}, would you say the date went well? - Yes or No")
            if response == "Yes":
                print("Hopefully you and Malia have exchanged numbers; It is nice to see the show fufilling it\'s purpose. ")
                response = input("Thank you for playing Play The Game of Love or Perish; until next time! ")
                quit()
        elif response == "No":
            print("Host: Not the outcome neither you or i wished for but hope you can stay another day in NYC to get some good memories. ")
            response = input("Thank you for playing The Game of Love or Perish; until next time! ")
            quit()
        else:
            print("You\'ve gotten yourself banished! ")
    else:
        print(f'Delusional Manchester United Fan. {pronoun} had to leave!')
        quit()

#New York officially start
# 
elif setting == 'New York':
    print('Welcome to the Big Apple and the land of $1 Pizza! You will be going on a blind date with Malia to officially start The Game of Love!....')
    response = input('Because we are in NYC we have planned a fun date and you get to pick.... - Fun Date or Perish!?')
    if response == 'Fun Date':
        print(f'We are going to Pier 25 - Hudson River Park where you and Malia will have an hour to eat, play and ask each other 20 questions about each other in hopes of falling in love - Have fun {name}' )
        response = input(f"Host: We will now watch as {name} embarks on his date will Meave. We will have a check in at the end of the date with {name} hoping for {pronoun}\'s thoughts ")
        response = input("Have you concluded the date, Yes or No")
        #Date Concluded
        if response == "Yes":
            print(f"Host: You seemed to be smiling throughout the date. {name}, would you say the date went well? - Yes or No")
            if response == "Yes":
                print("Hopefully you and Malia have exchanged numbers; It is nice to see the show fufilling it\'s purpose. ")
                response = input("Thank you for playing Play The Game of Love or Perish; until next time! ")
                quit()
        elif response == "No":
            print("Host: Not the outcome neither you or i wished for but hope you can stay another day in NYC to get some good memories. ")
            response = input("Thank you for playing Play The Game of Love or Perish; until next time! ")
            quit()
        else:
            print("You were so close, Try again next time")
    
#I did it. yay