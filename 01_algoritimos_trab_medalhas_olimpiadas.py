from dataclasses import dataclass
from enum import Enum, auto
import sys
sys.setrecursionlimit(2000)


class Medalha(Enum) : 
    BRONZE = '3'
    PRATA = '2' 
    OURO  = '1'

@dataclass
class Evento(): 
    Pais_Vencedor : str 
    Medal : Medalha 
    Genero : str

@dataclass  
class Medalhas_por_Pais () : 
    Pais : str
    Bronze : int
    Prata : int 
    Ouro : int

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])
    
    #DEIXAR A TABELA MENOR PARA TRABALHAR COM MENOS ITENS, A FIM APENAS DE OTIMIZAR, A TABELA COMPLETA NÃO COMPUTA A RECURSIVIDADE
    #tabela = tabela[0:10]

    #ATRIBUINDO VARIÁVEIS E PRINT`S PARA TESTAR AS FUNÇÕES

    tabelafiltrada = filtra(tabela)
    lista_de_eventos = transforma(tabelafiltrada)
    medalhas = soma_medalhas(lista_de_eventos)
    paises_ordenados = ordena(medalhas)
    tabela_formatada = exibir_tabela(paises_ordenados)

    #print(tabela)
    #print(tabelafiltrada)
    #print(lista_de_eventos)
    #print(medalhas)
    #print(paises_ordenados)
    print(tabela_formatada)

    #VARIÁVEIS E PRINT`S DAS FUNÇÕES RECURSIVAS PARA IDENTIFICAR PÁISES QUE VECERAM EM APENAS UM GÊNERO 

    paises_com_medalhas = transforma(tabelafiltrada)
    resultado_m = filtra_paises_masculinos(paises_com_medalhas, [])
    resultado_w = filtra_paises_femininos(paises_com_medalhas, [])

    print("\nPaíses com medalhas apenas masculinas:")
    for pais in resultado_m:
        print(f"País: {pais}")

    print("\nPaíses com medalhas apenas femininas:")
    for pais in resultado_w:
        print(f"País: {pais}")
    
    # TODO: computar e exibir o quadro de medalhas
    # TODO: computar e exibir os países que tiverem apenas
    #       atletas de um único gênero premiados


def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.

    Por exemplo, se o conteúdo do arquivo for

    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995

    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)


def filtra(tabela : list[list[str]])-> list[list[str]]: 
    '''
    Filtra a primeira tabela dos eventos do arquivo.csv, para ficar apenas com o necessário para resolução dos exercícios,
    no caso, o país, o tipo da medalha, e o gênero do ganhador
    >>> filtra([['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'BEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136\n']])
    [('1', 'BEL', 'M')]
    >>> filtra([['Silver Medal', '2', '2024-07-27', 'Filippo GANNA', 'ITA', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1923520\n']])
    [('2', 'ITA', 'M')]
    >>> filtra([['Bronze Medal', '3', '2024-07-27', 'Wout van AERT', 'BEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903147\n']])
    [('3', 'BEL', 'M')]
    '''
    tabela_filtrada = []
    for item in tabela :
        tabela_nova = (item[1], item[4], item[5])
        tabela_filtrada.append(tabela_nova)
    return tabela_filtrada 



def transforma(tabelafiltrada : list[list[str]]) -> list[Evento] : 
    '''
    Transforma a tabela filtrada, que está como uma lista de listas de stings, em uma lista de tipo composto de eventos, com o pais, medalha e gênero 
    >>> transforma([('1', 'BEL', 'M')])
    [Evento(Pais_Vencedor='BEL', Medal=<Medalha.OURO: '1'>, Genero='M')]
    >>> transforma([('2', 'ITA', 'M'), ('3', 'BEL', 'M'), ('1', 'AUS', 'W'), ('2', 'GBR', 'W')])
    [Evento(Pais_Vencedor='ITA', Medal=<Medalha.PRATA: '2'>, Genero='M'), Evento(Pais_Vencedor='BEL', Medal=<Medalha.BRONZE: '3'>, Genero='M'), Evento(Pais_Vencedor='AUS', Medal=<Medalha.OURO: '1'>, Genero='W'), Evento(Pais_Vencedor='GBR', Medal=<Medalha.PRATA: '2'>, Genero='W')]
    >>> transforma([('1', 'KOR', 'M')])
    [Evento(Pais_Vencedor='KOR', Medal=<Medalha.OURO: '1'>, Genero='M')] 
    '''
    tabela_enumeravel = []
    for item in tabelafiltrada : 
        evento = Evento(item[1], Medalha(item[0]), item[2])
        tabela_enumeravel.append(evento)
    return tabela_enumeravel


def soma_medalhas(tabela_enumeravel : list[Evento]) -> list[Medalhas_por_Pais]:
    '''
    Transforma a tabela de eventos em uma lista de medalhas por país, primeiro adicionando cada país, verifica se o páis já está na lista, se sim, quebra o laço, se não, 
    adicona apenas uma vez, com 0 medalhas em uma nova lista de uma classe diferente, posteriormente, soma a cada país suas medalhas de ouro, prata e bronze.
    >>> soma_medalhas([Evento(Pais_Vencedor='BEL', Medal=<Medalha.OURO: '1'>, Genero='M'), Evento(Pais_Vencedor='BEL', Medal=<Medalha.BRONZE: '3'>, Genero='M')])
    [Medalhas_por_Pais(Pais='BEL', Bronze=1, Prata=0, Ouro=1)]
    >>> soma_medalhas([Evento(Pais_Vencedor='USA', Medal=<Medalha.BRONZE: '3'>, Genero='W'), Evento(Pais_Vencedor='CHN', Medal=<Medalha.OURO: '1'>, Genero='W'), Evento(Pais_Vencedor='USA', Medal=<Medalha.PRATA: '2'>, Genero='W')])
    [Medalhas_por_Pais(Pais='CHN', Bronze=0, Prata=0, Ouro=1), Medalhas_por_Pais(Pais='USA', Bronze=1, Prata=1, Ouro=0)]
    >>> soma_medalhas([Evento(Pais_Vencedor='GBR', Medal=<Medalha.BRONZE: '3'>, Genero='W')])
    [Medalhas_por_Pais(Pais='GBR', Bronze=1, Prata=0, Ouro=0)]
    '''
    
    lista_pais = []
    for item in tabela_enumeravel:    
        pais_existe = False
        for pais in lista_pais:
            if pais.Pais == item.Pais_Vencedor:
                pais_existe = True
                break
        
        if not pais_existe:
            elemento = Medalhas_por_Pais(item.Pais_Vencedor, 0, 0, 0)
            lista_pais.append(elemento)

    for evento in tabela_enumeravel:
        for pais in lista_pais:
            if pais.Pais == evento.Pais_Vencedor:
                if evento.Medal == Medalha.OURO:
                    pais.Ouro += 1
                elif evento.Medal == Medalha.PRATA:
                    pais.Prata += 1 
                elif evento.Medal == Medalha.BRONZE: 
                    pais.Bronze += 1

    return lista_pais
def ordena(medalhas_pais: list[Medalhas_por_Pais]) -> list[Medalhas_por_Pais]:
    '''
    Primeiro, compara o número de medalhas de ouro.
    Se os números de ouro são iguais, compara o número de medalhas de prata.
    Se também os números de prata são iguais, compara o número de medalhas de bronze.
    As trocas são realizadas se qualquer uma das comparações indicar que o elemento atual deve vir depois do próximo elemento.
    >>> ordena([Medalhas_por_Pais(Pais='CHN', Bronze=24, Prata=27, Ouro=39), Medalhas_por_Pais(Pais='USA', Bronze=0, Prata=0, Ouro=40)])
    [Medalhas_por_Pais(Pais='USA', Bronze=0, Prata=0, Ouro=40), Medalhas_por_Pais(Pais='CHN', Bronze=24, Prata=27, Ouro=39)]
    >>> ordena([Medalhas_por_Pais(Pais='BRA', Bronze=100, Prata=100, Ouro=0), Medalhas_por_Pais(Pais='ITA', Bronze=0, Prata=0, Ouro=1)])
    [Medalhas_por_Pais(Pais='ITA', Bronze=0, Prata=0, Ouro=1), Medalhas_por_Pais(Pais='BRA', Bronze=100, Prata=100, Ouro=0)]
    >>> ordena([Medalhas_por_Pais(Pais='ITA', Bronze=0, Prata=0, Ouro=1), Medalhas_por_Pais(Pais='BRA', Bronze=100, Prata=100, Ouro=0), Medalhas_por_Pais(Pais='CHN', Bronze=101, Prata=100, Ouro=0), Medalhas_por_Pais(Pais='USA', Bronze=1, Prata=0, Ouro=1)])
    [Medalhas_por_Pais(Pais='USA', Bronze=1, Prata=0, Ouro=1), Medalhas_por_Pais(Pais='ITA', Bronze=0, Prata=0, Ouro=1), Medalhas_por_Pais(Pais='CHN', Bronze=101, Prata=100, Ouro=0), Medalhas_por_Pais(Pais='BRA', Bronze=100, Prata=100, Ouro=0)]
    '''
    n = len(medalhas_pais)
    for i in range(n):
        for j in range(0, n-i-1):
            if (medalhas_pais[j].Ouro < medalhas_pais[j+1].Ouro or
                (medalhas_pais[j].Ouro == medalhas_pais[j+1].Ouro and medalhas_pais[j].Prata < medalhas_pais[j+1].Prata) or
                (medalhas_pais[j].Ouro == medalhas_pais[j+1].Ouro and medalhas_pais[j].Prata == medalhas_pais[j+1].Prata and medalhas_pais[j].Bronze < medalhas_pais[j+1].Bronze)):
               
                aux = medalhas_pais[j]
                medalhas_pais[j] = medalhas_pais[j+1]
                medalhas_pais[j+1] = aux
                
    return medalhas_pais
                 
def exibir_tabela(paises : list[Medalhas_por_Pais]) -> str : 
    '''
    Exibe a tabela de classificação de cada país em uma string formatada 
    '''
    print(f'{"PAÍS":<15} {"OURO":<10} {"PRATA":<10} {"BRONZE":<10} {"TOTAL":<10}')    
    
    for item in paises:
        soma = item.Ouro + item.Prata + item.Bronze 
        print(f'{item.Pais:<15} {item.Ouro:<10} {item.Prata:<10} {item.Bronze:<10} {soma:<10}')

#FUNÇÕES RECURSIVAS PARA DESCOBRIR PAÍSES QUE GANHARAM COM APENAS UM GÊNERO

def filtra_paises_masculinos(paises_com_medalhas: list[Evento], paises_masculinos: list[str]) -> list[str]:

    '''
    Identificar os países que ganharam medalhas exclusivamente em eventos masculinos usando recurssão
    A função verifica se a lista paises_com_medalhas, uma lista de eventos,  está vazia. Se estiver, significa que todos os
    eventos foram processados, e a função retorna a lista paises_masculinos, uma lista de str com todos os países, atualizada.
    O primeiro evento da lista de eventos é extraído e armazenado em evento_atual.
    O restante dos eventos é armazenado em restante_eventos.
    Se o gênero do evento_atual for 'M' e o país vencedor não estiver na lista paises_masculinos,
    o país é adicionado à lista paises_masculinos.
    Se o gênero do evento_atual for 'W'  e o país vencedor  estiver na lista paises_masculinos,
    o país é removido da lista paises_masculinos. Porque a presença do país em um evento feminino indica que ele não deve estar na
    lista de países que ganharam apenas em eventos masculinos.
    A função se chama recursivamente passando o restante_eventos, quebrando em um problema menor, e a lista atualizada paises_masculinos como parâmetros.
    Isso permite que o processamento continue para os eventos restantes.
    >>> filtra_paises_masculinos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='M'),Evento(Pais_Vencedor='ARG', Medal=Medalha.PRATA, Genero='W'),Evento(Pais_Vencedor='FRA', Medal=Medalha.BRONZE, Genero='M'),Evento(Pais_Vencedor='BRA', Medal=Medalha.PRATA, Genero='W')], []])
    ['FRA']
    >>> filtra_paises_masculinos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='M'), [])
    ['BRA']
    >>> filtra_paises_masculinos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='W'), [])
    []
    '''
    if not paises_com_medalhas:
        return paises_masculinos
    
    evento_atual = paises_com_medalhas[0]
    restante_eventos = paises_com_medalhas[1:]

    if evento_atual.Genero == 'M' and evento_atual.Pais_Vencedor not in paises_masculinos:
        paises_masculinos.append(evento_atual.Pais_Vencedor)
 
    if evento_atual.Genero == 'W' and evento_atual.Pais_Vencedor in paises_masculinos:
        paises_masculinos.remove(evento_atual.Pais_Vencedor)

    return filtra_paises_masculinos(restante_eventos, paises_masculinos)

def filtra_paises_femininos(paises_com_medalhas: list[Evento], paises_femininos: list[str]) -> list[str]:
    '''
    Quase identica a função anterior, unica diferença é que esta processa verificando a presença de países com medalhas apenas femininas  
    >>> filtra_paises_femininos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='M'),Evento(Pais_Vencedor='ARG', Medal=Medalha.PRATA, Genero='W'),Evento(Pais_Vencedor='FRA', Medal=Medalha.BRONZE, Genero='M'),Evento(Pais_Vencedor='BRA', Medal=Medalha.PRATA, Genero='W')], []])
    ['ARG']
    >>> filtra_paises_femininos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='M'), [])
    []
    >>> filtra_paises_femininos([Evento(Pais_Vencedor='BRA', Medal=Medalha.OURO, Genero='W'), [])
    [BRA]
    '''
    if not paises_com_medalhas:
        return paises_femininos
 
    evento_atual = paises_com_medalhas[0]
    restante_eventos = paises_com_medalhas[1:]

    if evento_atual.Genero == 'W' and evento_atual.Pais_Vencedor not in paises_femininos:
        paises_femininos.append(evento_atual.Pais_Vencedor)

    if evento_atual.Genero == 'M' and evento_atual.Pais_Vencedor in paises_femininos:
        paises_femininos.remove(evento_atual.Pais_Vencedor)

    return filtra_paises_femininos(restante_eventos, paises_femininos)


if __name__ == '__main__':
    main()
