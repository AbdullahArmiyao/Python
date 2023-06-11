from quiz1 import question 

question_prompt = [
    "What color are Apples?\n(a)Red/Green\n(b)purple\n(c)Orange\n\n", 
    "What color are Oranges?\n(a)Red/Green\n(b)purple\n(c)Orange\n\n", 
    "What color are Eggplants?\n(a)Red/Green\n(b)purple\n(c)Orange\n\n"
]
questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b"),
]


        

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
            