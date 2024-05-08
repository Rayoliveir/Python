"""
Elabore um algoritmo para receber o login e senha de um usuario.
Caso o usuário e senha estejam corretos, mostre a mensagem
"Bem-vindo!", caso contrário, mostre a mensagem "Login ou senha
inválidos." 
"""

import os
os.system("cls || clear")

login = input("Informe seu login: ")
senha = input("Informe a sua senha: ")

if login == "marcelly" and senha =="123456":
    print("Bem-Vindo")
else:
    print("Login ou senha inválidos")