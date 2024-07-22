questions = ("Who developed Python Programming Language: ",
                       "Which type of Programming does Python support?: ",
                       "Is Python code compiled or interpreted?: ",
                       "Which of the following is used to define a block of code in Python language?: ",
                       "Which keyword is used for function in Python language?: ")

options = (("A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"),
                   ("A. object-oriented programming", "B. structured programming", "C. functional programming", "D. all of the mentioned"),
                   ("A. Python code is both compiled and interpreted", "B. Python code is neither compiled nor interpreted", "C. Python code is only compiled", "D. Python code is only interpreted"),
                   ("A. Indentation", "B. Key", "C. Brackets", "D.  All of the mentioned"),
                   ("A. Function", "B. def", "C. Fun", "D. Define"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")