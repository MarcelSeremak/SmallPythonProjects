import tkinter
from equations import Equations
from score import Score

tk=tkinter.Tk()
with open("ranking.txt","r")as data:
    for person in data:
        name=person.split()[0]
        sc=person.split()[1]

tk.wm_title("Math app")
tk.wm_minsize(width=300, height=300)
tk.config(width=300, height=300, bg="#F2AFA0")
gameIsOn = True
score=Score()

def GameOver():
    for widget in tk.winfo_children():
        widget.destroy()
    end=tkinter.Canvas(tk, width=300, height=80, bg="#F2AFA0")
    if score.score>int(sc):

        def conf():
            file=open("ranking.txt","w")
            file.write(f"{inp.get()} {score.score}")
            file.close()
            tk.destroy()
        end.create_text(150, 20, text=f"Your Score is: {score.score}", font=('Trebuchet 15 bold'))
        end.pack()
        inp=tkinter.Entry()
        inp.pack()
        conf=tkinter.Button(text="Confirm", command=conf)
        conf.pack()
    else:
        end.create_text(150, 20, text=f"Your Score is: {score.score}", font=('Trebuchet 15 bold'))
        end.create_text(150, 60, text=f"Record holder: {person}", font=('Trebuchet 10 bold'))


    end.pack()
def buttonClicked(mode):

    eq = Equations(mode)

    
    for widget in tk.winfo_children():
        widget.destroy()

    def checkData():
        try:
            if int(eq.result)==int(entry.get()):
                score.addScore()
        except Exception:
            pass
        buttonClicked(mode)
    if score.score==0:
        tk.after(15000,func=GameOver)
    eqText = tkinter.Canvas()
    eqText=tkinter.Canvas(tk, width=300, height=80, bg="#F2AFA0")
    eqText.create_text(150, 20, text=eq.pickEq(), font=('Trebuchet 15 bold'))
    eqText.create_text(150, 50, text=f"Score: {str(score.score)}", font=('Trebuchet 10 bold'))
    eqText.grid(row=0,column=0, pady=50)

    entry=tkinter.Entry()
    entry.grid(row=1, column=0 , pady=30)
    entry.focus_set()
    confirm = tkinter.Button(text="Confirm", padx=100, command=checkData)
    confirm.grid(row=2, column=0, pady=30)




def easyButton():
    mode = "easy"
    buttonClicked(mode)

def mediumButton():
    mode = "medium"
    buttonClicked(mode)

def hardButton():
    mode = "hard"
    buttonClicked(mode)

cv=tkinter.Canvas(tk, width=300, height=50, bg="#F2AFA0")
cv.create_text(150, 20, text="Choose your difficulty", font=('Trebuchet 15 bold'))
cv.grid(row=0,column=0, pady=20)

difficultyEasy = tkinter.Button(text = "Easy",padx=80, pady=10, command=easyButton)
difficultyEasy.grid(row=1,column=0,pady=20)

difficultyMedium = tkinter.Button(text = "Medium",padx=70, pady=10, command=mediumButton)
difficultyMedium.grid(row=2,column=0,pady=20)

difficultyHard = tkinter.Button(text = "Hard",padx=80, pady=10, command=hardButton)
difficultyHard.grid(row=3,column=0,pady=20)


tk.mainloop()

