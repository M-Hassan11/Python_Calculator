
from tkinter import Entry, Tk, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('346x385+0+0')
        master.config(bg='#c0c0c0')
        master.resizable(False, False)
        
        self.equation = StringVar()
        self.entry_value = ''
        
        self.entry = Entry(master, width=20, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation)
        self.entry.place(x=0, y=0)
        
        Button(width=7, height=3, text='1', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(1)).place(x=87, y=50)
        Button(width=7, height=3, text='0', relief='flat', font=(10), bg='green', command=lambda: self.show(0)).place(x=0, y=50)
        Button(width=7, height=3, text='2', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(2)).place(x=174, y=50)
        Button(width=7, height=3, text='c', relief='flat', font=(10), bg='red', command=self.clear).place(x=260, y=50)
        Button(width=7, height=3, text='3', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(3)).place(x=0, y=136)
        Button(width=7, height=3, text='4', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(4)).place(x=87, y=136)
        Button(width=7, height=3, text='5', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(5)).place(x=174, y=136)
        Button(width=7, height=3, text='+', relief='flat', font=(10), bg='blue', command=lambda: self.show('+')).place(x=260, y=136)
        Button(width=7, height=3, text='6', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(6)).place(x=0, y=220)
        Button(width=7, height=3, text='7', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(7)).place(x=87, y=220)
        Button(width=7, height=3, text='8', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(8)).place(x=174, y=220)
        Button(width=7, height=3, text='-', relief='flat', font=(10), bg='gray', command=lambda: self.show('-')).place(x=260, y=220)
        Button(width=7, height=3, text='9', relief='flat', font=(10), bg='lightblue', command=lambda: self.show(9)).place(x=0, y=300)
        Button(width=7, height=3, text='*', relief='flat', font=(10), bg='yellow', command=lambda: self.show('*')).place(x=87, y=300)
        Button(width=7, height=3, text='/', relief='flat', font=(10), bg='orange', command=lambda: self.show('/')).place(x=174, y=300)
        Button(width=7, height=3, text='=', relief='flat', font=(10), bg='green', command=self.solve).place(x=260, y=300)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')
            print(f"Error: {e}")

root = Tk()
calc = Calculator(root)
root.mainloop()



