from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Cliente():

    senha:int
    tipo:int

@dataclass
class Caixa():

    número:int
    situação: Cliente | None

@dataclass
class No:
    elemento: Caixa
    proximo: No | None = None 


class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    

    def vazia(self):
        return self.inicio == None
    
    
    def tamanho(self) -> int:
        p = self.inicio
        tam = 0
        while p != None:
            tam += 1
            p = p.proximo
        return tam
    

    def primeiro(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.inicio
    

    def ultimo(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.fim
    
    
    def exibe(self) -> None:
        #print('Lista: inicio --> [', end='')
        print("• ", end="")
        p = self.inicio
        while p != None:
            if p.elemento.situação == None:
                print('Caixa:', p.elemento.número,'[CAIXA LIVRE]')
            else:
                if p.elemento.situação.tipo == 1 : 
                    tipo = "COMUM"
                else : 
                    tipo = "PREFERENCIAL"
                print('Caixa: ' + str(p.elemento.número) +' [SENHA: 00'+ str(p.elemento.situação.senha) +'] -> '+ tipo)
            p = p.proximo
            if p != None: 
                print('• ', end='')
        #print('] <-- fim')
    
    
    def busca(self, elem) -> No | None:
        p = self.inicio
        while p != None and p.elemento.número != elem.número:
            p = p.proximo
        return p


    def buscaPos(self, pos: int) -> No:
        if pos < 0 or pos >= self.tamanho():
            raise ValueError('Posição inválida')
        i = 0
        p = self.inicio
        while p != None and i < pos:
            i += 1
            p = p.proximo
        return p.elemento
    

    def insereFim(self, elem) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
    

    def insereInicio(self, elem) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            self.fim = novo
        novo.proximo = self.inicio
        self.inicio = novo
    

    def inserePos(self, elem, pos: int) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        tam = self.tamanho()
        if pos < 0 or pos > tam:
            raise ValueError('Posição inválida')
        # inserção no início da lista
        if pos == 0:
            self.insereInicio(elem)
        # inserção no fim da lista
        elif pos == tam:
            self.insereFim(elem)
        # inserção no meio da lista
        else:
            i = 1
            p = self.inicio.proximo
            while p != None and i < pos-1:
                p = p.proximo
                i += 1
            novo = No(elem)
            novo.proximo = p.proximo
            p.proximo = novo       


    def removeInicio(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.vazia():
            self.fim = None
        removido.proximo = None


    def removeFim(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        if self.tamanho() == 1:
            self.inicio = None
            self.fim = None
        else:
            p = self.inicio
            anterior = None        
            while p != self.fim:
                anterior = p
                p = p.proximo
            anterior.proximo = None
            self.fim = anterior
        

    def removePos(self, pos: int) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        tam = self.tamanho()
        if pos < 0 or pos >= tam:
            raise ValueError('Posição inválida')
        # remoção no início da lista
        if pos == 0:
            self.removeInicio()
        # remoção no fim da lista
        elif pos == tam - 1:
            self.removeFim()
        # remoção no meio da lista
        else:
            i = 1
            anterior = self.inicio
            p = self.inicio.proximo
            while p != None and i < pos:
                anterior = p
                p = p.proximo
                i += 1
            anterior.proximo = p.proximo
            p.proximo = None


    def removeElemento(self, elem) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.busca(elem)
        if removido == self.inicio:
            self.removeInicio()
        elif removido == self.fim:
            self.removeFim()
        else:
            anterior = self.inicio
            p = self.inicio.proximo
            while p != removido:
                anterior = p
                p = p.proximo
            anterior.proximo = p.proximo
            p.proximo = None


    def esvazia(self) -> None:
        self.inicio = None
        self.fim = None
