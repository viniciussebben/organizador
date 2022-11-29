"""
Programa: organizador
Requisitos: organizar arquivos em pastas de acordo com a extensão (planilhas ou documentos).
Autor: Vinicius Ferreira Sebben
Data: 29/11/2022
Versão: 0.0.4
"""

# entrada de dados
# importar biblioteca OS - para automação
import os

# procurar a pasta para extensão docx    
if os.path.exists('documentos') == False:
    os.mkdir('documentos') # mkdir para criar pasta

# procurar a pasta para extensão xlsx    
if os.path.exists('planilhas') == False:
    os.mkdir('planilhas') # mkdir para criar pasta

# importar biblioteca SHUTIL - para cópia e rmeoção de arquivos
import shutil


# processamento de dados
arquivos = os.listdir()

for arquivo in arquivos:
    if ".xlsx" in arquivo:
        shutil.move(arquivo, f"./planilhas/{arquivo}")
    elif ".docx" in arquivo:
        shutil.move(arquivo, f"./documentos/{arquivo}")   
        
lista = os.listdir()

# saída de dados
print(lista)
