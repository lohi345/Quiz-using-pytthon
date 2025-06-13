from Quiz_database import question_bank
from Quiz_database import options
print("***************")
print("Welcome to my Quiz!!!")


score=0
def check_answers(User_guess, correct_answer ):
    if User_guess==correct_answer:
        return True 
    else:
        return False
    
for question_num in range(len(question_bank)):
    print("******************") 
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answers(guess,question_bank[question_num]["answer"])
    if is_correct:
       print("Correct answer")
       score+=1
    else:
      print("Incorrect answer")
      print(f"The correct answer is {question_bank [question_num] ['answer']}")
    print(f"Your Current score is {score}/{question_num+1}")
print(f"You have given {score} correct answer")
print(f"Your score is {(score/len(question_bank))*100 }%")
 