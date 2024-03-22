# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:04:26 2021

@author: fdepo
"""

class Page(object):     # Classe que define as páginas da árvore
	def __init__(self,folha):
		
		self.chaves = []
		self.folha = folha
		if folha:
			self.anterior = None
			self.proximo = None
		else:
			self.filhos = []

class Bplus(object):  # Classe com os atributos da árvore e os métodos
	def __init__(self, tamanho_pagina, tamanho_folha):
		self.raiz = Page(True)
		#self.raiz.chaves.append(valor)
		self.tamanho = tamanho_pagina
		self.tamanhoFolha = tamanho_folha

	# Método inserção inicial que recebe a raiz.
	def insereRaiz(self,raiz,valor):

		#faz a inserção do no
		pagReturn, chave = self.insere(raiz,valor)
		#verifica se é necessario uma nova raiz
		if pagReturn or chave:
			pageNewRaiz = Page(False) # false diz que não é folha e sim raiz
			pageNewRaiz.chaves.append(chave)
			pageNewRaiz.filhos.append(raiz)
			pageNewRaiz.filhos.append(pagReturn)
			self.raiz = pageNewRaiz #cria nova raiz

	#intermediario para inserir na folha ou raiz
	def insere(self,pag,valor):
		if pag.folha: #se a pagina estiver marcada como folha insira a folha
			pagReturn, chave = self.insereFolha(pag,valor)
		else: #se não for folha
			flag = False
			for i in pag.chaves:
				if i > valor:
					pagReturn, chave = self.insere(pag.filhos[pag.chaves.index(i)], valor)
			if not flag:
				pagReturn, chave = self.insere(pag.filhos[len(pag.filhos)-1],valor)
			
			if pagReturn or chave: #houve divisão
				if len(pag.chaves) < int(self.tamanho): #testa se a chave tem espaço
					#insere a chave e retorna None,None
					pag.chaves.append(chave)
					pag.chaves.sort() #organiza
					pag.filhos.insert(pag.chaves.index(chave)+1,pagReturn)
					return None,None
				else: #se não houver espaço 
					pagNew = Page(False) #cria uma nova pagina não folha
					pag.chaves.append(chave)
					pag.chaves.sort()
					pag.filhos.insert(pag.chaves.index(chave)+1,pagReturn)
					pagNew.chaves = pag.chaves[int((self.tamanho)):]
					pag.chaves = pag.chaves[:int((self.tamanho))]
					pagNew.filhos = pag.filhos[int((self.tamanho)):]
					pag.filhos = pag.filhos[:int((self.tamanho))]
					aux = pagNew.chaves[0]
					pagNew.chaves.pop(0)
					return pagNew,aux
		return pagReturn, chave

	#insere nas folhas, podendo dividir e conectar irmãos
	def insereFolha(self,pag,valor):
		if len(pag.chaves) < int(self.tamanhoFolha):
			pag.chaves.append(valor)
			pag.chaves.sort()
			return None,None
		else:
			pagNew = Page(True)
			pag.chaves.append(valor)
			pag.chaves.sort()
			pagNew.chaves = pag.chaves[int((self.tamanhoFolha)):]
			pag.chaves = pag.chaves[:int((self.tamanhoFolha))]
			pagNew.proximo = pag.proximo
			if(pag.proximo):
				pag.proximo.anterior = pagNew
			pag.proximo = pagNew
			pagNew.anterior = pag
			return pagNew,pagNew.chaves[0]


	# Método que mostra a árvore inteira começando da raiz
	def mostrarArvore(self,pag):
		if not pag.folha:
			print(pag.chaves," Não folha")
			for i in range(len(pag.filhos)):
				self.mostrarArvore(pag.filhos[i])
		else:
			print(pag.chaves)
    