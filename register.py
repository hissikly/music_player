from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.title('')
window.geometry('600x400+600+300')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = '#6A5ACD'

eye_img = PhotoImage(file='pictures/eye.png').subsample(25)


def sign_in():
    if len(input_password.get()) > 0 and len(input_login.get()) > 0:
        sup_window = Toplevel(window)
        sup_window.title('account')
        sup_window.geometry('500x300+800+300')

        label = Label(sup_window, text='Привет, друг', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
        label.pack()
    else:
        mb.showerror("Error", "Данные некорректны!")


def get_password():
    if input_password['show'] == '*':
        input_password['show'] = ''
    else:
        input_password['show'] = '*'


into = Button(window, text='Войти', command=sign_in)
into.place(x=280, y=220)

greeting = Label(window, text='Авторизация', fg='white', bd=10, font=('TimesNewRoman', 14, 'bold'), bg='#6A5ACD')
greeting.pack()

s = Label(window, text='', bd=10, font=('TimesNewRoman', 8, 'bold'), bg='#6A5ACD')
s.pack()

login = Label(window, text='Имя пользователя', fg='white', bd=10, font=('TimesNewRoman', 11, 'bold'), bg='#6A5ACD')
login.pack()

input_login = Entry(window, width=25, fg='black', bd=10, font=('TimesNewRoman', 12, 'bold'), borderwidth=1)
input_login.pack()

password = Label(window, text='Пароль', fg='white', bd=10, font=('TimesNewRoman', 11, 'bold'), bg='#6A5ACD')
password.pack()

input_password = Entry(window, show='*', width=25, fg='black', bd=10, font=('TimesNewRoman', 12, 'bold'), borderwidth=1)
input_password.pack()

check_password = Button(window, image=eye_img, command=get_password)
check_password.place(x=150, y=182)

window.mainloop()
