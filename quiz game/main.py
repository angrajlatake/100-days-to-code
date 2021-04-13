from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

continue_game = True
score = 0

while quiz.still_has_questions():
    quiz.next_question()

print(f"\n\n\nYou have completed the quiz. \n Your final score is {quiz.score}/{quiz.question_number}")

# I have to learn to pull the questions from a site and use it anywhere
