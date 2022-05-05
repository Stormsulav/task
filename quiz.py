def new_game():

    guesses = []
    correct_guesses = 0
    question_number = 1
    
    for key in questions:
        print("...........")
        print(key)
        for i in options[question_number - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1
    
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 10
    else:
        print("Incorrect!")
        return -5

def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    
    print("Answers:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = correct_guesses
    print("Congartulations! Your Score is:", score)

def play_again():
    
    response = input("Would you like to play again? (Y/N): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False       

# questions in dictionary format as we need key value pairs 
questions = {
    "Who is the first president of the Nepal?": "A",
    "What is the name of the capital city of France?": "C",
    "What is the name of the capital city of Nepal?": "B",
    "Who created Python?": "A",
    "Who is the current president of the USA?": "B",
    "Who is the current president of the Nepal?": "C",
    "What is the name of the capital city of USA?": "A",
    "Who created C++?": "D",
    "Who won the 2018 Football World Cup?": "C",
    "What is the name of the capital city of Germany?": "B",
    }

options = [[ "A. Dr Ram Baran Yadav", "B. Bidhya Devi Bhandari", "C. Bhimsen Thapa", "D. Jung Bahadur Rana" ],
           [ "A. Delhi", "B. London", "C. Paris", "D. Tokyo" ],
           [ "A. Dharan", "B. Kathmandu", "C. Pokahara", "D. Pokhara" ],
           [ "A. Guido van Rossum", "B. Bill Gates", "C. Steve Jobs", "D. Linus Torvalds" ],
           [ "A. Barack Obama", "B. Joe Biden", "C. George W Bush", "D. Donald Trump" ],
           [ "A. Bhimsen Thapa", "B. Dr Ram Baran Yadav", "C. Bidhya Devi Bhandari", "D. Bhimsen Thapa" ],
           [ "A. New York", "B. London", "C. Washington DC", "D. Tokyo" ],
           [ "A. Bill Gates", "B. Guido van Rossum", "C. Steve Jobs", "D. Bjarne Stroustrup" ],
           [ "A. Brazil", "B. Germany", "C. France", "D. Russia" ],
           [ "A. Kathmandu", "B. Berlin", "C. Munich", "D. Frankfurt" ],]

new_game()
# for playing again
while play_again():
    new_game()

print("Thanks for playing!")