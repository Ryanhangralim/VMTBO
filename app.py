import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Screen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, borderwidth=20, )
        self.grid(row=1, column=1, rowspan=18, columnspan=12, sticky='nesw', padx=10)
        self.hidden = 0

        #frame grid configure
        self.columnconfigure(tuple(range(10)), weight=1, uniform="a")
        self.rowconfigure(tuple(range(18)), weight=1, uniform="a")
        self.grid_propagate(False)

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

    
#window setup
window = tk.Tk()
window.geometry(f'500x675+{round((window.winfo_screenwidth() - 500)/2)}+{round((window.winfo_screenheight() - 730)/2)}')
window.title('Vending Machine D3')
window.resizable(False, False)
window.iconbitmap("images/vmicon.ico")

#variable setup
sepuluh_ribu = tk.IntVar(value=10000)
duapuluh_ribu = tk.IntVar(value=20000)

#window grid setup
window.columnconfigure(tuple(range(17)), weight=1, uniform='fred')
window.rowconfigure(tuple(range(23)), weight= 1, uniform='fred')
window.grid_propagate(False)

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

#change button
change = ttk.Label(window, text="Kembalian", background='dark grey', justify='center')
change.grid(row=19, column=13, columnspan=4, rowspan=2, sticky='nesw')

#vending machine screen setup
"""
    screen1 = bread size selection menu
    screen2 = vegetables selection menu
    screen3 = meat selection menu
    screen4 = sauce selection menu
    screen5 = thank you menu
"""
#frame styling
style = ttk.Style()
style.configure("TFrame", background="#858585")

#screen5
screen5 = Screen(window)
thank_you = ttk.Label(screen5, text="Thank You!", font='20', background='#ffffff')
thank_you.grid(row=4, column=1, rowspan=4, columnspan=8, sticky='nesw')



#screen4
screen4 = Screen(window)
bbq = ttk.Button(screen4, text="Select")
mayo = ttk.Button(screen4, text="Select")
tomat = ttk.Button(screen4, text="Select")
cabai = ttk.Button(screen4, text="Select")
menu4 = ttk.Label(screen4, text="Pick Sauce")

menu4.pack(side='top')
bbq.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
mayo.grid(row=7, column=9, columnspan=2, rowspan=1, sticky='nesw')
tomat.grid(row=11, column=9, columnspan=2, rowspan=1, sticky='nesw')
cabai.grid(row=15, column=9, columnspan=2, rowspan=1, sticky='nesw')

#screen3
screen3 = Screen(window)
menu3 = ttk.Label(screen3, text="Pick Meat")
ayam = ttk.Button(screen3, text="Select")
sapi = ttk.Button(screen3, text="Select")
tuna = ttk.Button(screen3, text="Select")

menu3.pack(side='top')
ayam.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
sapi.grid(row=8, column=9, columnspan=2, rowspan=1, sticky='nesw')
tuna.grid(row=13, column=9, columnspan=2, rowspan=1, sticky='nesw')

#screen2
screen2 = Screen(window)
tomato = ttk.Button(screen2, text="Select")
selada = ttk.Button(screen2, text="Select")
paprika= ttk.Button(screen2, text="Select")
bawang = ttk.Button(screen2, text="Select")
menu2 = ttk.Label(screen2, text="Pick Vegetable")

menu2.pack(side='top')
tomato.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
selada.grid(row=7, column=9, columnspan=2, rowspan=1, sticky='nesw')
paprika.grid(row=11, column=9, columnspan=2, rowspan=1, sticky='nesw')
bawang.grid(row=15, column=9, columnspan=2, rowspan=1, sticky='nesw')

label1 = ttk.Label(screen5, text='label1')
label2 = ttk.Label(screen5, text='label2')
label3 = ttk.Label(screen5, text='label3')
label4 = ttk.Label(screen5, text='label4')

#screen1
screen1 = Screen(window)
menu1 = ttk.Label(screen1, text="Pick Sandwich Size")
small = ttk.Button(screen1, text="Select")
large = ttk.Button(screen1, text="Select")

menu1.pack(side='top')
small.grid(row=6, column=3, rowspan=2, columnspan=4)
large.grid(row=14, column=3, rowspan=2, columnspan=4)

# label1.grid(row=1, column=1, sticky='nesw')
# label2.grid(row=9, column=17, sticky='nesw')
# label3.grid(row=0, column=9, sticky='nesw')
# label4.grid(row=17, column=0, sticky='nesw')
# screen = Screen(window)
# label = ttk.Label(screen, text="label", background='grey')
# label.pack(expand=True, fill='both')
# label = ttk.Label(window, text='label1', background='blue')
# label.grid(row=20, column=12, rowspan=2, columnspan=4, sticky='nesw')


#run
window.mainloop()