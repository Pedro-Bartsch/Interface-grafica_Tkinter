from tkinter.filedialog import askopenfilename
import pandas as pd

caminho_arquivo = askopenfilename(title = "Selecione um arquivo em excel para abrir")

df = pd.read_excel(caminho_arquivo)

print(df)
