from functions.interfaces.input_Texto_dinamico import *



teste = input_texto_dinamico("asdasd")

print(type(teste))
if teste.strip() == "":
    print('deu certo')