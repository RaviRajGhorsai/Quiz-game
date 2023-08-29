
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for que in questions:
        print("------------------------")
        print(que)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(que), guess)
        question_num += 1

    display_score(correct_guesses,guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT! ")
        return 1
    else:
        print("INCORRECT!!")
        return 0


def display_score(correct_guesses, guesses):
    print("RESULTS")
    print("------------------------")
    print("Answers: ")
    for i in questions:
        print(questions.get(i), end=" ")

    print("\nGuesses: ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():

    end = input("Play again? (Y/N): ")
    end = end.upper()
    if end == 'Y':
        return True
    else:
        return False


questions = {
    "Who created Python?: ": "A",
    "What year was Pyhon created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2003"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. true", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("\nByeee!!")
