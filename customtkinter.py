from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import time

window = Tk()
window.title('custom')
window.geometry('700x500+550+200')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = '#6A5ACD'

#dasdsadasdsad
# def func(i):
#     print(i)
#
#
# for i in range(5):
#     bt = Button(window, text=i, command=lambda x=i: func(x))
#     bt.pack()
#
# window.mainloop()
# nb = ttk.Notebook(window, width=500, height=300)
#
# tab_1 = ttk.Frame(nb)
# nb.add(tab_1, text='Вкладка 1')
#
# tab_2 = ttk.Frame(nb)
# nb.add(tab_2, text='Вкладка 2')
#
# nb.place(x=100, y=100)
#
# text_1 = Label(tab_1, text='Первая вкладка')
# text_2 = Label(tab_2, text='Вторая вкладка')
# text_1.pack()
# text_2.pack()


canvas = Canvas(window, width=600, height=400, bg='yellow')
canvas.place(x=50, y=50)


# square = canvas.create_rectangle(25, 10, 45, 30, fill='green')
#
# def moving(event):
#     global square
#     coo = canvas.coords(square)
#
#     if event.keysym == 'w':
#         canvas.move(square, 0, -20)
#     if event.keysym == 's':
#         canvas.move(square, 0, 20)
#     if event.keysym == 'a':
#         canvas.move(square, -20, 0)
#     if event.keysym == 'd':
#         canvas.move(square, 20, 0)
#     if event.keysym == 'space':
#         canvas.delete("all")
#         square = canvas.create_rectangle(25, 10, 45, 30, fill='green')
#         return
#     square_coo = canvas.coords(square)
#     square = canvas.create_rectangle(square_coo[0], square_coo[1], square_coo[2], square_coo[3], fill='green')
#     canvas.create_rectangle(coo[0], coo[1], coo[2], coo[3], fill='white', outline='black')
#
#
# canvas.bind_all('<Key>', moving)

image = PhotoImage(file='pictures/amongus.png').subsample(10)
player = canvas.create_image(50, 50, anchor=NW, image=image)


def moving(event):
    if event.keysym == 'w':
        canvas.move(player, 0, -10)
    if event.keysym == 's':
        canvas.move(player, 0, 10)
    if event.keysym == 'a':
        canvas.move(player, -10, 0)
    if event.keysym == 'd':
        canvas.move(player, 10, 0)


canvas.bind_all('<Key>', moving)

window.mainloop()
