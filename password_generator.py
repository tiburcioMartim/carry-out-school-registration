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