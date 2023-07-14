from tkinter import *
import string

operations = {'+': lambda a, b: float(a) + float(b),
              '-': lambda a, b: float(a) - float(b),
              ':': lambda a, b: float(a) / float(b) if b != '0' else 'ERROR',
              '*': lambda a, b: float(a) * float(b)}

window = Tk()
window.title('TEST')
window.geometry('400x500+800+300')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = 'yellow'


def use_operation(ent, text):
    for el in range(len(text)):
        if not text[el].isdigit() and text[el] != '.':
            if text[:el].count('.') <= 1 and text[el + 1:].count('.') <= 1:
                res = operations[text[el]](text[:el], text[el + 1:])
                get_button(res, ent)
            else:
                get_button('ERROR', ent)


def get_button(num, ent):
    text = ent.get()
    if 'ERROR' in text:
        ent.delete(0, END)
    if len(text) > 0 and text[-1] in '+-:*.' and str(num) in '+-:*.':
        ent.delete(len(text) - 1, END)
        ent.insert(END, num)
    else:
        ent.insert(END, num)


def inp_place():
    input_place = Entry(window, width=10, fg='orange', bd=10, font=('TimesNewRoman', 24, 'bold'))
    input_place.pack()
    return input_place


def try_isalpha(text):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    if not text[-1].isdigit():
        return False
    for i in text:
        if i in alphabet:
            return False
    return True


def get_text(ent):
    text = ent.get()
    if try_isalpha(text):
        ent.delete(0, END)
        use_operation(ent, text)
    else:
        ent.delete(0, END)
        get_button('ERROR', ent)


def del_last(ent):
    text = ent.get()
    ent.delete(len(text) - 1, END)


def del_all(ent):
    text = ent.get()
    ent.delete(0, END)


def pressed():
    btn.destroy()
    ent = inp_place()
    bt0 = Button(window, text=0,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(0, ent)
                 )
    bt0.place(x=100, y=200, width=50, height=50)
    bt1 = Button(window, text=1,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(1, ent)
                 )
    bt1.place(x=150, y=200, width=50, height=50)
    bt2 = Button(window, text=2,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(2, ent)
                 )
    bt2.place(x=200, y=200, width=50, height=50)
    bt3 = Button(window, text=3,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(3, ent))
    bt3.place(x=100, y=250, width=50, height=50)
    bt4 = Button(window, text=4,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(4, ent))
    bt4.place(x=150, y=250, width=50, height=50)
    bt5 = Button(window, text=5,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(5, ent))
    bt5.place(x=200, y=250, width=50, height=50)
    bt6 = Button(window, text=6,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(6, ent))
    bt6.place(x=100, y=300, width=50, height=50)
    bt7 = Button(window, text=7,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(7, ent))
    bt7.place(x=150, y=300, width=50, height=50)
    bt8 = Button(window, text=8,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(8, ent))
    bt8.place(x=200, y=300, width=50, height=50)
    bt9 = Button(window, text=9,
                 font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                 command=lambda: get_button(9, ent))
    bt9.place(x=100, y=350, width=50, height=50)
    bt_plus = Button(window, text='+',
                     font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                     command=lambda: get_button('+', ent))
    bt_plus.place(x=150, y=350, width=50, height=50)
    bt_minus = Button(window, text='-',
                      font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                      command=lambda: get_button('-', ent))
    bt_minus.place(x=200, y=350, width=50, height=50)
    bt_float = Button(window, text='.',
                      font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                      command=lambda: get_button('.', ent))
    bt_float.place(x=100, y=400, width=50, height=50)
    bt_mult = Button(window, text='*',
                     font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                     command=lambda: get_button('*', ent))
    bt_mult.place(x=150, y=400, width=50, height=50)
    bt_dev = Button(window, text=':',
                    font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                    command=lambda: get_button(':', ent))
    bt_dev.place(x=200, y=400, width=50, height=50)
    bt_del = Button(window, text='CE',
                    font=('TimesNewRoman', 20, 'bold'), bg='red', fg='green', bd=5,
                    command=lambda: del_all(ent))
    bt_del.place(x=250, y=200, width=50, height=50)
    bt_del = Button(window, text='<=',
                    font=('TimesNewRoman', 20, 'bold'), bg='red', fg='green', bd=5,
                    command=lambda: del_last(ent))
    bt_del.place(x=250, y=250, width=50, height=50)
    bt_res = Button(window, text='=',
                    font=('TimesNewRoman', 24, 'bold'), bg='red', fg='green', bd=5,
                    command=lambda: get_text(ent))
    bt_res.place(x=250, y=300, width=50, height=150)


btn = Button(window, text='Начать', command=pressed)
btn.pack()
window.mainloop()

# under_name = Entry(window, width=10, fg='orange', bd=10)
# under_name.pack(x=400, y=20)
# under_name.pack(side=LEFT)
# under_name.place(x=400, y=20)
