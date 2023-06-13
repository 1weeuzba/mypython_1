def new_game():

    guesses=[]    
    correct_guesses=0
    questions_number=1

    for key in questions:
        print("_______________________________________________________________________________________________")
        print(key)
        for i in options[questions_number-1]:
            print(i)
        guess=input("Enter (A,B,C,D): ")
        guess= guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)

        questions_number += 1

    display_score(correct_guesses,guesses)

#-----------------------------
def check_answer(answer,guess):

    if answer==guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#-----------------------------
def display_score(correct_guesses,guesses):
    print("______________________________")
    print("Results")
    print("______________________________")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)

    print("Your scored "+str(score)+"%")

    
#-----------------------------
def play_again():
    response = input('Do you want to play again?(yes/no): ').upper()
    if response =="YES":
        return True
    else:
        return False
    
questions = {"In which Italian city can you find the Colosseum?":"B",
             "What is the largest canyon in the world?":"C",
             "What is the largest active volcano in the world?":"C",
             "In which museum can you find Leonardo Da Vinci’s Mona Lisa?":"A"
             }
options=[["A.Venice","B.Rome","C.Naples","D.Milan"],
         ["A.Verdon Gorge, France","B.King’s Canyon, Australia","C.Grand Canyon, USA","D.Fjaðrárgljúfur Canyon, Iceland"],
         ["A.Mount Etna","B.Mount Vesuvius","C.Mouna Loa","D.Mount Batur"],
         ["A.Le Louvre","B.Uffizi Museum","C.British Museum","D.Metropolitan Museum of Art"]
         ]
new_game()
while play_again():
    new_game()
print("Thanks for playing!")
    



