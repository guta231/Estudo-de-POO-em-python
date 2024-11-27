import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("900x600")

root.configure(bg="gray")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)



def soma():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado_soma = num1 + num2
    label.config(text=resultado_soma)

def sub():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado_sub = num1 - num2
    label.config(text=resultado_sub)

def multi():

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado_multiplicacao = num1*num2
    label.config(text=resultado_multiplicacao)

def div():

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado_divisao = num1/num2
    label.config(text=resultado_divisao)

entrada1 = tk.Entry(root, width=25)
entrada2 = tk.Entry(root, width=25)
entrada1.grid(row=0, column=1)
entrada2.grid(row=0, column=2)
button_soma = tk.Button(root, text="Somar", command=soma, width=25)
button_subtracao = tk.Button(root, text="Subtrair", command=sub, width=25)
button_multiplicacao = tk.Button(root, text="Multiplicar", command=multi, width=25)
button_divisao = tk.Button(root, text="Dividir", command=div, width=25)
button_divisao.grid(row=1, column=0, padx=15)
button_multiplicacao.grid(row=1, column=1, padx=15)
button_subtracao.grid(row=1, column=2, padx=15)
button_soma.grid(row=1, column=3, padx=15)
label = tk.Label(root, bg="gray")
label.grid(row=2, column=2)








root.mainloop()