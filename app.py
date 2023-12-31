import tkinter as tk
from tkinter import Toplevel
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
from deltatopiVM import delta_topi

user_input = list()
state_list = list()
user_output = list()
current_state = 'R'
state_list.append(current_state)

background_color = "#ecf0f1"


def convert(list):
    roti = {
        "a" : "Roti Kecil.", #input sandwich
        "b" : "Roti Besar."    
    }

    sayur = {
        "c" : "Tomat,",
        "d" : "Selada,",
        "e" : "Paprika,",
        "f" : "Bawang,"
    }

    daging = {
        "g" : "Daging Ayam.",
        "h" : "Daging Sapi.",
        "i" : "Daging Tuna."
    }

    saus = {
        "j" : "Saus BBQ.",
        "k" : "Saus Mayonnaise.",
        "l" : "Saus Tomat.",
        "m" : "Saus Cabai.",
    }

    roti_output = "Roti : "
    sayur_output = "Sayur : "
    daging_output = "Daging : "
    saus_output = "Saus : " 
    for i in list:
        if i in roti:
            roti_output += roti[i]
        elif i in sayur:
            sayur_output += sayur[i] + " "
        elif i in daging:
            daging_output += daging[i]
        elif i in saus:
            saus_output += saus[i]
    sayur_output = sayur_output[:-2] + "."
    return f"{roti_output}\n{sayur_output}\n{daging_output}\n{saus_output}" 

def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

class Screen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, borderwidth=20, bootstyle = 'light')
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
    #amount = jumlah uang yang diinput oleh user
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
        current_state = 'N'
    elif(current == 20000):
        current_state = 'O'
    elif(current == 30000):
        current_state = 'P'
    elif(current == 40000):
        current_state = 'Q'
    state_list.append(current_state)
    
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
    balance_label.config(text=f"Balance: \nRp. {balance.get()}")


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
    balance_label.config(text=f"Balance:\n Rp. {balance.get()}")

#munculkan pesanan
def pesanan():
    #update user_input & state
    user_input.append('q')
    current_state = 'R'
    state_list.append(current_state)
    user_output.append('1')

    #Pop up screen
    tombol_ambil['state'] = 'disabled'
    top= Toplevel(window)
    top.geometry(f"500x600+{round((window.winfo_screenwidth() - 400)/2)}+{round((window.winfo_screenheight() - 630)/2)}")
    top.resizable(False,False)
    top.title("Pesanan")
    top.iconbitmap("images/vmicon.ico")

    #Label pesanan
    label = ttk.Label(top, text="Pesanan Anda", font=("Helvetica", 12, "bold"))
    label.pack(pady=5)

    #import gambar
    sandwich = Image.open("images/sandwich.png").resize((200,200))
    sandwich = ImageTk.PhotoImage(sandwich)
    top.image = sandwich

    #label gambar
    label_gambar = ttk.Label(top, image=sandwich ,text='gambar')
    label_gambar.pack()

    #label detail pesanan
    detail_pesanan = ttk.Label(top, text=f"Sandwich :\n{convert(user_input)}")
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
    ttk.Label(top, text=f"Vending Machine Output : {user_output}").pack()
    ttk.Label(top, text=f"State List : {state_list}").pack()
    ttk.Label(top, text=f"Status : {delta_topi(user_input)}").pack()

    #hapus kembalian
    change['text'] = "Kembalian"

    #reset vending machine button
    reset_button2 = ttk.Button(top, text="Reset Vending Machine", command=reset)
    reset_button2.pack(side='bottom', pady=25)


def screen1_func(size):
    global balance
    current = balance.get()

    #sets the price & userinput & state list
    if(size.get() == "small"):
        price = 20000
        user_input.append('a')
        current_state = 'A'
    elif(size.get() == "large"):
        price = 30000
        user_input.append('b')
        current_state = 'B'
    state_list.append(current_state)


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
    next['state'] = 'enabled'
    if(veggie == 1):
        user_input.append('c')
        current_state = 'C'
        tomato['state'] = 'disabled'
    elif(veggie == 2):
        user_input.append('d')
        current_state = 'D'
        selada['state'] = 'disabled'
    elif(veggie == 3):
        user_input.append('e')
        current_state = 'E'
        paprika['state'] = 'disabled'
    elif(veggie == 4):
        user_input.append('f')
        current_state = 'F'
        bawang['state'] = 'disabled'
    state_list.append(current_state)
    
def next_func():
    #hide screen
    screen2.hide()

def screen3_func(meat):
    #add user input and state travelled
    if(meat == 1):
        user_input.append('g')
        current_state = 'G'
    elif(meat == 2):
        user_input.append('h')
        current_state = 'H'
    elif(meat == 3):
        user_input.append('i')
        current_state = 'I'
    state_list.append(current_state)
    #hide screen
    screen3.hide()


def screen4_func(sauce):
    #add user input and state
    if(sauce == 1):
        user_input.append('j')
        current_state = 'J'
    elif(sauce== 2):
        user_input.append('k')
        current_state = 'K'
    elif(sauce== 3):
        user_input.append('l')
        current_state = 'L'
    elif(sauce == 4):
        user_input.append('m')
        current_state = 'M'
    state_list.append(current_state)
    
    #hide screen
    screen4.hide()
    output.destroy()

#window setup
window = ttk.Window(themename= 'flatly')
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
reset_button = ttk.Button(window, text="Reset", command=reset, bootstyle ="danger")
reset_button.grid(row = 2, column=14, rowspan=2, columnspan=2, sticky='nesw')

#balance label
balance = tk.IntVar(value = 0)
balance_label = ttk.Label(window, text=f'Balance: \nRp. {balance.get()}', font=("Helvetica", 11, "bold"))
balance_label.grid(row=4, column=14, rowspan=2, columnspan=3, sticky='nesw')
balance_label.config(anchor='center')

#cancel button
cancel = ttk.Button(window, text="Cancel", state='disabled', command=cancel_func, bootstyle='warning')
cancel.grid(row=6, column=14, rowspan=2, columnspan=2, sticky='nesw')

#add balance buttons
#10k image
gambar_sepuluh = Image.open("images/Uang10000.png").resize((150,64))
gambar_sepuluh = ImageTk.PhotoImage(gambar_sepuluh)

label_sepuluh = ttk.Label(window, image=gambar_sepuluh)
label_sepuluh.grid(row = 9, column=14, rowspan=2, columnspan=2)

#add 10k
input_sepuluh = ttk.Button(window, text="Input Rp. 10.000", command=lambda:addbalance(sepuluh_ribu))
input_sepuluh.grid(row=11, column=14, columnspan=2, rowspan=2, sticky='nesw', pady=5)

#20k image
gambar_duapuluh = Image.open("images/Uang20000.png").resize((150,64))
gambar_duapuluh = ImageTk.PhotoImage(gambar_duapuluh)

label_duapuluh = ttk.Label(window, image=gambar_duapuluh)
label_duapuluh.grid(row = 14, column=14, rowspan=2, columnspan=2)

#add 20k
input_duapuluh = ttk.Button(window, text="Input Rp. 20.000", command=lambda:addbalance(duapuluh_ribu))
input_duapuluh.grid(row=16, column=14, columnspan=2, rowspan=2, sticky='nesw', pady=5)

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
style.configure("TButton", font=("Helvetica", 10))
style.configure("TLabel", font=("Helvetica", 10))

#screen5
screen5 = Screen(window)
thank_you = ttk.Label(screen5, text="Thank You!", font=("Helvetica", 25, "bold"), background=background_color)
thank_you.grid(row=6, column=2, rowspan=4, columnspan=8, sticky='nesw')

#screen4
"""
    1 = BBQ
    2 = Mayonnaise
    3 = Tomat
    4 = Cabai
"""
screen4 = Screen(window)
bbq = ttk.Button(screen4, text="BBQ",command=lambda: screen4_func(1))
mayo = ttk.Button(screen4, text="Mayonnaise",command=lambda: screen4_func(2))
tomat = ttk.Button(screen4, text="Tomat",command=lambda: screen4_func(3))
cabai = ttk.Button(screen4, text="Cabai",command=lambda: screen4_func(4))
menu4 = ttk.Label(screen4, text="Pick Sauce", font=("Helvetica", 12, "bold"), background=background_color)
menu4.pack(side='top')

#images
bbq_img = ImageTk.PhotoImage(Image.open("images/bbq.png").resize((82, 82)))
mayo_img = ImageTk.PhotoImage(Image.open("images/mayonnaise.png").resize((82, 82)))
chili_img = ImageTk.PhotoImage(Image.open("images/chili.png").resize((82, 82)))
ketchup_img = ImageTk.PhotoImage(Image.open("images/ketchup.png").resize((82, 82)))

ttk.Label(screen4, image=bbq_img, background=background_color).grid(row=2, column=2, columnspan=2, rowspan=3)
ttk.Label(screen4, image=mayo_img, background=background_color).grid(row=6, column=2, columnspan=2, rowspan=3)
ttk.Label(screen4, image=ketchup_img, background=background_color).grid(row=10, column=2, columnspan=2, rowspan=3)
ttk.Label(screen4, image=chili_img, background=background_color).grid(row=14, column=2, columnspan=2, rowspan=3)

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
menu3 = ttk.Label(screen3, text="Pick Meat", font=("Helvetica", 12, "bold"), background=background_color)
ayam = ttk.Button(screen3, text="Ayam",command=lambda: screen3_func(1))
sapi = ttk.Button(screen3, text="Sapi",command=lambda: screen3_func(2))
tuna = ttk.Button(screen3, text="Tuna",command=lambda: screen3_func(3))

#images
chicken_img = ImageTk.PhotoImage(Image.open("images/chicken.png").resize((100, 100)))
beef_img = ImageTk.PhotoImage(Image.open("images/beef.png").resize((100, 100)))
tuna_img = ImageTk.PhotoImage(Image.open("images/tuna.png").resize((100, 100)))

ttk.Label(screen3, image=chicken_img, background=background_color).grid(row=3, column=2, columnspan=2, rowspan=3)
ttk.Label(screen3, image=beef_img, background=background_color).grid(row=8, column=2, columnspan=2, rowspan=3)
ttk.Label(screen3, image=tuna_img, background=background_color).grid(row=13, column=2, columnspan=2, rowspan=3)

menu3.pack(side='top')
ayam.grid(row=4, column=9, columnspan=2, rowspan=1, sticky='nesw')
sapi.grid(row=9, column=9, columnspan=2, rowspan=1, sticky='nesw')
tuna.grid(row=14, column=9, columnspan=2, rowspan=1, sticky='nesw')

#screen2
"""
    1 = tomat
    2 = selada
    3 = paprika
    4 = bawang
"""
screen2 = Screen(window)
tomato = ttk.Button(screen2, text="Tomat", command=lambda: screen2_func(1))
selada = ttk.Button(screen2, text="Selada", command=lambda: screen2_func(2))
paprika= ttk.Button(screen2, text="Paprika", command=lambda: screen2_func(3))
bawang = ttk.Button(screen2, text="Bawang", command=lambda: screen2_func(4))
next = ttk.Button(screen2, text="Next", width=15, state='disabled', command=next_func)
menu2 = ttk.Label(screen2, text="Pick Vegetable", font=("Helvetica", 12, "bold"), background=background_color)

menu2.pack(side='top')

#images
tomato_img = ImageTk.PhotoImage(Image.open("images/tomato.png").resize((75, 75)))
lettuce_img = ImageTk.PhotoImage(Image.open("images/lettuce.png").resize((75, 75)))
paprika_img = ImageTk.PhotoImage(Image.open("images/paprika.png").resize((75, 75)))
onion_img = ImageTk.PhotoImage(Image.open("images/onion.png").resize((75, 75)))

ttk.Label(screen2, image=tomato_img, background=background_color).grid(row=2, column=2, columnspan=2, rowspan=3)
ttk.Label(screen2, image=lettuce_img, background=background_color).grid(row=5, column=2, columnspan=2, rowspan=3)
ttk.Label(screen2, image=paprika_img, background=background_color).grid(row=8, column=2, columnspan=2, rowspan=3)
ttk.Label(screen2, image=onion_img, background=background_color).grid(row=11, column=2, columnspan=2, rowspan=3)

tomato.grid(row=3, column=9, columnspan=2, rowspan=1, sticky='nesw')
selada.grid(row=6, column=9, columnspan=2, rowspan=1, sticky='nesw')
paprika.grid(row=9, column=9, columnspan=2, rowspan=1, sticky='nesw')
bawang.grid(row=12, column=9, columnspan=2, rowspan=1, sticky='nesw')
next.pack(side='bottom', ipady=12, pady=5)

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

small_bread_label = ttk.Label(screen1, image=small_bread, background=background_color)
big_bread_label = ttk.Label(screen1, image=big_bread, background=background_color)

menu1 = ttk.Label(screen1, text="Pick Sandwich Size", font=("Helvetica", 12, "bold"), background=background_color)
small = ttk.Button(screen1, text="Small: Rp. 20.000", state='disabled', command=lambda:screen1_func(small_size))
large = ttk.Button(screen1, text="Large: Rp. 30.000", state='disabled', command=lambda:screen1_func(large_size))

menu1.pack(side='top')
small.grid(row=8, column=3, rowspan=2, columnspan=4)
large.grid(row=14, column=3, rowspan=2, columnspan=4)
small_bread_label.grid(row = 6, column=4, rowspan=2, columnspan=2)
big_bread_label.grid(row = 11, column=4, rowspan=2, columnspan=2)

#run
window.mainloop()