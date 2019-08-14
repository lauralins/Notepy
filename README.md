# Notepy
Projeto de introdução a computação
import pandas as pd
import numpy as np

info = {'numero_licenca': [],'orgao_responsavel': [],'data_emissao_licenca': [], 'data_vencimento_licenca': [], 'condicionante':[]}
banco = pd.DataFrame(info)
def menu():
    escolha = int(input("Digite 1 para cadastrar ou 2 para consultar:") )
    if escolha == 1:
        cadastro()
    elif  escolha == 2:
        consulta()
    else:
        print("Error: escolha uma opc")
def cadastro():
    
