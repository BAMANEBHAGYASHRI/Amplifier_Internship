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


        #function------------------

        def pin_enter():
            pinno = self.txtreceipt.get("1.0","end-1c")
            if ((pinno == str ("2213")) or  (pinno == str("4323")) or  (pinno == str("5982"))):
                self.txtreceipt.delete("1.0",END)
                
                self.txtreceipt.insert(END,'\t\t               ATM' + "\n\n")
                self.txtreceipt.insert(END, 'withdraw cash\t\t\t  Loan' + "\n\n\n\n")
                self.txtreceipt.insert(END, 'cash with Receipt\t\t\t Deposit' + "\n\n\n\n")
                self.txtreceipt.insert(END, 'Balance\t\t\t  Request New Pin' + "\n\n\n\n")
                self.txtreceipt.insert(END, 'Mini Statement\t\t\t  Print Statement' + "\n\n\n\n")
             
                
                self.btnArrowR1 = Button(topframe2right, width=160, height = 60 , state= NORMAL,
                command=loan , image=self.img_arrow_Right).grid(row=0 , column=0, padx=2 , pady=2)

                self.btnArrowR2 = Button(topframe2right, width=160, height = 60 , state= NORMAL,
                command=deposit ,image=self.img_arrow_Right).grid(row=1 , column=0, padx=2 , pady=2)

                self.btnArrowR3 = Button(topframe2right, width=160, height = 60 , state= NORMAL, 
                command = request_NewPin ,image=self.img_arrow_Right).grid(row=2 , column=0, padx=2 , pady=2)

                self.btnArrowR4 = Button(topframe2right, width=160, height = 60 , state= NORMAL,
                command = statement,image=self.img_arrow_Right).grid(row=3 , column=0, padx=2 , pady=2)
                
                #--------------------------------
                self.btnArrowL1 = Button(topframe2left, width=160, height = 60 , state= NORMAL,
                command =withdraw,image=self.img_arrow_Left).grid(row=0 , column=0, padx=2 , pady=2)

                self.btnArrowL2 = Button(topframe2left, width=160, height = 60 , state= NORMAL,
                command=withdraw ,image=self.img_arrow_Left).grid(row=1 , column=0, padx=2 , pady=2)

                self.btnArrowL3 = Button(topframe2left, width=160, height = 60 , state=NORMAL,
                command = Balance,image=self.img_arrow_Left).grid(row=2 , column=0, padx=2 , pady=2)

                self.btnArrowL4 = Button(topframe2left, width=160, height = 60 , state= NORMAL,
                command = statement,image=self.img_arrow_Left).grid(row=3 , column=0, padx=2 , pady=2)
            else:
                self.txtreceipt.delete("1.0",END)
                self.txtreceipt.insert(END, ' Invalid Pin  number' + '\n\n')
                
                
                
                
                


        def clear():
            self.txtreceipt.delete("1.0",END)
            
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

        def insert0():
            value0=0
            self.txtreceipt.insert(END,value0 )

        def insert1():
            value1=1
            self.txtreceipt.insert(END,value1)

        def insert2():
            value2=2
            self.txtreceipt.insert(END,value2 )

        def insert3():
            value3=3
            self.txtreceipt.insert(END,value3 )

        def insert4():
            value4=4
            self.txtreceipt.insert(END,value4 )

        def insert5():
            value5=5
            self.txtreceipt.insert(END,value5 )

        def insert6():
            value6=6
            self.txtreceipt.insert(END,value6 )

        def insert7():
            value7=7
            self.txtreceipt.insert(END,value7 )

        def insert8():
            value8=8
            self.txtreceipt.insert(END,value8 )

        def insert9():
            value9=9
            self.txtreceipt.insert(END,value9 )

        def cancel():
            cancel = tkinter.messagebox.askyesno("ATM","Confirm if you want to cancel")
            if cancel > 0:
                self.root.destroy()
                return

        def withdraw():
            pin_enter()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.focus_set()

        def loan():
            pin_enter()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END, 'loan ')
            self.txtreceipt.focus_set()

        def deposit():
            pin_enter()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.focus_set()


        def  request_NewPin():
            pin_enter()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END , '\t \tWelcome to XBank\n')
            self.txtreceipt.insert(END , 'new pin will be send to your home address\n')
            self.txtreceipt.insert(END, 'withdraw cash\t\t\t  Loan' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'cash with Receipt\t\t\t Deposit' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'Balance\t\t\t  Request New Pin' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'Mini Statement\t\t\t  Print Statement' + "\n\n\n\n")
            self.txtreceipt.insert(END , '\t \tThanks for using XBank\n')

        def  Balance():
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END , '\t \tWelcome to XBank\n')
            self.txtreceipt.insert(END , ' $1967' + "\n") 
            self.txtreceipt.insert(END, 'withdraw cash\t\t\t  Loan' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'cash with Receipt\t\t\t Deposit' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'Balance\t\t\t  Request New Pin' + "\n\n\n\n")
            self.txtreceipt.insert(END, 'Mini Statement\t\t\t  Print Statement' + "\n\n\n\n")
            self.txtreceipt.insert(END , '\t \tThanks for using XBank\n')

        def  statement():
            pinno1 = str(self.txtreceipt.get("1.0","end-1c"))
            pinno2 = str(pinno1)
            pinno3 = float (pinno2)
            pinno4 = float (1967  - (pinno3))
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END , '\n \t ' +  str(pinno4) +  '\n')
            self.txtreceipt.insert(END , '\t\t\t\n\n account balance' + str(pinno4) + "\t\t\n\n" ) 
            self.txtreceipt.insert(END, 'Rent \t\t\t\t  $1200 '+ "\n\n")
            self.txtreceipt.insert(END, 'Tesco \t\t\t\t $79.36' + "\n\n")
            self.txtreceipt.insert(END, 'Rent \t\t\t\t  $1200 '+ "\n\n")
            self.txtreceipt.insert(END, 'sainsbury' + ' \t\t\t\t  $1200 '+ "\n\n")
            self.txtreceipt.insert(END , 'Student Loan \t\t\t\t  $69.72 ' + "\n\n")
            self.txtreceipt.insert(END , 'poundland \t\t\t\t  $19.00 ' + "\n\n")
            
            
            
            
            

        

        #widgets
        self.txtreceipt= Text(topframe2mid, height=17 , width=42 , bd=12 , font=('arial' , 9 , 'bold'))
        self.txtreceipt.grid(row=0, column=0)

        self.img_arrow_Left= PhotoImage(file = "leftarrow.png")
        
        self.btnArrowL1 = Button(topframe2left, width=160, height = 60 , state= DISABLED,
        command = withdraw ,image=self.img_arrow_Left).grid(row=0 , column=0, padx=2 , pady=2)

        self.btnArrowL2 = Button(topframe2left, width=160, height = 60 , state= DISABLED,
        command = withdraw ,image=self.img_arrow_Left).grid(row=1 , column=0, padx=2 , pady=2)

        self.btnArrowL3 = Button(topframe2left, width=160, height = 60 , state=DISABLED,command =Balance ,
        image=self.img_arrow_Left).grid(row=2 , column=0, padx=2 , pady=2)

        self.btnArrowL4 = Button(topframe2left, width=160, height = 60 , state= DISABLED,command =statement ,
        image=self.img_arrow_Left).grid(row=3 , column=0, padx=2 , pady=2)

        #--------------------------------
        self.img_arrow_Right= PhotoImage(file = "rightarraow.png")
        self.btnArrowR1 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        command =loan ,image=self.img_arrow_Right).grid(row=0 , column=0, padx=2 , pady=2)

        self.btnArrowR2 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        command =deposit ,image=self.img_arrow_Right).grid(row=1 , column=0, padx=2 , pady=2)

        self.btnArrowR3 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        command = request_NewPin ,image=self.img_arrow_Right).grid(row=2 , column=0, padx=2 , pady=2)

        self.btnArrowR4 = Button(topframe2right, width=160, height = 60 , state= DISABLED,
        command =statement ,image=self.img_arrow_Right).grid(row=3 , column=0, padx=2 , pady=2)



         #Pin Numbers
        self.img1= PhotoImage(file = "one.png")
        self.btn1 = Button(topframe1, width=160, height = 60 ,  command=insert1,
        image=self.img1).grid(row=2 , column=0, padx=6 , pady=4)

        self.img2= PhotoImage(file = "two.png")
        self.btn2 = Button(topframe1, width=160, height = 60 , command=insert2,
        image=self.img2).grid(row=2 , column=1, padx=6 , pady=4)

        self.img3= PhotoImage(file = "three.png")
        self.btn3 = Button(topframe1, width=160, height = 60 ,  command=insert3,
        image=self.img3).grid(row=2 , column=2, padx=6 , pady=4)


        self.img_cancel= PhotoImage(file = "cancel.png")
        self.btn_cancel = Button(topframe1, width=160, height = 60 , command = cancel ,
        image=self.img_cancel).grid(row=2, column=3, padx=6 , pady=4)

        #-------------------------
        self.img4= PhotoImage(file = "four.png")
        self.btn4 = Button(topframe1, width=160, height = 60 , command=insert4,
        image=self.img4).grid(row=3 , column=0, padx=6 , pady=4)

        self.img5= PhotoImage(file = "five.png")
        self.btn5 = Button(topframe1, width=160, height = 60 , command=insert5,
        image=self.img5).grid(row=3 , column=1, padx=6 , pady=4)

        self.img6= PhotoImage(file = "six.png")
        self.btn6 = Button(topframe1, width=160, height = 60 , command=insert6,
        image=self.img6).grid(row=3, column=2, padx=6 , pady=4)


        self.img_clear= PhotoImage(file = "clear.png")
        self.btn_clear = Button(topframe1, width=160, height = 60 , command=clear,
        image=self.img_clear).grid(row=3, column=3, padx=6 , pady=4)

        #-------------------------
        self.img7= PhotoImage(file = "seven.png")
        self.btn7 = Button(topframe1, width=160, height = 60 , command=insert7,
        image=self.img7).grid(row=4, column=0, padx=6 , pady=4)

        self.img8= PhotoImage(file = "eight.png")
        self.btn8 = Button(topframe1, width=160, height = 60 , command=insert8,
        image=self.img8).grid(row=4, column=1, padx=6 , pady=4)

        self.img9= PhotoImage(file = "nine.png")
        self.btn9 = Button(topframe1, width=160, height = 60 , command=insert9,
        image=self.img9).grid(row=4, column=2, padx=6 , pady=4)


        self.img_enter= PhotoImage(file = "enter.png")
        self.btn_enter = Button(topframe1, width=160, height = 60 , command = pin_enter,
        image=self.img_enter).grid(row=4, column=3, padx=6 , pady=4)
    

        #----------------
        self.img_space1= PhotoImage(file = "empty.png")
        self.btn7 = Button(topframe1, width=160, height = 60 , 
        image=self.img_space1).grid(row=5 , column=0, padx=6 , pady=4)

        self.img_zero= PhotoImage(file = "zero.png")
        self.btn8 = Button(topframe1, width=160, height = 60 , command=insert0,
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
