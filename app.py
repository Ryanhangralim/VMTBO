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

#add balance function
def addbalance(amount):
    #initialize variable
    global balance
    a = balance.get()
    b = amount.get()
    balance.set(a+b)
    current = balance.get()

    #checking for max balance
    if(current == 30000):
        input_sepuluh['state'] = 'disabled'
        input_duapuluh['state'] = 'disabled'
    elif(current == 40000):
        input_sepuluh['state'] = 'disabled'
        input_duapuluh['state'] = 'disabled'
    
    #enable cancel button when balance is added
    cancel['state'] = 'enabled'

    #update label
    balance_label.config(text=f"Balance: {balance.get()}")


#cancel function
def cancel_func():
    global balance

    #sets balance to 0
    balance.set(0)

    #disable button state and enable input button
    cancel['state'] = 'disabled'
    input_sepuluh['state'] = 'enabled'
    input_duapuluh['state'] = 'enabled'

    #update label
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
cancel = ttk.Button(window, text="Cancel", state='disabled', command=cancel_func)
cancel.grid(row=5, column=13, rowspan=2, columnspan=3, sticky='nesw')

#add balance buttons
#add 10k
input_sepuluh = ttk.Button(window, text="Input 10 Ribu", command=lambda:addbalance(sepuluh_ribu))
input_sepuluh.grid(row=11, column=14, columnspan=2, sticky='nesw')

#add 20k
input_duapuluh = ttk.Button(window, text="Input 20 Ribu", command=lambda:addbalance(duapuluh_ribu))
input_duapuluh.grid(row=16, column=14, columnspan=2, sticky='nesw')

label = ttk.Label(screen, text="label", background='grey')
label.pack(expand=True, fill='both')
# label = ttk.Label(window, text='label1', background='blue')
# label.grid(row=20, column=12, rowspan=2, columnspan=4, sticky='nesw')


#run
window.mainloop()