from object import exam
Questions =  ["1. Is set of Real Numbers countable \n (a) Yes\n(b) No",
              "2. The Wronskian of linearly independent solutins of a differential equaiton is \n (a) zero\n(b) identically zero\n(c) Never zero \n(d) Insufficient Information to conclude anything",
              "3. A differentiable function is necessarily continuous.\n(a) True\n(b)False",
              "4. What are eigenvalues of Involutionary Matrices?\n(a) 1\n(b) 0\n(c) Undefined\n (d) -1 or 1"]

exampaper=[exam(Questions[0], "b"),
           exam(Questions[1], "b"),
           exam(Questions[2], "a"),
           exam(Questions[3],"d")]

def startexam(paper):
    score=0
    for question in paper:
        a=input(question.Questionprompt + ":\n ")      #Question prompt is the input prompt
        if a==question.answer:
            score+=1
    print("You scored " + str(score) + " /"+ str(len(paper)))        #strings cannot be concatenated with integers

startexam(exampaper)            #call this function to start exam
