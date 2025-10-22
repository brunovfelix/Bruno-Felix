#IMPORTAR AS FUNÇÕES NECESSÁRIAS

from dataclasses import dataclass
from enum import Enum, auto
from os import system

#CRIANDO CLASSES NECESSÁRIAS PARA USUÁRIOS, PAGAMENTOS E VENDAS 

class Usuarios (Enum) : 
    Aluno = auto() 
    Servidores_menor_tres_salarios = auto()
    docentes = auto()
    Servidores_maior_tres_salarios = auto()
    Externo = auto()

class Pagamento (Enum):
    Dinheiro = auto()
    PIX = auto()
    Cartão = auto() 

@dataclass
class Vendas ():
    Usuario : Usuarios
    Quant_tiquetes : int
    forma_pagamento : Pagamento
    receita_por_venda : int


#LISTA PARA ARMANEZENAR TODAS AS VENDAS 
list_vendas =[]

#FUNÇÃO PRINCIPAL, PARA FUNCIONALIDADE DO SISTEMA 
def main () :
    açao = '0'
    while açao != '3' :
        print('')
        print('==============================================================================')
        print('')
        print('                                  CONTROLE RU                  ')
        print('')
        print('==============================================================================')

        açao = input(' [ 1 ] - REGISTRAR VENDA \n [ 2 ] - EXIBIR RELATÓRIO \n [ 3 ] - SAIR \n\n O que deseja fazer  :   ')
        print('')
        system('clear')


        if açao == '1' : 

            print('')
            print('==============================================================================')
            print('')
            print('                              REGISTRAR VENDAS                 ')
            print('')
            print('==============================================================================')
            
            print('')
            usu = input(' \n [01] - Aluno \n [02] - Servidores menores que 3 salários  \n [03] - Servidores maiores que 3 salários  \n [04] - docente \n [05] - Cliente externo \n\n Qual o tipo de usuario : ')
            system('clear')

            if usu == '01' : 
                usuario = Usuarios.Aluno
                print('USUARIO SELECIONADO = ALUNO')
                valor_tiquete = 5
                print('')
                print('Valor do tíquete para o usuário : ', valor_tiquete)
                print('')
                

            elif usu == '02' : 
                usuario = Usuarios.Servidores_menor_tres_salarios
                print('USUARIO SELECIONADO = SERVIDORES COM MENOS DE 3 SALÁRIOS')
                valor_tiquete = 5
                print('')
                print('Valor do tíquete para o usuário : ', valor_tiquete)
                print('')
                
                
            elif usu == '03' : 
                usuario = Usuarios.Servidores_maior_tres_salarios
                print('USUARIO SELECIONADO = SERVIDORES COM MAIS DE 3 SALÁRIOS')
                valor_tiquete = 10
                print('')
                print('Valor do tíquete para o usuário : ', valor_tiquete)
                print('')
                
            elif usu == '04' : 
                usuario = Usuarios.docentes
                print('USUARIO SELECIONADO = DOCENTES')
                valor_tiquete = 10
                print('')
                print('Valor do tíquete para o usuário : ', valor_tiquete)
                print('')
                
            elif usu == '05' :
                usuario = Usuarios.Externo
                print('USUARIO SELECIONADO =  COMUNIDADE EXTERNA')            
                valor_tiquete = 19
                print('')
                print('Valor do tíquete para o usuário : ', valor_tiquete)
                print('')
                
            else : 
                print('')
                print('Digite apenas os códigos descritos ( 01, 02, ...)')
                print('')
                açao = '3'

            quant_tiquetes = int(input('Qual a quantidade de tíquetes : '))
            valor_total = valor_tiquete * quant_tiquetes
            
            print('')
            print('O valor total da compra é de : ', valor_total, 'R$')
            print('')
            print('')
            
            forma_pagamento = input(' [01] - Dinheiro \n [02] - Cartão \n [03] - PIX \n\n Qual a forma de pagamento : ')
            print('')
            print('')

            if forma_pagamento == '01' : 
                pag = Pagamento.Dinheiro
                
            elif forma_pagamento == '02' :
                pag = Pagamento.Cartão
                
            elif forma_pagamento == '03' : 
                pag = Pagamento.PIX

            else : 
                print('')
                print('')
                print('DIGITE APENAS OS CÓDIGOS DESCRITOS !')   
                print('')
                print('')
                açao ='3'

            
            venda = Vendas(usuario, quant_tiquetes, pag, valor_total )
            list_vendas.append(venda) 
            print('')
            print('')
            print('Venda Adicionada !!')
            print('')
            print('')
            input('Tecle ENTER para voltar ao menu inicial ')
            system('clear')

        elif açao == '2' :
            print('')
            print('==============================================================================')
            print('')
            print('                                RELATÓRIO                 ')
            print('')
            print('==============================================================================')

            
            
            print('')
            print('A quantidade de tíquetes vendidos é  : ', quantidade_tiquetes(list_vendas), ' unidades')
            print('')
            print('')
            print('A receita total foi : ', receita_total(list_vendas), ' R$')
            print('')

            print('==========================================================================')
            print('')
            print('          PORCENTAGEM DE TÍQUETES VENDIDOS PARA CADA USUÁRIO  ')
            print('')
            print('==========================================================================')
            print('')
            print('')                
           
           
            print(grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario(list_vendas, Usuarios.Aluno ), Usuarios.Aluno))
            print('')
            print(grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario(list_vendas, Usuarios.Servidores_maior_tres_salarios ), Usuarios.Servidores_maior_tres_salarios))
            print('')
            print(grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario(list_vendas, Usuarios.Servidores_menor_tres_salarios ), Usuarios.Servidores_menor_tres_salarios))
            print('')
            print(grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario(list_vendas, Usuarios.docentes ), Usuarios.docentes))
            print('')
            print(grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario(list_vendas, Usuarios.Externo ), Usuarios.Externo))
            print('')
            print('')

            print('==============================================================================')
            print('')
            print('             PORCENTAGEM FORMA DE PAGAMENTO POR RECEITA OBTIDA')
            print('')
            print('==============================================================================')

            print(grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento(list_vendas, Pagamento.PIX), Pagamento.PIX))
            print('')
            print(grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento(list_vendas, Pagamento.Cartão), Pagamento.Cartão))
            print('')
            print(grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento(list_vendas, Pagamento.Dinheiro), Pagamento.Dinheiro))
            print('')
            print('')

            input('Tecle ENTER para voltar ao menu inicial ')
            system('clear')

        elif açao == '3' :
            açao =='3'    
        else : 
            print('')
            print('DIGITE APENAS OS CÓDIGOS DESCRITOS ! ' )
            print('')
            print('')
            input('Tecle ENTER para continuar')
            system('clear')
                

#FUNÇÃO QUE CÁLCULA A QUANTIDADE TOTAL DE TÍQUETES VENDIDOS

def quantidade_tiquetes( list_vendas : list[Vendas]) -> int :
    '''
    Dado a lista com todas as vendas, calcula a quatidade total de tíquetes

    >>> quantidade_tiquetes([Vendas(Usuarios.Aluno, 45, Pagamento.PIX, 225), Vendas(Usuarios.docentes, 5, Pagamento.Cartão, 50), Vendas(Usuarios.Externo, 2, Pagamento.Dinheiro, 38)])
    52
    >>> quantidade_tiquetes([Vendas(Usuarios.Aluno, 2, Pagamento.PIX, 10), Vendas(Usuarios.docentes, 1, Pagamento.Cartão, 10), Vendas(Usuarios.Externo, 5, Pagamento.Dinheiro, 95)])
    8
    >>> quantidade_tiquetes([Vendas(Usuarios.Servidores_menor_tres_salarios, 0, Pagamento.PIX, 0), Vendas(Usuarios.docentes, 100, Pagamento.Cartão, 1000), Vendas(Usuarios.Externo, 250, Pagamento.Dinheiro, 4750)])
    350
    '''
    
    cont = 0
    for item in list_vendas :
        cont = cont + item.Quant_tiquetes   
    return cont

#FUNÇÃO QUE CÁLCULA A RECEITA TOTAL OBTIDA

def receita_total ( list_vendas : list[Vendas]) -> int : 
    '''
    Dado a lista com todas as vendas, calcula a receita total obtida 

    >>> receita_total([Vendas(Usuarios.Servidores_menor_tres_salarios, 50, Pagamento.PIX, 250), Vendas(Usuarios.docentes, 100, Pagamento.Cartão, 1000), Vendas(Usuarios.Externo, 250, Pagamento.Dinheiro, 4750)])
    6000
    >>> receita_total([Vendas(Usuarios.Aluno, 50, Pagamento.PIX, 100000), Vendas(Usuarios.Aluno, 100, Pagamento.Cartão, 100000), Vendas(Usuarios.Aluno, 250, Pagamento.Dinheiro, 800000)])
    1000000
    >>> receita_total([Vendas(Usuarios.Servidores_menor_tres_salarios, 0, Pagamento.PIX, 0), Vendas(Usuarios.docentes, 0, Pagamento.Cartão, 0), Vendas(Usuarios.Externo, 0, Pagamento.Dinheiro, 0)])
    0
    '''

    receita_total = 0 
    for item in list_vendas :
        receita_total = receita_total + item.receita_por_venda
    return receita_total

#FUNÇÃO QUE CÁLCULA A PORCENTAGEM DE TÍQUETES POR USUARIO 

def porcentagem_relativa_usuario( list_vendas : list[Vendas], usu : Usuarios) -> int  :
    '''
    Dado a lista de vendas, calcula a porcentagem de tiquetes adquiridos relativa ao usuario selecionado 

    >>> porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 50, Pagamento.PIX, 100000), Vendas(Usuarios.Aluno, 100, Pagamento.Cartão, 100000), Vendas(Usuarios.Aluno, 250, Pagamento.Dinheiro, 800000)], Usuarios.Aluno)
    100
    >>> porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 1, Pagamento.PIX, 5), Vendas(Usuarios.Aluno, 2, Pagamento.Cartão, 10), Vendas(Usuarios.Aluno, 8, Pagamento.Dinheiro, 40)], Usuarios.docentes)
    0
    >>> porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 50, Pagamento.PIX, 100000), Vendas(Usuarios.Aluno, 100, Pagamento.Cartão, 100000), Vendas(Usuarios.docentes, 100, Pagamento.Dinheiro, 800000), Vendas(Usuarios.Externo, 50, Pagamento.Dinheiro, 0)], Usuarios.Aluno)
    50
    >>> porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 1, Pagamento.PIX, 5), Vendas(Usuarios.docentes, 9, Pagamento.Cartão, 90)], Usuarios.Aluno)
    10
    '''
    
    quat_tiquete = 0
    for item in list_vendas :
        
        if item.Usuario == usu :
            quat_tiquete += item.Quant_tiquetes 
    
    porcentagem= round((quat_tiquete / quantidade_tiquetes(list_vendas) ) * 100) 
    return porcentagem

#FUNÇÃO QUE CÁLCULA A PORCENTAGEM DE RECEITA POR FORMA DE PAGAMENTO

def porcentagem_receita_forma_pagamento ( list_vendas : list[Vendas], forma_pag :Pagamento ) -> int : 
    '''
    Dado a lista de vendas, calcula a porcentagem da receita total relativa a forma de pagamento
    >>> porcentagem_receita_forma_pagamento([Vendas(Usuarios.Servidores_maior_tres_salarios, 5, Pagamento.PIX, 50), Vendas(Usuarios.docentes, 15, Pagamento.Cartão, 150)], Pagamento.Cartão) 
    75
    >>> porcentagem_receita_forma_pagamento([Vendas(Usuarios.Servidores_menor_tres_salarios, 8, Pagamento.PIX, 40), Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60)], Pagamento.Dinheiro)  
    60
    >>> porcentagem_receita_forma_pagamento([Vendas(Usuarios.Externo, 5, Pagamento.PIX, 95), Vendas(Usuarios.Servidores_menor_tres_salarios, 1, Pagamento.Cartão, 5)], Pagamento.PIX)
    95
    >>> porcentagem_receita_forma_pagamento([Vendas(Usuarios.Externo, 1, Pagamento.Dinheiro, 19)], Pagamento.Dinheiro)
    100
    >>> porcentagem_receita_forma_pagamento([Vendas(Usuarios.Externo, 1, Pagamento.Dinheiro, 19)], Pagamento.PIX)
    0
    '''

    receita = 0 
    for item in list_vendas :
        if item.forma_pagamento == forma_pag :
            receita = receita + item.receita_por_venda
    
    porcentagem_receita = round((receita / receita_total(list_vendas)) * 100)
    
    return porcentagem_receita

#FUNÇÕES QUE CÁLCULAM OS GRAFICOS HORIZONTAIS

def grafico_horizontal_usuario_tiquete( num : int, cliente : Usuarios) -> str:
    '''
    Dado a porcentagem de tiquetes relativa ao usuario, monta um gráfico na horizontal

    >>> grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60)], Usuarios.Aluno ), Usuarios.Aluno)
    'Aluno                                   [=========================]   100%'
    >>> grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60)], Usuarios.docentes ), Usuarios.docentes)
    'docentes                                []                            0%'
    >>> grafico_horizontal_usuario_tiquete(porcentagem_relativa_usuario([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60), Vendas(Usuarios.Externo, 8, Pagamento.PIX, 152)], Usuarios.Externo ), Usuarios.Externo)
    'Externo                                 [==========]                  40%'
    '''
    num = round((num * 25) / 100)
    quant_iguais = '=' * num

    linha_grafico = '[' + quant_iguais + ']'
    linha_grafico_formatada = "{:<30}".format(linha_grafico)
    usuario_grafico_formatado = "{:<40}".format(cliente.name)
    porcentagem_grafico = str(num * 4)  # Reverter a conversão de linha 313

    linha_final = usuario_grafico_formatado + linha_grafico_formatada + porcentagem_grafico + '%'
    return linha_final

def grafico_horizotal_pagamento_renda(num : int, pagamento : Pagamento) -> str : 


    '''
    Dado a porcentagem de tiquetes relativa ao usuario, monta um gráfico na horizontal

    >>> grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60)], Pagamento.Dinheiro ), Pagamento.Dinheiro)
    'Dinheiro                                [=========================]   100%'
    >>> grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60)], Pagamento.PIX ), Pagamento.PIX)
    'PIX                                     []                            0%'
    >>> grafico_horizotal_pagamento_renda(porcentagem_receita_forma_pagamento([Vendas(Usuarios.Aluno, 12, Pagamento.Dinheiro, 60), Vendas(Usuarios.Externo, 8, Pagamento.Cartão, 152)], Pagamento.Cartão ), Pagamento.Cartão)
    'Cartão                                  [==================]          72%'
      
    '''
    num = round((num * 25) / 100)
    quant_iguais = '=' * num

    linhas_grafico = '[' + quant_iguais + ']'
    linhas_grafico_formatada = "{:<30}".format(linhas_grafico)
    forma_pagamento_grafico_formatado = "{:<40}".format(pagamento.name)
    porcentagem_grafico = str(num * 4)  # Reverter a conversão de linha 331

    linha_final = forma_pagamento_grafico_formatado + linhas_grafico_formatada + porcentagem_grafico + '%'
    return linha_final

if __name__ == '__main__':
    main()
