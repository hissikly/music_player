from tkinter import *
from tkinter import ttk
import requests

url = 'https://api.exchangerate.host/symbols'
response = requests.get(url)
data = response.json()
data = data['symbols']


def convert():
    summ = input_summ.get()
    from_ = com.get()
    to = res.get()
    url = f'https://api.exchangerate.host/convert?from={from_}&to={to}&amount={summ}'
    response = requests.get(url)
    data = response.json()
    data = data['result']
    input_res.delete(0, END)
    input_res.insert(END, data)



valutes = list(data.keys())

window = Tk()
window.title('TEST')
window.geometry('600x400+800+300')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = 'yellow'

title = Label(window, text='Конвертер валют', fg='orange', bd=10, font=('TimesNewRoman', 24, 'bold'))
title.pack()
summ = Label(window, text='Сумма:', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
summ.place(x=50, y=100)
input_summ = Entry(window, width=10, fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
input_summ.place(x=200, y=100)

conv = Label(window, text='Конвертировать в', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
conv.place(x=50, y=200)

conv = Label(window, text='Результат:', fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
conv.place(x=50, y=300)
input_res = Entry(window, width=10, fg='orange', bd=10, font=('TimesNewRoman', 12, 'bold'))
input_res.place(x=200, y=300)

com = ttk.Combobox(window, values=valutes, font=('TimesNewRoman', 12, 'bold'), state="readonly")
com.place(x=350, y=110)
com.current(0)

res = ttk.Combobox(window, values=valutes, font=('TimesNewRoman', 12, 'bold'), state="readonly")
res.place(x=350, y=210)
res.current(0)

bt = Button(window, text='Провести конверт',
                      font=('TimesNewRoman', 12, 'bold'), bg='red', fg='green', bd=5,
                      command=convert)
bt.place(x=250, y=350, height=50)

window.mainloop()