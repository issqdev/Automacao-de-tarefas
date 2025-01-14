# pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.3

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.press -> pressionar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> combinação de teclas (ctrl, C)

# Passo 1: Abrir o sistema da empresa

# abrir o google chrome
# apertar a tecla 'win'
pyautogui.press("win")

# digitar o texto 'chrome'
pyautogui.write("chrome")

# apertar 'enter'
pyautogui.press("enter")

# escolher usuário do google chrome
pyautogui.click(x=868, y=470)

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pedir pro computador esperar 3 segundos
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de 'email'
pyautogui.click(x=682, y=373)
# escrever o seu email
pyautogui.write("isaqueoliv.dev@gmail.com")
# passando pro próximo campo
pyautogui.press("tab")
pyautogui.write("suasenha")
# clique no botao de login
pyautogui.press("tab")
pyautogui.press("enter")


# Passo 3: Importar a base de dados dos produtos
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)


# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=681, y=257) # clica no 1° campo

    # codigo
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo em string
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # str -> string = texto
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter") # apertar o botão de 'enviar'

    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000)


# Passo 5: Repetir o passo 4 até acabar todos os produtos

# nan = valor vazio em uma base de dados
# Not a Number