import pyautogui
import time

pyautogui.PAUSE = 0.5
# Abrir o app email
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(3)

# escrevendo o email
pyautogui.click(x=133, y=170)

import pandas
tabela = pandas.read_csv("emails.csv")
print(tabela)

for linha in tabela.index:

    email = tabela.loc[linha, "Email"]
    assunto = tabela.loc[linha, "Assunto"]
    texto = tabela.loc[linha, "Texto"]

    pyautogui.write(str(email))
    pyautogui.press("enter")
    time.sleep(1)  
    pyautogui.press("tab")
    pyautogui.write(str(assunto))
    pyautogui.press("tab")
    pyautogui.write(str(texto))

    # envindo email
    # pyautogui.click(x=1309, y=1023) -> poderia ser por click, porém pra deixar o codigo funcionando em qualquer pc irei usar o comando
    pyautogui.hotkey("ctrl", "enter")
    pyautogui.click(x=133, y=170) # clicando denovo no botao de escrever