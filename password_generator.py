import string
import random
import csv
import os

def gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais):
    caracteres = string.ascii_lowercase
    if usar_maiusculo:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha

def gerar_log(tamanho, usar_maiusculo, usar_numeros, usar_especiais, senha):
    if os.path.exists("log.csv"):
        with open("log.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            index = sum(1 for row in reader)
    else:
        index = 0
    
    with open("log.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([index, senha])

'''

def main():
    while(input("Deseja criar uma senha? (s/n): ").lower() == "s"):
    
        tamanho = int(input("Qual será o tamanho da senha? "))
        usar_maiusculo = input("Incluir letras maiusculas? (s/n)").lower() == "s"
        usar_numeros = input("Incluir números? (s/n)").lower() == "s"
        usar_especiais = input("Incluir caracteres especiais? (s/n)").lower() == "s"

        global senha
        senha = gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais)
        largura_decoradora = 38
        text = f"SENHA GERADA"
        print(
            f"""\n{"=" * largura_decoradora}
            \n{text.center(largura_decoradora)}
            \n{senha.center(largura_decoradora)}
            \n{"=" * largura_decoradora}"""
        )
        
        gerar_log(tamanho, usar_maiusculo, usar_numeros, usar_especiais)

if (__name__ == "__main__"):
    main()
'''
