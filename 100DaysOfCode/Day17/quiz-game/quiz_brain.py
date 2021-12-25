class QuizBrain():
    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.score=0

    def still_have_question(self):
        if(self.question_number>len(self.question_list)-1):
            return False
        return True

    def next_question(self):
        inp=input(f"Q {(self.question_number)+1}: {self.question_list[self.question_number].text}? True/False  ")
        self.check_answer(self.question_list[self.question_number].answer,inp)
        self.question_number+=1


    def check_answer(self,correct,user):
        if (correct.lower()==user.lower()):
            print("Well done")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number+1}")
        else:
            print("Oops! Wrong answer")
            print(f"The correct answer is {correct}")
            print(f"Your current score is {self.score}/{self.question_number+1}")
        print("\n")




