import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Screen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, borderwidth=20, )
        self.grid(row=1, column=1, rowspan=18, columnspan=12, sticky='nesw')
        self.hidden = 0


    def hide(self):
        if self.hidden == 0:
            self.destroy()
            self.hidden = 1

def add10():
    global balance
    a = balance.get()
    b = sepuluh_ribu.get()
    balance.set(a+b)
    print(f"a:{a}, b:{b}, balance:{balance.get()}")
    balance_label.config(text=f"Balance: {balance.get()}")


def add20():
    global balance
    a = balance.get()
    b = duapuluh_ribu.get()
    balance.set(a+b)
    print(f"a:{a}, b:{b}, balance:{balance.get()}")
    balance_label.config(text=f"Balance: {balance.get()}")
    
#setup
window = tk.Tk()
window.geometry(f'500x675+{round((window.winfo_screenwidth() - 500)/2)}+{round((window.winfo_screenheight() - 730)/2)}')
window.title('Vending Machine D3')
window.resizable(False, False)
window.iconbitmap("images/vmicon.ico")

#variable setup
sepuluh_ribu = tk.IntVar(value=10000)
duapuluh_ribu = tk.IntVar(value=20000)

#window grid setup
window.columnconfigure(tuple(range(17)), weight=1, uniform='a')
window.rowconfigure(tuple(range(23)), weight= 1, uniform='a')

#vending machine screen setup
screen = Screen(window)

#balance label
balance = tk.IntVar(value = 0)
balance_label = ttk.Label(window, text=f'Balance = {balance.get()}')
balance_label.grid(row=2, column=13, rowspan=2, columnspan=3, sticky='nesw')

#cancel button
cancel = ttk.Button(window, text="Cancel", command=add10)
cancel.grid(row=5, column=13, rowspan=2, columnspan=3, sticky='nesw')

#add balance buttons
#add 10k
input_sepuluh = ttk.Button(window, text="Input 10 Ribu", command=add10)

#add 20k
input_sepuluh = ttk.Button(window, text="Input 10 Ribu", command=add10)

label = ttk.Label(screen, text="label", background='grey')
label.pack(expand=True, fill='both')
# label = ttk.Label(window, text='label1', background='blue')
# label.grid(row=20, column=12, rowspan=2, columnspan=4, sticky='nesw')


#run
window.mainloop()