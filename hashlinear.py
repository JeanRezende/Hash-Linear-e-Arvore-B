#classe para ser usada como objeto do vetor bucket
class Page:
    def __init__(self):
        self.valores = [] #valores em cada pagina
        self.overflow = None #overflow

class LinearHash:
    def __init__(self, tamanho_buckets, tamanho_pagina):
        self.h0 = tamanho_buckets #define o tamanho inicial do hash
        self.page_size = tamanho_pagina # define o tamanho de cada pagina
        self.proximo = 0 #inicia o valor do proximo
        self.buckets = []  #inicia o vetor de buckets
        i=0
        while i < self.h0: #insere paginas vazias como valores iniciais do bucket
            self.buckets.append(Page())
            i += 1

    #metodo pra calcular o hash de um valor
    def hash(self, key):
        #faz o calculo se o hash for menor ou igual ao proximo e menor que o hash atual
        if self.proximo <= key % self.h0 < self.h0: #calcula h0
            return key % self.h0
        else: #calcula h1
            return key % (self.h0 * 2)

    #metodo para lidar com colisões de overflow
    def overflow(self, key, page):
        if page.overflow: #se ja houver uma pagina de overflow
            #insere na pagina de overflow
            page.overflow.valores.append(key)
        else: #se ainda não ter uma pagina de overflow:
            page.overflow = Page()
            page.overflow.valores.append(key)

    #metodo para dividir o bucket com o marcador proximo, ativado quando houver overflow
    def split(self):
        #cria um novo bucket
        self.buckets.append(Page())
            
        #copia todo o vetor onde o proximo esta
        aux = self.buckets[self.proximo].valores[:] 
        aux_overflow = self.buckets[self.proximo].overflow 

        #esvazia o bucket que foi copiado pro aux
        self.buckets[self.proximo].valores = []
        self.buckets[self.proximo].overflow = None

        #recalcula o proximo
        if self.proximo < self.h0:
            self.proximo = self.proximo + 1
        else:
            self.proximo = 0 #faz o proximo voltar ao valor inicial
            self.h0 = self.h0 * 2 #dobra o tamanho do hash
            
        #reinsere os dados que foram tirados desse split
        for keys in aux:
            self.insert(keys)
        #reinsere os dados retirados do overflow
        if aux_overflow != None: 
            for keys in aux_overflow.valores:
                self.insert(keys)

    def insert(self, key):
        chavehash = self.hash(key) #pega o calculo do hash
		
        #se o tamanho for menor que o maximo insere no espaço vazio do bucket
        if len(self.buckets[chavehash].valores) < self.page_size: 
            self.buckets[chavehash].valores.append(key)
        #se passar do tamanho chama função de overflow
        else:
            self.overflow(key, self.buckets[chavehash]) #chama o gerencidor de overflow
            self.split() #faz a divisão do bucket na posição proximo

    
    def remove(self, key):
        chavehash = self.hash(key) #pega o calculo do hash
        # se encontrar o valor no hash remove
        if key in self.buckets[chavehash].valores: 
            self.buckets[chavehash].valores.remove(key)
        # caso não procura tambem na pagina de overflow
        elif self.buckets[chavehash].overflow != None:
            #se achar a chave no overflow remove
            if key in self.buckets[chavehash].overflow.valores:
                self.buckets[chavehash].overflow.valores.remove(key)
            #se removeu e zerou o overflow ele volta pra None
            if len(self.buckets[chavehash].overflow.valores) == 0:
                self.buckets[chavehash].overflow = None

    def search(self, key):
        chavehash = self.hash(key) #pega o calculo do hash

        if key in self.buckets[chavehash].valores: # procura o valor nas paginas normais
            print("chave " + str(key) + " encontrada no bucket " + str(self.buckets[chavehash].valores))
        elif self.buckets[chavehash].overflow: # testa se tem overflow no bucket
            if key in self.buckets[chavehash].overflow.valores: # retira o valor se encontrar
                print("chave " + str(key) + " encontrada na pag de overflow")
        else:
            print("chave não encontrada")
			
	# Método que mostra todas as chaves da hash
    def mostrar(self):
        for page in self.buckets:
            
            if page.overflow != None:
                print(str(page.valores) + " " + str(page.overflow.valores) )
            else:
                print(str(page.valores) + " " + str(page.overflow))