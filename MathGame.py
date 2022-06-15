import tkinter as tk
import random

#variables
numAttempted = 0
numCorrect = 0
numIncorrect = 0
questionList = []
numGuesses = 0
numAttempted = 0
answer = None
    
#window
window = None
qframe = None
radioframe = None
entryGuess = None

#buttons
buttonCheck = None
buttonQuit = None
buttonNew = None

#radio buttons
buttonAdd = None
buttonSub = None
buttonMult = None
buttonDiv = None
buttonAny = None
radioValue = 5

#labels
displayCorrect = None
displayIncorrect = None
displayNumQuestion = None
questionLabel = None
promptLabel = None

#methods
qAdd = None
qSub = None
qMult = None
qDiv = None
isNewQuestion = True






def addition():
    global qframe, qAdd, answer, questionList, questionLabel
    
    x = random.randrange(0, 1000)
    y = random.randrange(0, 1000)
    
    while questionSeen([x, y, '+']) == True:
        x = random.randrange(0, 1000)
        y = random.randrange(0, 1000)

    answer = x + y
    questionList.append([x, y, '+'])

    questionLabel = tk.Label(qframe, text = ('{} + {} = ').format(x,y), bg='#ff9999')
    questionLabel.pack(side=tk.LEFT)
    questionLabel.pack()

def subtraction():
    global qframe, qSub, answer, questionList, questionLabel
    
    x = random.randrange(0, 1000)
    y = random.randrange(x, 1000)

    while questionSeen([x, y, '-']) == True:
        x = random.randrange(0, 1000)
        y = random.randrange(x, 1000)

    answer = y - x
    questionList.append([x, y, '-'])

    questionLabel = tk.Label(qframe, text = ('{} - {} = ').format(y, x), bg='#ff9999')
    questionLabel.pack(side=tk.LEFT)
    questionLabel.pack()

def multiplication():
    global qframe, qMult, answer, questionList, questionLabel
    
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)

    while questionSeen([x, y, '*']) == True:
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)        

    questionList.append([x, y, '*'])
    answer = x * y 

    questionLabel = tk.Label(qframe, text = ('{} * {} = ').format(x,y), bg='#ff9999')
    questionLabel.pack(side=tk.LEFT)
    questionLabel.pack()
    
def division():
    global qframe, qDiv, answer, questionList, numerator, denominator, questionLabel
    
    numerator = random.randrange(0, 1000)
    denominator = random.randrange(1, 1000)

    if questionSeen([numerator, denominator, '/']) == False:
        while numerator % denominator != 0:
            numerator = random.randrange(0, 1000)
            denominator = random.randrange(1, 1000)

    while questionSeen([numerator, denominator, '/']) == True:
        while numerator % denominator != 0:
            numerator = random.randrange(0, 1000)
            denominator = random.randrange(1, 1000)
    
    questionList.append([numerator, denominator, '/'])
    answer = int(numerator / denominator)
    
    questionLabel = tk.Label(qframe, text = ('{} / {} = ').format(numerator, denominator), bg='#ff9999')
    questionLabel.pack(side=tk.LEFT)
    questionLabel.pack()
    

def questionSeen(sublist):
    if sublist in questionList:
        return True
    else: 
        return False


def checkAnswer():
    global numCorrect, numIncorrect, displayCorrect, displayNumQuestion, promptLabel, entryGuess, answer, numGuesses
    global numAttempted, isNewQuestion
    
    if isNewQuestion == True:
        numAttempted += 1
        numIncorrect = 0

    isNewQuestion = False

    try:
        guess = int(entryGuess.get())
        
        if  guess == answer: 
            numCorrect += 1
            numGuesses += 1
            entryGuess.configure(state='disabled')
            promptLabel.configure(text='Correct!')
            # solved = True
            
        elif guess != answer:
            numIncorrect += 1
            numGuesses += 1
            entryGuess.delete(0, 'end')
            promptLabel.configure(text='{} Was Incorrect. Try Again'.format(guess))
            # solved = False 
        
    except ValueError:
        entryGuess.delete(0,'end')
        promptLabel.configure(text = 'Please Enter a Valid Integer')
        # solved = False
    
    #labels update
    displayCorrect.configure(text = 'Number of Correct: {}'.format(numCorrect))
    displayIncorrect.configure(text = 'Number of Incorrect Guesses for this Problem: {}'.format(numIncorrect))
    displayNumQuestion.configure(text = 'Number of Questions: {}'.format(numAttempted))

    
#question makers
def makeRandom():
    
    randomOperation = [addition, subtraction, multiplication, division]
    randNum = random.randint(0, len(randomOperation)-1)
    randomOperation[randNum]()

def newQuestion():
    global numAttempted, questionLabel
    global radioValue, isNewQuestion, numIncorrect

    isNewQuestion = True
    numIncorrect = 0 
    displayIncorrect.configure(text = 'Number of Incorrect Guesses for this Problem: {}'.format(numIncorrect))
    
    # numQuestionCounter()

    entryGuess.configure(state='normal')
    entryGuess.delete(0, 'end')
    questionLabel.destroy()
    promptLabel.configure(text = 'Please Enter Your Answer')
    
    if radioValue == 5:
        makeRandom()
    
    if radioValue == 4:
        division()
        
    if radioValue == 3:
        multiplication()
        
    if radioValue == 2:
        subtraction()
        
    if radioValue == 1:
        addition()

def setRadioValue(v):
    global radioValue

    radioValue = v
    newQuestion() 


def quitGame():
    global buttonQuit, numCorrect, numIncorrect
    global numAttempted
    
    window.destroy()

    print('Questions: ', numAttempted)
    print('Solved: ', numCorrect)

    if numCorrect > 0: 
        print('Average Number of Guesses Per Solved Problem: ', int(numGuesses / numCorrect))
    else:
        print('Average Number of Guesses Per Solved Problem Does Not Exist')

def gameWindow():
    global window, qframe, radioframe, buttonCheck, buttonQuit, buttonNew 
    global buttonAdd, buttonSub, buttonMult, buttonDiv, buttonAny
    global displayCorrect, displayIncorrect, displayNumQuestion, promptLabel
    global qAdd, qSub, qMult, qDiv, entryGuess
    global radioValue
    
    
    
    #window
    window = tk.Tk()
    window.title('Math Game')
    window.configure(background = '#ff9999')
        

    #frames
    qframe = tk.Frame(window, bg='#ff9999')
    radioframe = tk.Frame(window, bg='#ff9999')
    
    qframe.pack()
    radioframe.pack(side='left')
    
    #entry text box
    entryGuess = tk.Entry(window)
    entryGuess.pack()
    
    makeRandom()
    
    
    
    #labels
    promptLabel = tk.Label(window, text = 'Please Enter Your Answer', font=('none', 15, 'bold'), bg='#ff9999')
    displayCorrect = tk.Label(window, text = 'Number of Correct: 0', bg='#ff9999')
    displayIncorrect = tk.Label(window, text = 'Number of Incorrect Guesses for this Problem: 0', bg='#ff9999')
    displayNumQuestion = tk.Label(window, text = 'Number of Questions: 0', bg='#ff9999')
    
    promptLabel.pack()
    displayCorrect.pack()
    displayIncorrect.pack()
    displayNumQuestion.pack()
    

    #radio buttons
    var = tk.IntVar()
    var.set(5) #purely for appearance 
    radioValue = 5
    
    buttonAdd = tk.Radiobutton(radioframe, text = '+', variable = var, value = 1, bg='#ff9999', command=lambda: setRadioValue(1))
    buttonSub = tk.Radiobutton(radioframe, text = '-', variable = var, value = 2, bg='#ff9999', command=lambda: setRadioValue(2))
    buttonMult = tk.Radiobutton(radioframe, text = '*', variable = var, value = 3, bg='#ff9999', command=lambda:setRadioValue(3))
    buttonDiv = tk.Radiobutton(radioframe, text = '/', variable = var, value = 4, bg='#ff9999', command=lambda: setRadioValue(4))
    buttonAny = tk.Radiobutton(radioframe, text = 'Any', variable = var, value = 5, bg='#ff9999', command=lambda: setRadioValue(5))

    buttonAdd.pack()
    buttonSub.pack()
    buttonMult.pack()
    buttonDiv.pack()
    buttonAny.pack()
    

    #buttons
    buttonCheck = tk.Button(window, text = 'Check', highlightbackground='#ff9999', command = checkAnswer)
    buttonNew = tk.Button(window, text="New Question", highlightbackground='#ff9999', command = newQuestion)
    buttonQuit = tk.Button(window, text="Quit", highlightbackground='#ff9999', command = quitGame)
    
    buttonCheck.pack()
    buttonNew.pack()
    buttonQuit.pack()
    
    window.mainloop()


gameWindow()