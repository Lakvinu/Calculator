from tkinter import *
from tkinter import messagebox
window = Tk()

window.title("Simple Calculator by Lakvinu")
window.resizable(0,0)
#window.configure(background = 'light blue')
input_line = []
symbols = {'÷': '/', '×': '*', '−': '-', '+': '+'}

def button_command(symbol):

    if symbol in symbols and len(input_line) == 0:
        messagebox.showinfo(title="Warning", message= "The " + symbol + " is not allowed at the beginning")

    if symbol == '0' and len(input_line) >= 2:
        if input_line[-1] == '÷':
            messagebox.showinfo(title= "Warning", message="Dividing by 0 will result in an undefined Awnser")

    if symbol == '=':
        equal_sign()

    elif symbol == 'c':
        clear()
    else:
        if symbol in symbols and input_line[-1] in symbols:
            input_line[-1] = symbol

        else:
            input_line.append(symbol)

        equation.set(''.join(input_line))


def equal_sign():
    global input_line

    new = ''

    for symbol in input_line:
        if symbol in symbols:
            new += symbols[symbol]

        else:
            new += symbol

    sum = eval(new)

    equation.set(sum)

    input_line = [str(sum)]


def clear():
    global input_line

    input_line = []
    equation.set('')


def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

equation = StringVar()
top  = Frame(window, bg= rgbtohex(170,38,54))
top.pack(side = TOP, expand = True, fill = X)
input_place = Entry(top, font =("Arial", 20), textvariable=equation)
input_place.pack(anchor='center', pady=10, ipady=10, ipadx = 40)

#input_place.grid(ipadx = 70, ipady = 20,  padx = 10, pady = 10)

bottom = Frame(window, bg= rgbtohex(43,135,209))
bottom.pack(side=LEFT, fill=BOTH, expand=True)
bottom.pack_propagate(False)

key = {0: ['7','8','9', '+'], 1: ['4','5','6', '−'], 2: ['1','2','3', '×'], 3: ['c', '0', '=', '÷']}

for i in range(4):

    numb = key[i]

    for j in range(4):

        cur = numb[j]

        new_button = Button(bottom, text = cur, font = ("Arial", 20), command =lambda sym = cur: button_command(sym))
        new_button.grid(row = i, column = j, ipadx = 30, padx = 2, ipady = 10, pady = 2)


window.mainloop()