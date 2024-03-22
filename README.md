# Hash Linear e Arvore B+

Algoritmo implementado para disciplina de banco de dados 2, reproduzindo 2 algoritmos muito utilizados em banco de dados atuais, e utilizando um gerador de dados automaticos para teste destes algoritmos


# instruções para executar as funções

O arquivo main engloba e importa todas as funções
basta colocar os comandos dentro da função main

* gerando os dados
usando a função 'criar_dados(atributos, insercao, remocao)'
é feito a criação de um arquivo 'dados.csv'
que serve de base para inserir e remover dados do hash

* hash linear
usando a função 'run_hash(numero_de_buckets, tamanho_paginas)'
de acordo com os dados criados, eles são lidos e inseridos e removidos
essa função retorna um o tempo de execução dessa operação em float
essa função tambem grava um arquivo 'resultado_hash.csv' que representa
o estado do hash apos as operações

* arvore b+
usando a função 'run_tree(tamanho_paginas, tamanho_folha)'
de acordo com os dados criados, eles são lidos e inseridos e removidos
essa função retorna um o tempo de execução dessa operação em float
e faz o print da arvore no console
resultado pode levar um tempo para banco com mais de 1000 inserções


