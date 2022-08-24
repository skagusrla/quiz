from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizeBrain(question_bank)

while quiz.still_have_question():#퀴즈가 계속 남아있도록 한다.
    quiz.next_question()

print(f"Quiz is end")
print(f"Your final score was : {quiz.score}/{len(quiz.question_list)}")
