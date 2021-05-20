class Quizfun:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.message = None
        self.user_answer = None

    def check_questions_left(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.question_text = f"{self.current_question.text}"

    def check_answer(self):
        if self.user_answer == self.current_question.answer:
            self.score += 1
            self.message = "You got it right!"
        else:
            self.message = "Wrong Answer!"

    def true_button(self):
        self.user_answer = "True"
        self.check_answer()
        self.next_question()

    def false_button(self):
        self.user_answer = "False"
        self.check_answer()
        self.next_question()
