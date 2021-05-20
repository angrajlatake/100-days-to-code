import requests
from question_model import Question
import html
response = requests.get("https://opentdb.com/api.php?amount=20&category=11&difficulty=easy&type=boolean")

data = response.json()

results = data["results"]

question_bank = []
for n in results:
    question = html.unescape(n["question"])
    answer = n ["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)
