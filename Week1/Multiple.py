#Create a multiple choice quiz 


#Store the quesions answers and prompts
class Questions:

    def __init__(self, prompt, answer):
        self.prompt = prompt 
        self.answer = answer 
    

#Question prompts
question_prompts =["What color are apples\nred(A)\npurple(B)\npink(C)\n",
           "What color are banana's\nblue(A)\nyellow(B)\nwhite(C)\n",
            "What color are mangos\nred(A)\ngreen(B)\norange(C)\n"]

#Making the list of questions
questions = [
    Questions(question_prompts[0],"a"),
    Questions(question_prompts[1],"b"),
    Questions(question_prompts[2],"c")
]

def run_test(questions):
    score = 0
    for question in questions:
        #Accesses the lists attributes to see if the question correct
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(f"You scored {score}/{len(questions)} correct")

run_test(questions)
