import tkinter as tk 
import io, sys

class Calculatrice(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Calculatrice basique")
        self.master.minsize(300, 200)

        self.lbl_resultat = None
        self.resultat = tk.StringVar()
        self.resultat.set('0')
        self.entrees = ''

        self.setLabel()
        self.setButtons()
    
    def setLabel(self):
        self.lbl_resultat = tk.Label(self.master, width=30, anchor="e", textvariable=self.resultat, \
            bg="white", pady=5, borderwidth=1, relief="solid")
        self.lbl_resultat.pack()

    def setButtons(self):
        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack()

        self.textButtons = [('(', ')', '%', 'AC'), 
        ('1', '2', '3', '+'), 
        ('4', '5', '6', '-'), 
        ('7', '9', '8', '/'), 
        ('0', '.', '=', '*')]

        i = 1
        for tb in self.textButtons:
            j = 0
            for t in tb:
                tk.Button(self.frame_buttons, text=t, width=4, command=self.handleClick(t)).grid(row=i, column=j, padx=5)
                j += 1
            i += 1
        
    def handleClick(self, arg=''):
        def click():
            if arg == 'AC':
                self.entrees = ''
            elif arg == '=':
                self.entrees = self.calculate()
            else:
                self.entrees += arg
            self.resultat.set(self.entrees)
            print(self.entrees)
            
        return click
    
    def calculate(self):
        old_stdout = sys.stdout 
        new_stdout = io.StringIO() 
        sys.stdout = new_stdout 

        prog = 'print(%s)' % self.entrees
        val = ''
        try:
            exec(prog)
            val = sys.stdout.getvalue().strip()
        except:
            val = 'Erreur' 
        finally:
            sys.stdout = old_stdout 
        return val
    

if __name__ == '__main__':
    calc = Calculatrice()
    calc.mainloop()


