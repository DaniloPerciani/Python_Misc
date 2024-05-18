import pyautogui as gui
import pandas as pd
import time

portal = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
dados = pd.read_csv('C:\\Users\\Danilo\\Desktop\\Dev\\Python_Misc\\WindowsAutomation\\produtos.csv')

# abrir o navegador
gui.press('win')
time.sleep(1)
gui.write('chrome')
time.sleep(1)
gui.press('enter')
time.sleep(2)

# acessar o site
gui.write(portal)
gui.press('enter')
time.sleep(5)

# informar credenciais
gui.press('tab')
gui.write('my_username')
gui.press('tab')
gui.write('a!6b@9o##vr!')
gui.press('enter')
time.sleep(5)
gui.press('tab')

for i in dados.index:
    # preencher os dados
    gui.write(dados.loc[i, 'codigo'])
    gui.press('tab')

    gui.write(dados.loc[i, 'marca'])
    gui.press('tab')

    gui.write(dados.loc[i, 'tipo'])
    gui.press('tab')

    gui.write(str(dados.loc[i, 'categoria']))
    gui.press('tab')

    gui.write(str(dados.loc[i, 'preco_unitario']))
    gui.press('tab')

    gui.write(str(dados.loc[i, 'custo']))
    gui.press('tab')

    gui.write('' if pd.isna(dados.loc[i, 'obs']) else str(dados.loc[i, 'obs']))
    gui.press('tab')

    # confirmar e posicionar para o proximo registro
    gui.press('enter')
    time.sleep(1)
    gui.scroll(3000)
    gui.leftClick(100, 200)
    gui.press('tab')

