from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import random

alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '1234567890'
alpha_low = alpha_up.lower()

window = Tk()
window.title('password generator')
window.geometry('600x400+800+300')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = '#6A5ACD'


def password(length):
    res = list(random.choice(alpha_up) + random.choice(alpha_low) + random.choice(digit))
    for i in range(length - 3):
        index = random.randint(0, len(res))
        symbol = random.choice(alpha_up + digit + alpha_low)
        res.insert(index, symbol)
    return ''.join(res) + '\n'


def del_info():
    input_text.delete(1.0, END)


def generate_passwords():
    try:
        long = int(input_lenght.get())
        quan = int(input_quanity.get())
    except:
        mb.showerror("Error", "Данные некорректны!")
        return

    for i in range(quan):
        result = password(long)
        input_text.insert(END, result)


def save_pass():
    file_name = fd.asksaveasfilename(defaultextension='')

    with open(file_name, 'w') as f:
        text = input_text.get(0.0, END)
        f.write(text)


lenght = Label(window, text='Длина паролей:', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
lenght.place(x=125, y=25)
input_lenght = Entry(window, width=10, fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
input_lenght.place(x=300, y=25)

quantity = Label(window, text='Кол-во паролей:', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
quantity.place(x=125, y=100)
input_quanity = Entry(window, width=10, fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
input_quanity.place(x=300, y=100)

input_text = Text(window, fg='orange', width=60, height=8, bd=10, font=('TimesNewRoman', 12, 'bold'))
input_text.place(x=20, y=220)

generate = Button(window, text='Генерировать',
                  font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5,
                  command=generate_passwords)
generate.place(x=130, y=170)

clean = Button(window, text='Очистить',
               font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5,
               command=del_info)
clean.place(x=310, y=170)
save = Button(window, text='Сохранить',
              font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5,
              command=save_pass)
save.place(x=450, y=170)

window.mainloop()
