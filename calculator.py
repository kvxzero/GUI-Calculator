from tkinter import * 

expression = ''

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)  

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = str(total)
    except:
        equation.set("Invalid Expression!")
        expression = ""  

def clear():
    global expression
    expression = ""
    equation.set("")
    
def backB():
    global expression
    expression = expression[:-1]
    equation.set(expression)

gui = Tk()  
gui.configure(background="white")  
gui.title("GUI Py Calc")  
gui.geometry("400x230")  
gui.resizable(width=False, height=False)

equation = StringVar()


expression_field = Entry(gui,font=("Courier New", 16, 'bold'), textvariable=equation)
expression_field.grid(columnspan=50, ipadx=70)
equation.set("0")

button0=Button(gui, text=' 0 ', fg='black', bg='grey',command=lambda: press(0),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button0.grid(row=4, column=1)  

button1=Button(gui, text=' 1 ', fg='black', bg='grey', command=lambda: press(1),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button1.grid(row=2, column=0)

button2= Button(gui, text=' 2 ', fg='black', bg='grey', command=lambda: press(2),
                height=1, width=7,font=("Arial", 16, 'bold'))  
button2.grid(row=2, column=1) 

button3=Button(gui, text=' 3 ', fg='black', bg='grey',command=lambda: press(3),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button3.grid(row=2, column=2)

button4=Button(gui, text=' 4 ', fg='black', bg='grey', command=lambda: press(4),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button4.grid(row=2, column=3)  

button5=Button(gui, text=' 5 ', fg='black', bg='grey', command=lambda: press(5),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button5.grid(row=3, column=0)  

button6=Button(gui, text=' 6 ', fg='black', bg='grey', command=lambda: press(6),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button6.grid(row=3, column=1) 

button7=Button(gui, text=' 7 ', fg='black', bg='grey',command=lambda: press(7),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button7.grid(row=3, column=2) 

button8=Button(gui, text=' 8 ', fg='black', bg='grey',command=lambda: press(8),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button8.grid(row=3, column=3)  

button9=Button(gui, text=' 9 ', fg='black', bg='grey', command=lambda: press(9),
               height=1, width=7,font=("Arial", 16, 'bold'))  
button9.grid(row=4, column=0)  

decimal=Button(gui, text='.', fg='black', bg='#FEB95F',command=lambda: press("."),
               height=1, width=7,font=("Arial", 16, 'bold'))  
decimal.grid(row=4, column=2)

plus = Button(gui, text=' + ', fg='black', bg='#FEB95F', command=lambda: press("+"),
              height=1, width=7,font=("Arial", 16, 'bold'))  
plus.grid(row=4, column=3) 

minus = Button(gui, text=' - ', fg='black', bg='#FEB95F', command=lambda: press("-"),
               height=1, width=7,font=("Arial", 16, 'bold'))  
minus.grid(row=5, column=0) 

multiply = Button(gui, text='X', fg='black', bg='#FEB95F', command=lambda: press("*"),
                  height=1, width=7,font=("Arial", 16, 'bold'))  
multiply.grid(row=5, column=1) 

divide = Button(gui, text=' / ', fg='black', bg='#FEB95F',command=lambda: press("/"),
                height=1, width=7,font=("Arial", 16, 'bold'))  
divide.grid(row=5, column=2) 

equal = Button(gui, text=' = ', fg='black', bg='#FEB95F',command=equalpress,
               height=1, width=7,font=("Arial", 16, 'bold'))  
equal.grid(row=5, column=3) 

clear = Button(gui, text='AC', fg='black', bg='#FEB95F',command=clear,
               height=1,  width=7,font=("Arial", 16, 'bold'))  
clear.grid(row=6, column=2) 

back = Button(gui, text='Back', fg='black', bg='#FEB95F',command=lambda: backB(),
              height=1,  width=7,font=("Arial", 16, 'bold'))   
back.grid(row=6, column=3)

gui.mainloop()
