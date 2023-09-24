from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm_machine:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110  * blank_space + "ATM MACHINE")
        self.root.geometry("790x760+280+0")
        self.root.configure(background = "gray")
         #Frames
        mainframe = Frame(self.root , bd=20 , width=784 , height = 700 , relief=RIDGE)
        mainframe.grid()
        topframe1 = Frame(mainframe , bd=7 , width=734 , height = 300 , relief=RIDGE)
        topframe1.grid( row=1 , column=0, padx=12)
        topframe2 = Frame(mainframe , bd=7 , width=734 , height = 300 , relief=RIDGE)
        topframe2.grid( row=0 , column=0, padx=8)

        topframe2left= Frame(topframe2 , bd=5 , width=190, height = 300 , relief=RIDGE)
        topframe2left.grid( row=0 , column=0, padx=3)
        
        topframe2mid = Frame(topframe2 , bd=5 , width=200, height = 300 , relief=RIDGE)
        topframe2mid.grid( row=0 , column=1, padx=3)

        topframe2right = Frame(topframe2 , bd=5 , width=190, height = 300 , relief=RIDGE)
        topframe2right.grid( row=0 , column=2, padx=3)

        #widgets
        self.txtreceipt= Text(topframe2mid, height=17 , width=42 , bd=12 , font=('arial' , 9 , 'bold'))
        self.txtreceipt.grid(row=0, column=0)

        self.img_arrow_Left= PhotoImage(file = "leftarrow.png")
        self.btnArrowL1 = Button(topframe2left, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Left).grid(row=0 , column=0, padx=2 , pady=2)

        self.btnArrowL2 = Button(topframe2left, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Left).grid(row=1 , column=0, padx=2 , pady=2)

        self.btnArrowL3 = Button(topframe2left, width=160, height = 60 , state=DISABLED,
        image=self.img_arrow_Left).grid(row=2 , column=0, padx=2 , pady=2)

        self.btnArrowL4 = Button(topframe2left, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Left).grid(row=3 , column=0, padx=2 , pady=2)

        #--------------------------------
        self.img_arrow_Right= PhotoImage(file = "rightarraow.png")
        self.btnArrowR1 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Right).grid(row=0 , column=0, padx=2 , pady=2)

        self.btnArrowR2 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Right).grid(row=1 , column=0, padx=2 , pady=2)

        self.btnArrowR3 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Right).grid(row=2 , column=0, padx=2 , pady=2)

        self.btnArrowR4 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        image=self.img_arrow_Right).grid(row=3 , column=0, padx=2 , pady=2)


         #Pin Numbers
        self.img1= PhotoImage(file = "one.png")
        self.btn1 = Button(topframe1, width=160, height = 60 , 
        image=self.img1).grid(row=2 , column=0, padx=6 , pady=4)

        self.img2= PhotoImage(file = "two.png")
        self.btn2 = Button(topframe1, width=160, height = 60 , 
        image=self.img2).grid(row=2 , column=1, padx=6 , pady=4)

        self.img3= PhotoImage(file = "three.png")
        self.btn3 = Button(topframe1, width=160, height = 60 , 
        image=self.img3).grid(row=2 , column=2, padx=6 , pady=4)


        self.img_cancel= PhotoImage(file = "cancel.png")
        self.btn_cancel = Button(topframe1, width=160, height = 60 , 
        image=self.img_cancel).grid(row=2, column=3, padx=6 , pady=4)

        #-------------------------
        self.img4= PhotoImage(file = "four.png")
        self.btn4 = Button(topframe1, width=160, height = 60 , 
        image=self.img4).grid(row=3 , column=0, padx=6 , pady=4)

        self.img5= PhotoImage(file = "five.png")
        self.btn5 = Button(topframe1, width=160, height = 60 , 
        image=self.img5).grid(row=3 , column=1, padx=6 , pady=4)

        self.img6= PhotoImage(file = "six.png")
        self.btn6 = Button(topframe1, width=160, height = 60 , 
        image=self.img6).grid(row=3, column=2, padx=6 , pady=4)


        self.img_clear= PhotoImage(file = "clear.png")
        self.btn_clear = Button(topframe1, width=160, height = 60 , 
        image=self.img_clear).grid(row=3, column=3, padx=6 , pady=4)

        #-------------------------
        self.img_space1= PhotoImage(file = "empty.png")
        self.btn7 = Button(topframe1, width=160, height = 60 , 
        image=self.img_space1).grid(row=5 , column=0, padx=6 , pady=4)

        self.img_zero= PhotoImage(file = "zero.png")
        self.btn8 = Button(topframe1, width=160, height = 60 , 
        image=self.img_zero).grid(row=5 , column=1, padx=6 , pady=4)

        self.img_space2= PhotoImage(file = "empty.png")
        self.btn9 = Button(topframe1, width=160, height = 60 , 
        image=self.img_space2).grid(row=5, column=2, padx=6 , pady=4)


        self.img_space3= PhotoImage(file = "empty.png")
        self.btn_enter= Button(topframe1, width=160, height = 60 , 
        image=self.img_space3).grid(row=5, column=3, padx=6 , pady=4)













if __name__ == '__main__':
    root = Tk()
    application = atm_machine(root)
    root.mainloop()
