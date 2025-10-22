from dataclasses import dataclass
from time import sleep
import os
from filaLigada import *
from listaLigada import *

def main():
    '''Função principal para funcionamento do menu do sistema'''
    #Programa inicia
    print('='*50)
    print("")
    print(f'{"INICIALIZANDO O SISTEMA":^50}')
    print("")
    print('='*50)
    print("")

    print(f'{"["+"="*8+"]":<25}'+ "40%")
    sleep(1) #serve como um timer que congela o terminal, para fins estéticos
    
    print(f'{"["+"="*12+"]":<25}' +"60%")
    sleep(2)
    
    print(f'{"["+"="*20+"]":<25}'+"98%" )
    sleep(2)

    print(f'{"["+"="*22+"]":<25}'+"100%" )
    print("")
    
    print(f'{"SISTEMA PRONTO !":^50}')
    print("")
    continuar_operando = input("Tecle ENTER para iniciar:")
    
    os.system("cls") #Windowns -> serve para limpar o terminal, porém muda o comando dependendo do S.O
    #os.system('clear') #linux

    #Mensagem de opções
    print('='*50)
    print("")
    print(f'{"BEM VINDO !":^50}')
    print("")   
    print('='*50)
    global Qnt_caixas
    print("")
    print("DESEJA OPERAR COM QUANTOS CAIXAS :")
    print("")
    Qnt_caixas = int(input('(Escolha entre 2 e 20): '))
    if Qnt_caixas < 2 or Qnt_caixas > 20 : 
        print("")
        print(f'{"ERRO DE INICIALIZAÇÃO DE SISTEMA":^50}')
        print("")
        print("ESCOLHA APENAS ENTRE 2 E 20 !!")
        print("")
        continuar_operando = input("Tecle ENTER para iniciar o sistema novamente")
        os.system("cls")
        #os.system("clear")
        main()

    print("\nÓTIMO! VAMOS OPERAR COM", Qnt_caixas, "CAIXAS !")
    print("")
    continuar_operando = input("Tecle ENTER para iniciar: ")
    #Gerando Lista de caixas
    i=1
    while i <= Qnt_caixas:
        caixas.insereFim(Caixa(i,None))
        i+=1
    
    os.system("cls")
    #os.system('clear')

    acao = 0
    #looping de ações

    while acao != 5:    
        #sleep(2)
        print('='*50)
        print("")
        print(f'{"MENU PRINCIPAL":^50}')
        print("")
        print('='*50)

        print('\n[ 1 ] -> (GERAR SENHA) \n[ 2 ] -> (CHAMAR CLIENTE)\n[ 3 ] -> (CONSULTAR CLIENTES EM ESPERA) \n[ 4 ] -> (CONSULTAR SITUAÇÃO DOS CAIXAS)\n[ 5 ] -> (SAIR DO PROGRAMA)\n')
        acao = int(input('QUAL AÇÃO DESEJA REALIZAR: '))
        os.system("cls")
        #os.system('clear')

        if acao == 1:
            print("="*50)
            print("")
            print(f'{"GERAR SENHA":^50}')
            print("")
            print("="*50)
            GerarSenha()
        elif acao == 2:
            print("="*50)
            print("")
            print(f'{"CHAMAR CLIENTE":^50}')
            print("")
            print("="*50)
            ChamarCliente()
        elif acao == 3:
            print("="*50)
            print("")
            print(f'{"CLIENTES EM ESPERA":^50}')
            print("")
            print("="*50)
            Consultar_Clientes()
        elif acao == 4:
            print("="*50)
            print("")
            print(f'{"SITUAÇÃO DOS CAIXAS":^50}')
            print("")
            print("="*50)
            Consultar_Caixas()
        elif acao == 5 :
            print("="*50)
            print("")
            print(f'{"FOI UM PRAZER, VOLTE SEMPRE !":^50}')
            print("")
            print("="*50)
        else:
            print("="*50)
            print("")
            print(f'{"DIGITE APENAS OS CÓDIGOS CORRESPONDENTES !!":^50}')
            print("")
            print("="*50)
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            
def GerarSenha():
    '''Gera uma senha a partir do tipo de cliente, comum ou preferencial e incluindo o mesmo em sua devida fila'''
    global SenhaComum
    global SenhaPreferencial
    cliente = Cliente(0,0)
    tipo = int(input('\n[ 1 ] -> COMUM\n[ 2 ] -> PREFERENCIAL\n\nESCOLHA O TIPO DE SENHA: '))
    os.system("cls")
    #os.system('clear')

    #Comum
    if tipo == 1:
        qnt_zeros = "" 
        if SenhaComum < 10 :
            qnt_zeros = "00"
        elif SenhaComum > 10 : 
            qnt_zeros = "0" 
        elif SenhaComum > 99 :
            qnt_zeros = ""
        
        print("")
        print('SUA SENHA -> '+qnt_zeros + str(SenhaComum + 1))
        print("")
        yesorno = input("DESEJA CRIAR A SENHA ? (s/n) ")
        if yesorno == "s":
            SenhaComum += 1
            cliente.tipo = 1
            cliente.senha = SenhaComum
            print("\nSENHA GERADA !\n") 
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
            fila_Comum.enfileira(cliente)
        elif yesorno == "n" :
            print("\nCRIAÇÕA DE SENHA CANCELADA!\n")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
        else : 
            print("")
            print(f'{"ERRO DE RESPOSTA ERRADA !":^50}')
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
            
    #Preferencial
    elif tipo == 2:
        qnt_zeros = "" 
        if SenhaPreferencial < 10 :
            qnt_zeros = "00"
        elif SenhaPreferencial > 10 : 
            qnt_zeros = "0" 
        elif SenhaPreferencial > 99 :
            qnt_zeros = ""
        
        print("")
        print('SUA SENHA -> '+qnt_zeros + str(SenhaPreferencial + 1 ))
        print("")
        yesorno = input("DESEJA CRIAR A SENHA ? (s/n) ")
        if yesorno == "s":
            SenhaPreferencial += 1
            cliente.tipo = 2
            cliente.senha = SenhaPreferencial
            print("\nSENHA GERADA !\n") 
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
            fila_Preferencial.enfileira(cliente)
        elif yesorno == "n" :
            print("\nCRIAÇÕA DE SENHA CANCELADA!\n")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
        else : 
            print("")
            print(f'{"ERRO DE RESPOSTA ERRADA !":^50}')
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")
            #os.system('clear')
    else : 
        print("")
        print(f'{"ERRO DE RESPOSTA ERRADA !":^50}')
        print("")
        continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
        os.system("cls")
        #os.system('clear')
        
def ChamarCliente():
    '''
    Chama um *cliente* da devida fila, conforme a ordem, e dirije o mesmo ao caixa indicado.
    '''

    global ordem
    global SenhaPreferencial
    global SenhaComum
    global Qnt_caixas
    

    print('\nQUAL CAIXA ESTÁ CHAMANDO ? (1 até ' + str(Qnt_caixas) +')')
    caixa_livre = int(input('CAIXA '))
    if caixa_livre < 1 or caixa_livre > Qnt_caixas : 
        print("")
        print(f'{"ERRO ! CAIXA NÃO EXISTENTE":^50}')
        print("")
        continuar_operando = input("Tecle ENTER para volata ao Menu Principal")
        os.system("cls")
        #os.system("clear")

    elif fila_Comum.vazia() and fila_Preferencial.vazia():
        print("")
        print(f'{"NÃO EXISTEM CLIENTES EM ESPERA !":^50}')
        print("")
        continuar_operando = input("Tecle ENTER para volata ao Menu Principal")
        os.system("cls")
        #os.system("clear")
    else:   
        if ordem == 2 or fila_Preferencial.vazia():
            cliente_chamado = fila_Comum.desenfileira()
            ordem = 0
        elif ordem < 2:
            cliente_chamado = fila_Preferencial.desenfileira()

        caixa_livre = caixas.buscaPos(caixa_livre-1)
        caixa_livre.situação = cliente_chamado
        ordem +=1 
        print("")
        if  cliente_chamado.tipo == 1:
            qnt_zeros = "" 
            if SenhaComum < 10 :
                qnt_zeros = "00"
            elif SenhaComum > 10 : 
                qnt_zeros = "0" 
            elif SenhaComum > 99 :
                qnt_zeros = ""
            print('Senha[COMUM]: '+qnt_zeros + str(cliente_chamado.senha) +'\n\nDIRIJA-SE AO CAIXA:' + str(caixa_livre.número))
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao menu principal")
            os.system("cls")
            #os.system("clear")
        else:
            qnt_zeros = "" 
            if SenhaPreferencial < 10 :
                qnt_zeros = "00"
            elif SenhaPreferencial > 10 : 
                qnt_zeros = "0" 
            elif SenhaPreferencial > 99 :
                qnt_zeros = ""
            print('Senha[PREFERENCIAL]: '+qnt_zeros + str(cliente_chamado.senha) +'\n\nDIRIJA-SE AO CAIXA:' + str(caixa_livre.número))
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao menu principal")
            os.system("cls")
            #os.system("clear")
        

def Consultar_Clientes():
    '''
    Mostra as filas comum e preferêncial
    '''
    print('='*50 + '\n')
    print(f'{"FILA COMUM":^50}')
    print("")
    fila_Comum.exibe()
    print("")
    print("="*50 + "\n")
    print(f'{"FILA PREFERENCIAL":^50}' + "\n")
    fila_Preferencial.exibe()
    print("")
    print('='*50 + "\n")
    continuar_operando = input("Tecle ENTER para voltar ao menu principal")
    os.system("cls")
    #os.system("clear")
    

def Consultar_Caixas():
    '''
    Mostra os caixas, se estiver atendendo um cliente ele mostra a senha sendo atendida, senão, mostra que está livre.
    '''
    print("")
    caixas.exibe()
    print("")
    continuar_operando = input("Tecle ENTER para voltar ao menu principal")
    os.system("cls")
    #os.system("clear")
    
if __name__ == '__main__':

    #Variaveís auxiliares
    global SenhaComum
    global SenhaPreferencial
    global ordem
    SenhaComum = 0
    SenhaPreferencial = 0
    ordem = 0
    fila_Comum = FilaDinamica()
    fila_Preferencial = FilaDinamica()
    caixas = ListaLigada()

    main()    

