#passo a passo

 #1. abrir o sistema da empresa
 # https://dlp.hashtagtreinamentos.com/python/intensivao/login


# instalar pyautogui
import pyautogui
import time
# tempo de resposta em cada comando 
pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado  
#pyautogui.hotkey -> apertar um conjunto de teclas 

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
pyautogui.sleep(3)

 #2. fazer login
pyautogui.click(x=198, y=353)
pyautogui.write("mamadaloka@gmail.com")
pyautogui.press("tab")
pyautogui.write("chupameupaulatifa")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#posição do mouse
#time.sleep(6)
#print(pyautogui.position())

 #3. abrir e importar a base de dados de produtos para cadastrar
 # pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

#print(tabela)
 #4. cadastrar um produto
# str -> texto
for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    #clicar no campo do codigo do produto
    pyautogui.click(x=141, y=249)

    #preencher o codigo
    pyautogui.write(codigo)
    #passar pro proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)    
    # passar pro proximo campo
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

 #5. repetir tudo isso ate acabar a lista