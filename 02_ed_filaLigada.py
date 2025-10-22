from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Cliente():

    senha:int
    tipo:int


@dataclass
class No:
    elemento: Cliente | None
    proximo: No | None = None 


class FilaDinamica():
    ''' Representa uma fila dinamica com sentinela '''

    def __init__(self) -> None:
        ''' Inicializa a fila '''
        self.inicio = No(None)
        self.fim = self.inicio

    def vazia(self) -> bool:
        ''' verifica se a fila está vazia '''
        return self.inicio.proximo == None
       
    def enfileira(self, elem) -> None:
        ''' Insere um elemento na fila '''
        novo = No(elem)
        self.fim.proximo = novo
        self.fim = novo
        
    def desenfileira(self) -> Cliente:
        ''' Remove um elemento da fila '''
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.inicio.proximo
        self.inicio.proximo = removido.proximo
        removido.proximo = None
        if self.vazia():
            self.fim = self.inicio
        return removido.elemento
    
    def primeiroElemento(self) -> No:
        ''' Retorna o primeiro elemento da fila '''
        if self.vazia():
            raise ValueError('Fila Vazia')
        return deepcopy(self.inicio.proximo)
        
    def exibe(self) -> None:

        if self.vazia():
            print(f'{"[ NÃO HÁ CLIENTES NA FILA ]":^50}')
            print("")
        else:
            p = self.inicio.proximo
            print('[' + "00" + str(p.elemento.senha), end="")

            while p.proximo!=None:
                p = p.proximo
                print(',',p.elemento.senha,end ='')

            print(']')
            
    def esvazia(self) -> None:
        self.inicio.proximo = None
        self.fim = self.inicio

    def tamanho(self) -> int:

        p = self.inicio.proximo
        i=0

        while p != None:

            p=p.proximo
            i+=1

        return i 
