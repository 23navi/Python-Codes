from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    new_que=Question(i["text"],i["answer"])
    question_bank.append(new_que)

quiz=QuizBrain(question_bank)
while(quiz.still_have_question()):
    quiz.next_question()
print(f"Your final score is {quiz.score}/{len(question_bank)}")