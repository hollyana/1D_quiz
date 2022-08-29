# Version 5
# Final version

# Generates random number generator
import random

#------------------------------------------------------------------------
# Validation for answer input
#------------------------------------------------------------------------

# A function to run velidation on answer input
def get_single_input():

        '''
           Checks user answer
           asks to re-enter if doesn't work 
           returns user input
        '''

        # When validation is working
        get_input = True
        while get_input == True:

            # Asks user to input answer to dictionary question    
            user_input = input("Please enter your answer:  ")

            # Makes input lowercase and removes any spaces    
            user_input = user_input.lower()
            user_input = user_input.strip()

            # Asks user to re enter input as it is too many letters
            if len(user_input) != 1:
                print("You can only enter one letter")
                continue
            # Asks user to re enter input as it isn't a correct letter     
            elif user_input not in ["a", "b", "c", "d"]:
                print("You have not entered a, b, c or d")
                continue

            # Ends loop    
            get_input = False

            # Prints user input    
            return user_input

#------------------------------------------------------------------------
# Validation for name input
#------------------------------------------------------------------------

# A function to run velidation on name input
def get_user_name():

    '''
       Checks user name input
       checks number of letters
       returns user name
    '''

    # When validation is working
    get_user_name = True
    while get_user_name == True:

        # Asks for users name   
        user_name = input("Please enter your name:  ")
        user_name = user_name.title()

        # Asks user to re enter as input was too long
        if len(user_name) > 25:
            print("Your name is too long")
            continue

        # Asks user to re enter as input was too short
        elif len(user_name) < 2:
            print("Sorry your name is too short")
            continue

        # Prints user name
        else:
            # all good here
            return user_name

        # Ends loop
        get_user_name = False

#------------------------------------------------------------------------
# Validation for play again input
#------------------------------------------------------------------------

# A function to run validation on play again input
def get_play_again():

    '''
       Checks play again input
       checks length and correct letters
       returns input
    '''

    # When validation is working
    play_again = True
    while play_again == True:

        # Asks for play again input    
        again = input("Do you want to play again y or n:  ")
        again = again.lower()
        again = again.strip()

        # Asks user to re enter as input is an incorrect letter
        if again not in ["y", "n"]:
            print("You have not entered y or n")
            continue
        
        # Asks user to re enter as input is too long
        elif len(again) != 1:
            print("You haven't entered y or n")
            continue

        # Prints play again code
        else:
                return again
        
# Ends loop
play_again = False

#------------------------------------------------------------------------
# Validation for amount of questions
#------------------------------------------------------------------------

# A function to run validation on amount of questions
def get_num_question():

    '''
       Checks amount of questions input
       checks if they are numbers and between 1 and 10
       returns input
    '''

    # When validation is working
    num_question = True
    while num_question == True:

        # Prints out question for input 
        try:
                question = int(input("Between 1-10 how many questions do you want to answer?  "))

        # Asks to re enter as user didn't enter a whole number
        except ValueError:
                print("You have not entered a whole number")
                continue

        # Asks to re enter as user didn't enter a number between 1 and 10
        if question < 1 or question > 10:
                print("You have not entered a number between 1 and 10")
                continue

        # Ends loop
        num_question = False

    # Prints how many question input   
    return question    

#------------------------------------------------------------------------
# Question printing function
#------------------------------------------------------------------------

# A function to run a question take a dictionary as an argument
def run_a_question(Q):

        '''
           Takes the question dictionary
           checks user responce
           returns none
        '''

        # Gets 'score' from loop
        global score

        # Prints question from dictionary
        print(Q["Question"])
        print("-"*70)

        # Printing out the options for answers from dictionary
        for x, y in Q.items():
            if x in ["a", "b", "c", "d"]:
                print("{} . {}".format(x,y))
        print("-"*70)

        # Getting input for answer from validation code
        answer_1 = get_single_input()

        # Getting the validation to check answer and
        # make sure it matches the dictionaries answer
        # Prints if you get it correcy
        if answer_1 == Q["answer"]:
            print("-"*70)
            print("Correct great job")
            print("-"*70)
            # Adds one to global score if answer correct 
            score += 1
        # Prints worng answer with statement
        else:
            print("-"*70)
            print("Sorry you are wrong, better luck next time the answer is {}".format(Q["answer"]))
            print("-"*70)



#------------------------------------------------------------------------
# Questions
#------------------------------------------------------------------------

# Dictionary with questions, options and the answer that the function reads
question_1 = {
            "Question" : "What day was One Direction formed?",
            "a" : "August 23, 2010",
            "b" : "July 23, 2010",
            "c" : "September 10, 2009",
            "d" : "July 1, 2010",
            "answer" : "b"
}

question_2 = {
            "Question" : "Which two One Direction members have the same tattoo?",
            "a" : "Harry & Zayn",
            "b" : "Louis & Zayn",
            "c" : "Liam & Zayn",
            "d" : "Louis & Liam",
            "answer" : "b"
}

question_3 = {
            "Question" : "Which guest judge suggested the idea of forming the band?",
            "a" : "Geri Halliwell",
            "b" : "Natalie Imbruglia",
            "c" : "Katy Perry",
            "d" : "Nicole Scherzinger",
            "answer" : "d"
}

question_4 = {
            "Question" : "How many teen choice awards has One Direction won?",
            "a" : "26",
            "b" : "19",
            "c" : "28",
            "d" : "32",
            "answer" : "c"
}

question_5 = {
            "Question" : "Which 1D member was part of a band called The Rogue?",
            "a" : "Louis",
            "b" : "Harry",
            "c" : "Zayn",
            "d" : "Niall",
            "answer" : "a"
}

question_6 = {
            "Question" : "Who was the first member to release a solo album?",
            "a" : "Harry",
            "b" : "Zayn",
            "c" : "Liam",
            "d" : "Niall",
            "answer" : "b"
}

question_7 = {
            "Question" : "Which two members have a solo song with the same title?",
            "a" : "Louis & Zayn",
            "b" : "Louis & Liam",
            "c" : "Harry & Zayn",
            "d" : "Louis & Niall",
            "answer" : "c",
}

question_8 = {
            "Question" : "At which stadium did the boys film a concert film during the ‘where we are tour’?",
            "a" : "Croke Park",
            "b" : "San Siro",
            "c" : "Wembly",
            "d" : "Stade de France",
            "answer" : "b"
}

question_9 = {
            "Question" : "One Way Or Another (Teenage Kicks) was recorded for what charity?",
            "a" : "Comic Relief",
            "b" : "WWF",
            "c" : "LGBT Foundation - UK",
            "d" : "Women's Aid - UK",
            "answer" : "a"
}

question_10 = {
            "Question" : "Which member hosts the ‘Away From Home Festival’ every year?",
            "a" : "Liam",
            "b" : "Niall",
            "c" : "Harry",
            "d" : "Louis",
            "answer" : "d"
}

#------------------------------------------------------------------------
# Instructions
#------------------------------------------------------------------------

print("="*70)

# Asking for users name
user_name = get_user_name()

# Printing instructions
print("-"*70)
print("Hi {} welcome to this One Direction quiz game!".format(user_name))

# Asking user how many questions they want to answer
number_questions = get_num_question()

# Instructions on how to play 
print("This quiz has different questions that you have to answer")
print("they are all multi choice so when you are asked for your answer")
print("you put the letter beside it not the full name")
print("Good luck")
print("-"*70)

# Starting game
start = input("Press enter to start:  ")
print("="*70)

#------------------------------------------------------------------------
# List to run questions
#------------------------------------------------------------------------

# List that runs the game questions from the dictionary
game_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

# Randomises my list of game questions
random.shuffle(game_questions)

#------------------------------------------------------------------------
# Start of loop 
#------------------------------------------------------------------------

# Starting the replay loop
start = "y"
while start == "y":
        
    # Vairable to count the score    
    score = 0          

    # Vairable to count the number of questions to answer    
    counter = 0    
    while counter < number_questions:
        run_a_question(game_questions[counter])

        counter += 1

    # Prints final score    
    print("Your final score was {}/{}!".format(score, number_questions))


    # Linking to play again validation 
    start = get_play_again()

# Out of loop end of game
print("")
print("Game over")



