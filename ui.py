from  tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.configure(background=THEME_COLOR)
        self.window.title("Quizz app")
        self.window.config(padx=50, pady=50)
        
        self.score_label = Label(text="score:", pady=20, background=THEME_COLOR,fg="white", font=("Arial", 15, "italic"))
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250)
        self.canvas.config()
        self.question_text = self.canvas.create_text(150, 100,
                                                  text= "",
                                                  width=250,
                                                  font=("Arial", 15, "italic"),
                                                  fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20)
        



        self.y_image = PhotoImage(file="images/true.png")
        self.y_button = Button(image=self.y_image, highlightthickness=0, command=self.answer_true)
        self.y_button.grid(row=2, column=0,pady=30)


        self.x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image=self.x_image, highlightthickness=0, command=self.answer_false)
        self.x_button.grid(row=2, column=1, pady=30)
        
        self.get_next_question()

        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"Score: {self.quiz.score}")
            self.y_button.config(state="disabled")
            self.x_button.config(state="disabled")
    
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
    

        
        
        
        













    









