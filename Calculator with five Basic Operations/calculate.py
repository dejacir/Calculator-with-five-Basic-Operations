#====DM.Dev======

from tkinter import *
import math

def calculates():
    which_button = selected_operation.get()
    value_1 = float(entry_field__1.get())
    value_2 = float(entry_field__2.get())
    if which_button == 1:
        resultado = value_1 + value_2
    elif which_button == 2:
        resultado = value_1 - value_2
    elif which_button == 3:
        resultado = value_1 * value_2
    elif which_button == 4:
        resultado = value_1 / value_2
    elif which_button == 5:
        resultado = value_1 /100 * value_2

    result_field.delete(0, END)
    result_field.insert(0, resultado)

janela = Tk()
janela.title('Calculator with five Basic Operations')
janela.geometry("400x300+300+200")
janela.configure(background="gray")


window_title = Label(janela, text='DM.Dev', foreground="white",  bg="green", font=('Arial',12)).grid(row=0, column=0,columnspan=3, pady=4)

lb_1 = Label(janela, text='Digite um número', bg="yellow").grid(row=1, column=0, pady=4)
entry_field__1 = Entry(janela, text='Número 1', width=11)
entry_field__1.grid(row=1, column=1, pady=4)

lb_2 = Label(janela, text='Digite outro número',bg="yellow").grid(row=2, column=0, pady=4)
entry_field__2 = Entry(janela, text='Número 2', width=11)
entry_field__2.grid(row=2, column=1, pady=4)

selected_operation = IntVar()

lb_3 = Label(janela, text='Escolha a operação desejada', foreground="yellow",bg="gray").grid(row=3, column=0, columnspan=3, pady=4)

sum_button = Radiobutton(janela, text='+', variable=selected_operation, value=1)
sum_button.grid(row=4, column=0, pady=4)

subtraction_button = Radiobutton(janela, text='-', variable=selected_operation, value=2)
subtraction_button.grid(row=4, column=1)

multiplication_button = Radiobutton(janela, text='x', variable=selected_operation, value=3)
multiplication_button.grid(row=5, column=0, pady=4)

division_button = Radiobutton(janela, text='/', variable=selected_operation, value=4)
division_button.grid(row=5, column=1, pady=4)

percentage_button = Radiobutton(janela, text='%', variable=selected_operation, value=5)
percentage_button.grid(row=4, column=2)

botao = Button(janela, text='Calcular operação',fg="red", command=calculates, width='30').grid(row=7, column=0, columnspan=2, pady=4)

lb_4 = Label(janela, text='Resultado').grid(row=8, column=0, pady=4)

result_field = Entry(janela)
result_field.grid(row=8, column=1, pady=4)

janela.mainloop()
