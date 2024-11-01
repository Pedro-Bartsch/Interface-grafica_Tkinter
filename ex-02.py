import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocional?", variable = var_promocoes)
checkbox_promocoes.grid(row = 0, column = 0)

janela.mainloop()