from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = Tk()
window.title('Text Editor')
window.geometry('900x700+500+150')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = '#6A5ACD'


def save_file():
    file_name = fd.asksaveasfilename(defaultextension='')

    with open(file_name, 'w') as f:
        f.write(text.get(0.0, END))


def clean_text():
    text.delete(1.0, END)


def show_info():
    input_place = text.get(0.0, END)
    quan_proposal = list(text.get(0.0, END))
    for i in range(len(quan_proposal) - 1):
        if quan_proposal[i] == '.' and quan_proposal[i + 1] != '.':
            quan_proposal[i] = '. '
    showinfo(title='Информация', message=f'Кол-во слов: {len(input_place.split())}\nКол-во символов: {len(input_place) - 1}\nКол-во строк: {int(text.index("end").split(".")[0]) - 1}\n'
                                         f'Кол-во предложений: {quan_proposal.count("?") + quan_proposal.count(". ") + quan_proposal.count("...") + quan_proposal.count("!")}')


def change_color(event):
    text['fg'] = color.get()


save = Button(window, text='Сохранить',
              font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5, command=save_file)
save.place(x=20)

clean = Button(window, text='Очистить',
               font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5, command=clean_text)
clean.place(x=400)

info = Button(window, text='Инфо',
              font=('TimesNewRoman', 12, 'bold'), bg='#8A2BE2', fg='#FFFFFF', bd=5, command=show_info)
info.place(x=800)

text = Text(window, fg='black', width=95, height=30, bd=10, font=('TimesNewRoman', 12, 'bold'))
text.place(x=10, y=100)

scrollbar = ttk.Scrollbar(orient="vertical", command=text.yview)
scrollbar.place(x=870, y=100)

text['yscrollcommand'] = scrollbar.set

color = ttk.Combobox(window, values=['black', 'blue', 'orange'], font=('TimesNewRoman', 12, 'bold'), state="readonly")
color.current(0)
color.place(y=50)

color.bind_all('<<ComboboxSelected>>', change_color)

window.mainloop()
