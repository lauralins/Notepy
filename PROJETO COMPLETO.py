#baixa o pipe e depois o modulo smtplib
#importação dos modulos necessários
import pandas as pd
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt
from datetime import date
import time
from time import time, sleep
import pandas as pd
import numpy as np



def notpy_menu():
    """

    Esta função possui o objetivo de exibir para o operador as operações que este programa pode executar, esta função não usa
    argumentos.

    """
    print("Seja bem-vindo ao Notpy!")
    print("Por favor, escolha uma opção:\n[1] Cadastrar processo\n[2] Consultar processo\n[3] Alterar ou excluir licença \n[4] Sair do Notpy")
    opcao = input() #Opção escolhida pelo operador
    return opcao
   

def notpy():
    """
    Essa função garante o funcionamento do programa, pois ela é responsável por solicita do usuário as operações que ele deseja
    executar, chamar cada uma das funções e criar condições para sua execução. Nela, é criado um dataframe 'banco' a partir do arquivo
    'pindorama.csv' e definido 'Numero da licença' com index. Retorna o dataframe 'banco'.

    """
    banco = pd.read_csv(r'pindorama.csv', index_col='numero licenca')
    while True:
        opcao = notpy_menu()
        if opcao == "4":
            print("Programa encerrado!")
            break #interrompe a execução do programa
        elif (opcao == "1"):
            b = cadastro_licenca(banco)
        elif (opcao == "2"):
            b = consulta(banco)
        elif (opcao == "3"):
            b = altera(banco)
        else: #Caso o operador digite um número que não faça parte das opções de funções do Notpy
               print("Função inválida! Por favor, digite '1' para cadastro, '2' para consulta ou '3' para sair do programa.")

    return banco


def cadastro_licenca(banco):
    """

    Essa função é responsavel por cadastrar as licenças desejadas e guarda-las em um dataframe criado a partir de
    uma arquivo csv que contém as colunas do dataframe. Ela recebe o dataframe como argumento e retorna atualizado.

    """
    n_licenca = input('Digite o numero da licença:')
    org_responsavel = input('Digite o orgão responsavel:')
    d_emissao = input('Digite a data de emissão no formato ddmmaaaa:')
    d_vencimento = input('Digite a data de vencimento no formato ddmmaaaa:')
    condicional = int(input('Digite de quanto em quantos dias deseja receber o aviso(Ex.: 30):'))

    banco=banco.append({"numero licenca":n_licenca,
              "orgao responsavel":org_responsavel,
              "data emissao":d_emissao,
              "data vencimento":d_vencimento,
              "condicionante":condicional},ignore_index=True)
    print("Cadastro realizado!")
    
    return banco

def consulta(banco):
    """

    Essa função é responável pela consulta do banco de dados. Ela recebe o dicionario 'info' - um dicionario de
    dicionarios, que tem como chave o número da licença -, o dataframe 'banco' e vai buscar dentro do dicionário a
    licença desejada através dos métodos de busca em um dicionario.

    """


    print("Digite [1] para consultar uma licença \nDigite [2] para visualizar todas as licenças cadastradas.")
    lista = []
    for licenca in banco.index:
        lista.append(licenca)
    esc = int(input())
    if esc == 1:
        l_desejado = int(input("Digite o número da licença desejada:"))
        if l_desejado in lista:
            local = banco.loc[l_desejado]
        else:
            print("Error: licença não encontrada")
    elif esc == 2:
        print(banco)
    else:
        print("Error: escolha uma opção válida.")


def altera(banco):
    """

    Essa função recebe o dataframe 'banco' como argumento e pede ao usuário o numero da licença que ele deseja alterar
    ou excluir, depois verifica se ela está em 'banco'. Se estiver, pede ao usuário o item que deseja ser alterado, localiza
    ele dentro de 'banco' e faz a alteração; se a escolha for por excluir, o metodo 'drop' exclui a licença pelo index dado.
    Retorna 'banco'.

    """     

    indice = ['orgao responsavel','data emissao','data vencimento','condicionante']
    esco = input('Digite "E" para excluir ou "A" para alterar:')
    alter = int(input('Digite o número da licença:'))
    lista = []
    for licenca in banco.index:
        lista.append(licenca)
    if esco == "A":
        if alter in lista:
            chave = input('Digite qual tópico você deseja alterar exatamente como está descrito no cadastro:')
            if chave in indice:
                novo = input('Digite a alteração:')
                alterado = banco.loc[alter,chave]=novo
                print('Alteração realizada com sucesso!')
            else:
                print('Error: licença não encontrada.')
        else:
            print('Error: licença não encontrada.')
    elif esco == "E":
        if alter in lista:
            banco = banco.drop(alter)
            print ('Licença excluída.')
        else:
            print('Error: licença não encontrada.')
        
    return banco


#informações para o envio do email
MY_ADDRESS = 'cooperativapindorama2019@gmail.com'
PASSWORD = 'Cp123456'

def contatos(filename):
    """
    Retorna duas listas names e emails que conta os nomes e os enderessos
    de email lidos de um arquivo com nome especifico.
    """
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contato in lista_contatos:
            emails.append(contato)
        return emails
def licenca(banco,i):
    """
    Essa função verifica o dataframe e faz uma lista como todos os seus 'index'. Neste caso, definimos o index do dataframe
    como os numeros das licenças cadastradas. Recebe o dataframe 'banco' como argumento e retorna a lista 'licencas'
    """
    licencas = []
    licencas.append(banco.index)
    licenca_escolhida = []
    for j in licencas:
        if i == j:
            licenca_escolhida.append(j)       
    
    return licenca_escolhida

def read_template(filename):
    """
    Retorna um 'objeto Template', que vai formar o corpo do email recebendo os
    dados de um arquivo especificado.
    """
    with open(filename, 'r', encoding='ISO 8859-1') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    """
    Essa função é responsável pela montagem e envio do email.
    """
    emails = contatos('lista.txt') # lê os contatos
    licenca_escolhida = licenca(banco,i)
    message_template = read_template('email.txt')
    # configura o servidor SMTP
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    # envia o email para cada contato
    for lincenca, email in zip(licenca_escolhida, emails):
        # cria a mensagem
        msg = MIMEMultipart()
        # personalisa o template 
        message = message_template.substitute(N_LICENCA=licenca.title())
        print(message) # 'printa' a mensagem para teste 
        # configura os parâmetros do email 
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Situação da licença"
       # adiciona o conteudo na mensagem
        msg.attach(MIMEText(message, 'plain'))
        # envia a mensagem através do servidor configurado anteriormente.
        s.send_message(msg,env_email(envio_time))
    s.quit()
def env_email(envio_time):
    """ Essa função é responsável por calcular o tempo de envio de cada email. Recebe como
    uma variavel de data."""
    start = time() # faz o programa trabalhar em segundo plano
    data = datas(banco)
    while (time() - start < n):
        sleep(n - (time() - start))
    main()

def datas(banco):
    """
    Calcula as datas para envio do email. recebe como parametro o daframe 'banco' e retorna  a variável 'envio_time'.
    """
    hoje = date.today()
    for i in range(len(banco)):
        condicional = banco.loc[i]['condicionante']
        data_emissao=banco[i]['data emissao']
        data_vencimento = banco [i]['data vencimento']
        #formata a data para o modelo DD-MM-AAAA
        data1 = datetime.datetime.strptime(data_emissao, '%d-%m-%y')
        data2 = datetime.datetime.strptime(data_vencimento, '%d-%m-%y')
        #calcula o intervalo d etempo entre os emails
        intervalo = dt.timedelta(seconds=3600*24*condicional)
        #calcula a distancia da data atual até o vencimento
        calcula = data2 - hoje
        primeiro_email = data1 + intervalo
        
        envio_mail = primeiro_email
    while True:
        if calcula <= intervalo:
            licenca(i)
            env_email(envio_time)
            envio_time = envio_time + intervalo
        else:
            break
    return envio_time
        
 






#-----------------------------------------------------------------------------------------------------------------------------
notpy()
