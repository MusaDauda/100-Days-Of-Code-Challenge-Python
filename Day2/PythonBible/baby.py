from random import choice

questions = [
    "Why is 1 = 1?: ", "Why is the sky blue?: ", "How many stars in our galaxy?: "]
question_to_ask = choice(questions)
answer = input(question_to_ask).strip().lower()
while answer != "just because":
    answer = input("Why?: ")
print("Oh.. Okay!")
