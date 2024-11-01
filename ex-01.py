import tkinter as tk
from tkinter import ttk
janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight = 1)
janela.columnconfigure(0, weight = 1)

mensagem = tk.Label(text = "Sistema de Busca de Cotação de Moedas", fg='white', bg ='#7301F5', width = 35, height = 5)
mensagem.grid(row = 0 , column = 0, columnspan = 2, sticky = "NSEW")

mensagem2 = tk.Label(text = " Selecione a moeda desejada") #fg ='white', bg= '#F5AC5B' , height = 15, width = 70)
mensagem2.grid(row = 1, column = 0)

mensagem3 = tk.Label(text = "Caso você queira pegar mais de 1 cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem2.grid(row = 4, column = 0, columnspan = 2)

moeda = tk.Entry()
moeda.grid(row = 1, column = 1)

caixa_texto = tk.Text (width = 10, height = 5)
caixa_texto.grid(row = 5, column = 0 , sticky = 'nsew')

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values = moedas)
moeda.grid (row = 1, column = 1)

def buscar_cotacao():
    moeda_preenchida = (moeda.get())
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text = "Cotação não encontrada", fg = 'red')
    mensagem_cotacao.grid(row = 3, column = 0, sticky= 'nsew')
    if cotacao_moeda:
        mensagem_cotacao ['text'] = f'Cotação do {moeda_preenchida} é de R${cotacao_moeda} reais' 
    else:
       mensagem_cotacao ['text'] = ("Cotação não encontrada")
            
def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item} : R${cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row = 6, column = 1)

botao = tk.Button(text = "Buscar Cotação", command = buscar_cotacao)
botao.grid(row = 2, column = 1)
botao2 = tk.Button(text = "Buscar Cotações", command = buscar_cotacoes)
botao2.grid(row = 5, column = 1)

janela.mainloop()
