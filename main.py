from hashlinear import LinearHash
from arvore_B import Bplus
import siogen
import csv
import time
import matplotlib.pyplot as plt

def run_hash(tamanho_buckets, tamanho_paginas):
    inicio = time.time()
    #instanciando a função de hash linear
    hl = LinearHash(tamanho_buckets, tamanho_paginas)
    #abrindo e lendo o arquivo gerado pelo siogen
    with open('dados.csv') as dados:
        reader = csv.reader(dados)
        for linha in reader:
            if len(linha) > 0: #ignora linhas vazias
                if linha[0] =='+': #le os dados a inserir
                    hl.insert(int(linha[1]))
                if linha[0] == '-': #le os dados a remover
                    hl.remove(int(linha[1]))

    final = time.time() #contabiliza o tempo de inserção e remoção

    #grava o arquivo resultados que mostra a saida completa do hash linear
    with open('resultado_hash.csv', 'w') as dados:
        writer = csv.DictWriter(dados, delimiter = ',', fieldnames=['Buckets', 'Overflow'],  lineterminator = '\n',)
        for page in hl.buckets:
            if page.overflow != None:
                writer.writerow({'Buckets' : str(page.valores) ,'Overflow' : str(page.overflow.valores) })
            else:
                writer.writerow({'Buckets' : str(page.valores) ,'Overflow' : str(page.overflow)})     
    while input("Deseja fazer alguma busca no hash? S/N : ").lower() == 's' :
        hl.search(int(input("Digite a chave desejada: ")))
    return final - inicio #

def run_tree(tamanho_paginas, tamanho_folha):
    inicio = time.time()
    #instanciando a função de hash linear
    Btree = Bplus(tamanho_paginas, tamanho_folha)
    #abrindo e lendo o arquivo gerado pelo siogen
    with open('dados.csv') as dados:
        reader = csv.reader(dados)
        for linha in reader:
            if len(linha) > 0: #ignora linhas vazias
                if linha[0] =='+': #le os dados a inserir
                    Btree.insereRaiz(Btree.raiz, int(linha[1]))
                #if linha[0] == '-': #le os dados a remover
                #    Btree.remover(Btree.raiz, int(linha[1]))
    Btree.mostrarArvore(Btree.raiz)
    final = time.time() #contabiliza o tempo de inserção e remoção
    return final - inicio #

def criar_dados(atributos, insercao, remocao):
    pardict = { 'att' : atributos, 'ins' : insercao, 'del' : remocao, 'file' : 'dados.csv'}
    siogen.gen_data(pardict)

def main():
    #gera os dados no SIOgem no formato atr, ins, remo (a arquivo tem nome de dados.csv)
    criar_dados(5, 500, 250)
    #roda o hash passando (tamanho_buckets, tamanho_paginas)
    run_hash(10,10)
    #roda a arvore passando (tamanho_paginas, tamanho_folha)
    run_tree(4, 20)
    
if __name__ == '__main__':
    main()