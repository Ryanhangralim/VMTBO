import tkinter as tk
from tkinter import ttk, Toplevel
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

user_input = list()
state_list = list()
user_output = list()
state_list.append('R')

table = {
    "a" : "Roti Kecil,", #input sandwich
    "b" : "Roti Besar,",
    "c" : "Tomat,",
    "d" : "Selada,",
    "e" : "Paprika,",
    "f" : "Bawang,",
    "g" : "Daging Ayam,",
    "h" : "Daging Sapi,",
    "i" : "Daging Tuna,",
    "j" : "Saus BBQ.",
    "k" : "Saus Mayonnaise.",
    "l" : "Saus Tomat.",
    "m" : "Saus Cabai.",
    "r" : "Kembalian = Rp. 10000",       #output kembalian
    "s" : "Kembalian = Rp. 20000",
    "t" : "Kembalian = Rp. 30000",
    "u" : "Kembalian = Rp. 40000"
}


def convert(list):
    final = " "
    for i in list:
        if i in table:
            final += table[i] + " "
    return final

def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

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

    #add input to user_input
    if(b == 10000):
        user_input.append('n')
    elif(b == 20000):
        user_input.append('o')

    #add state to travelled state
    current = balance.get()
    if(current == 10000):
        state_list.append('N')
    elif(current == 20000):
        state_list.append('O')
    elif(current == 30000):
        state_list.append('P')
    elif(current == 40000):
        state_list.append('Q')
    
    #checking for max balance
    if(current == 30000):
        input_sepuluh['state'] = 'disabled'
        input_duapuluh['state'] = 'disabled'
    elif(current == 40000):
        input_sepuluh['state'] = 'disabled'
        input_duapuluh['state'] = 'disabled'
    
    #enabling menu1 buttons when above a certain balance
    if(current >= 20000):
        small['state'] = 'enabled'
    if(current >= 30000):
        small['state'] = 'enabled'
        large['state'] = 'enabled'

    #enable cancel button when balance is added
    cancel['state'] = 'enabled'

    #update label
    balance_label.config(text=f"Balance: {balance.get()}")


#cancel function
def cancel_func():
    global balance

    #add input to user_input
    user_input.append('p')

    #add travelled state to state_list
    state_list.append('R')

    #add output to user_output
    current = balance.get()
    if(current == 10000):
        user_output.append('r')
        change["text"] = "10000"
    elif(current == 20000):
        user_output.append('s')
        change["text"] = "20000"
    elif(current == 30000):
        user_output.append('t')
        change["text"] = "30000"
    elif(current == 40000):
        user_output.append('u')
        change["text"] = "40000"

    #sets balance to 0
    balance.set(0)

    #disable button state and enable input button, disable small and large button
    cancel['state'] = 'disabled'
    input_sepuluh['state'] = 'enabled'
    input_duapuluh['state'] = 'enabled'
    small['state'] = 'disabled'
    large['state'] = 'disabled'


    #update label
    balance_label.config(text=f"Balance: {balance.get()}")

#munculkan pesanan
def pesanan():
    #update user_input & state
    user_input.append('q')
    state_list.append('R')
    user_output.append('1')

    #Pop up screen
    tombol_ambil['state'] = 'disabled'
    top= Toplevel(window)
    top.geometry(f"400x500+{round((window.winfo_screenwidth() - 400)/2)}+{round((window.winfo_screenheight() - 630)/2)}")
    top.resizable(False,False)
    top.title("Pesanan")

    #Label pesanan
    label = ttk.Label(top, text="Pesanan Anda")
    label.pack()

    #import gambar
    sandwich = Image.open("images/sandwich.png").resize((250,250))
    sandwich = ImageTk.PhotoImage(sandwich)
    top.image = sandwich

    #label gambar
    label_gambar = ttk.Label(top, image=sandwich ,text='gambar')
    label_gambar.pack()

    #label detail pesanan
    detail_pesanan = ttk.Label(top, text=f"Sandwich :{convert(user_input)}")
    detail_pesanan.pack()

    #kembalian
    if change['text'] == "Kembalian":
        pass
    else:
        kembalian = ttk.Label(top, text=f"Kembalian : Rp. {change['text']}")
        kembalian.pack()

    #final state
    final_state = ttk.Label(top, text=f"Final State : {state_list[-1]}")
    final_state.pack()

    #print list
    ttk.Label(top, text=f"User Input : {user_input}").pack()
    ttk.Label(top, text=f"User Output : {user_output}").pack()
    ttk.Label(top, text=f"State List : {state_list}").pack()

    #hapus kembalian
    change['text'] = "Kembalian"

def screen1_func(size):
    global balance
    current = balance.get()

    #sets the price & userinput & state list
    if(size.get() == "small"):
        price = 20000
        user_input.append('a')
        state_list.append('A')
    elif(size.get() == "large"):
        price = 30000
        user_input.append('b')
        state_list.append('B')


    #check for changes
    user_change = current-price

    #output 
    if (user_change == 10000):
        user_output.append('r')
        change["text"] = "10000"
    elif(user_change == 20000):
        user_output.append('s')
        change["text"] = "20000"
    user_change = 0
    balance.set(user_change)

    #update balance label
    balance_label.config(text=f"Balance: {balance.get()}")

    #disable cancel button and input button once selected size
    cancel['state'] = 'disabled'
    input_sepuluh['state'] = 'disabled'
    input_duapuluh['state'] = 'disabled'

    #hide screen
    screen1.hide()


def screen2_func(veggie):
    #add user input and state
    if(veggie == 1):
        user_input.append('c')
        state_list.append('C')
    elif(veggie == 2):
        user_input.append('d')
        state_list.append('D')
    elif(veggie == 3):
        user_input.append('e')
        state_list.append('E')
    elif(veggie == 4):
        user_input.append('f')
        state_list.append('F')
    
    #hide screen
    screen2.hide()


def screen3_func(meat):
    #add user input and state travelled
    if(meat == 1):
        user_input.append('g')
        state_list.append('G')
    elif(meat == 2):
        user_input.append('h')
        state_list.append('H')
    elif(meat == 3):
        user_input.append('i')
        state_list.append('I')

    #hide screen
    screen3.hide()


def screen4_func(sauce):
    #add user input and state
    if(sauce == 1):
        user_input.append('j')
        state_list.append('J')
    elif(sauce== 2):
        user_input.append('k')
        state_list.append('K')
    elif(sauce== 3):
        user_input.append('l')
        state_list.append('L')
    elif(sauce == 4):
        user_input.append('m')
        state_list.append('M')
    
    #hide screen
    screen4.hide()
    output.destroy()

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

#reset button
reset_button = ttk.Button(window, text="Reset", command=reset)
reset_button.grid(row = 2, column=13, rowspan=2, columnspan=2, sticky='nesw')

#balance label
balance = tk.IntVar(value = 0)
balance_label = ttk.Label(window, text=f'Balance = {balance.get()}')
balance_label.grid(row=4, column=13, rowspan=2, columnspan=3, sticky='nesw')
balance_label.config(anchor='center')

#cancel button
cancel = ttk.Button(window, text="Cancel", state='disabled', command=cancel_func)
cancel.grid(row=6, column=13, rowspan=2, columnspan=3, sticky='nesw')

#add balance buttons
#10k image
gambar_sepuluh = Image.open("images/Uang10000.png").resize((150,64))
gambar_sepuluh = ImageTk.PhotoImage(gambar_sepuluh)

label_sepuluh = ttk.Label(window, image=gambar_sepuluh)
label_sepuluh.grid(row = 9, column=14, rowspan=2, columnspan=3)

#add 10k
input_sepuluh = ttk.Button(window, text="Input 10 Ribu", command=lambda:addbalance(sepuluh_ribu))
input_sepuluh.grid(row=11, column=14, columnspan=2, sticky='nesw')

#20k image
gambar_duapuluh = Image.open("images/Uang20000.png").resize((150,64))
gambar_duapuluh = ImageTk.PhotoImage(gambar_duapuluh)

label_duapuluh = ttk.Label(window, image=gambar_duapuluh)
label_duapuluh.grid(row = 14, column=14, rowspan=2, columnspan=3)

#add 20k
input_duapuluh = ttk.Button(window, text="Input 20 Ribu", command=lambda:addbalance(duapuluh_ribu))
input_duapuluh.grid(row=16, column=14, columnspan=2, sticky='nesw')

#change label
change = ttk.Label(window, text="Kembalian", background='dark grey')
change.grid(row=20, column=13, columnspan=3, rowspan=2, sticky='nesw', )
change.config(anchor='center')

#tombol ambil pesanan
tombol_ambil = ttk.Button(window, text="Konfirmasi Pesanan", command=pesanan)
tombol_ambil.grid(row=20, column=3, columnspan=8, rowspan=2, sticky='nesw')

#output label
output = ttk.Label(window, text="Output", background="light grey")
output.grid(row=20, column=3, columnspan=8, rowspan=2, sticky='nesw')
output.config(anchor='center')

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
"""
    1 = BBQ
    2 = Mayonnaise
    3 = Cabai
    4 = Tomat
"""
screen4 = Screen(window)
bbq = ttk.Button(screen4, text="Select",command=lambda: screen4_func(1))
mayo = ttk.Button(screen4, text="Select",command=lambda: screen4_func(2))
tomat = ttk.Button(screen4, text="Select",command=lambda: screen4_func(3))
cabai = ttk.Button(screen4, text="Select",command=lambda: screen4_func(4))
menu4 = ttk.Label(screen4, text="Pick Sauce")

menu4.pack(side='top')
bbq.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
mayo.grid(row=7, column=9, columnspan=2, rowspan=1, sticky='nesw')
tomat.grid(row=11, column=9, columnspan=2, rowspan=1, sticky='nesw')
cabai.grid(row=15, column=9, columnspan=2, rowspan=1, sticky='nesw')

#screen3
"""
    1 = ayam
    2 = sapi
    3 = tuna
"""
screen3 = Screen(window)
menu3 = ttk.Label(screen3, text="Pick Meat")
ayam = ttk.Button(screen3, text="Select",command=lambda: screen3_func(1))
sapi = ttk.Button(screen3, text="Select",command=lambda: screen3_func(2))
tuna = ttk.Button(screen3, text="Select",command=lambda: screen3_func(3))

menu3.pack(side='top')
ayam.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
sapi.grid(row=8, column=9, columnspan=2, rowspan=1, sticky='nesw')
tuna.grid(row=13, column=9, columnspan=2, rowspan=1, sticky='nesw')

#screen2
"""
    1 = tomat
    2 = selada
    3 = paprika
    4 = bawang
"""
screen2 = Screen(window)
tomato = ttk.Button(screen2, text="Select", command=lambda: screen2_func(1))
selada = ttk.Button(screen2, text="Select", command=lambda: screen2_func(2))
paprika= ttk.Button(screen2, text="Select", command=lambda: screen2_func(3))
bawang = ttk.Button(screen2, text="Select", command=lambda: screen2_func(4))
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
small_size = tk.StringVar(value="small")
large_size = tk.StringVar(value="large")
screen1 = Screen(window)

#screen 1 images
small_bread = Image.open("images/Bread.png").resize((130,130))
small_bread = ImageTk.PhotoImage(small_bread)

big_bread = Image.open("images/Bread.png").resize((190,190))
big_bread = ImageTk.PhotoImage(big_bread)

small_bread_label = ttk.Label(screen1, image=small_bread, background='#858585')
big_bread_label = ttk.Label(screen1, image=big_bread, background='#858585')

menu1 = ttk.Label(screen1, text="Pick Sandwich Size")
small = ttk.Button(screen1, text="Small: Rp. 20.000", state='disabled', command=lambda:screen1_func(small_size))
large = ttk.Button(screen1, text="Large: Rp. 30.000", state='disabled', command=lambda:screen1_func(large_size))

menu1.pack(side='top')
small.grid(row=8, column=3, rowspan=2, columnspan=4)
large.grid(row=14, column=3, rowspan=2, columnspan=4)
small_bread_label.grid(row = 6, column=4, rowspan=2, columnspan=2)
big_bread_label.grid(row = 11, column=4, rowspan=2, columnspan=2)


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

print(f" User Input: {user_input}")
print(f" User Output: {user_output}")
print(f" State List: {state_list}")