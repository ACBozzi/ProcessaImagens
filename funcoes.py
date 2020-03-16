#Trabalho de Amostragem e quantização referente a disciplina de Processamento de IMAGENS#
#																						#
#Aluna: Anna Caroline Bozzi																#
#GRR: 20173532																			#	
#########################################################################################

#####################################################################################################
#ENUNCIADO:																							#
#Implemente um programa que realize amostragem de quantização em uma imagem monocromática. O 		#
#programa deve receber como parâmetros o nome da imagem, o porcentual de amostragem, a técnica de 	#
#amostragem (média, mediana ou moda.) e a quantidade de níveis de cinza [2,4,8,16,32,64,128,256] 	#
#(quantização). A saída do programa deve ser a imagem amostrada. Utilize a imagem exemplo.png para 	#
#testar o programa.																					#
#####################################################################################################



import numpy as np
import cv2
import sys
from matplotlib import pylab
from pylab import *
import os
from numpy import *
import random
import statistics
from PIL import Image
from pylab import *
import matplotlib.cm as cm


#-------------------FUNÇÃO PARA VERIFICAÇÃO DE ERROS PASSADOS EM PARÂMETRO------------------------------------------------------------

def verificaErroParametros():
    argumentos = len(sys.argv)
    if(argumentos == 1):
        print("Entre com o nome da imagem")
        print("Exmeplo: python3 trab1.py [nome][percentual][nivel de cinza][tecnica]")
        exit()
    elif(argumentos==2):
        print("Entre com o percentual desejado em %")
        exit()
    elif(argumentos==3):
        print("Entre com a tecnica desejada: ")
        print("1 - Media")
        print("2 - Mediana")
        print("3 - Moda")
    elif(argumentos==4):
        print("Entre com os niveis de cinza desejados")
        exit()


#------------------FUNÇÃO PARA DEFINIR O TAMANHO DA JANELA PARA AMOSTRAGEM------------------------------------

def tamanho_janela(percentual_amostragem,dimensions):	
	nova_altura = dimensions[0] - (dimensions[0]*percentual_amostragem)
	nova_largura = dimensions[1] - (dimensions[1]*percentual_amostragem)
	janela1 = dimensions[0] / int(nova_altura)
	janela2 = dimensions[1] / int(nova_largura)

	return float(janela1), float(janela2), int(nova_altura), int(nova_largura)


#------------PARA CÁUCULOS QUAMNDO A JANELA É MULTIPLA DO TAMANHO-----------------------------------

def amostragem(img,tipo, dimensions,janela1,janela2,alturaNova,larguraNova):
	Inova = np.zeros((alturaNova,larguraNova), dtype = int)
	Lnova = 0
	Cnova = 0

	
	# se o parametro passado for um então a técnica é a MÉDIA
	if tipo == 1:
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova = 0
			for coluna in range(0,dimensions[1], janela2):	#coluna
				for x in range(linha, (linha+janela1)):
					for y in range(coluna, (coluna+janela2)):
						Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media 
				Inova[Lnova,Cnova] = (Inova[Lnova,Cnova] / (janela1*janela2))	#aqui faz a media
				Cnova+=1
			Lnova+=1

	# se o parâmetro for dois então é MEDIANA
	elif tipo ==2:
		lista = []
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova = 0
			for coluna in range(0,dimensions[1], janela2):	#coluna
				for x in range(linha, (linha+janela1)):
					for y in range(coluna, (coluna+janela2)):
						lista.append(img[x,y])
				lista_ordenada = sorted(lista) 
				if len(lista_ordenada) % 2 == 0:
					mediana = median(lista_ordenada)
					Inova[Lnova,Cnova] = mediana
					lista.clear()
				else:
					print("Janela não pe redonda")
				Cnova+=1
			Lnova+=1
		Inova = Inova.astype(np.uint8) 
		tamanho = Inova.shape
	
	#senão é a MODA
	else:
		lista = []
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova = 0
			for coluna in range(0,dimensions[1], janela2):	#coluna
				for x in range(linha, (linha+janela1)):
					for y in range(coluna, (coluna+janela2)):
						lista.append(img[x,y]) 
				try:
					moda = statistics.mode(lista)
					Inova[Lnova,Cnova] = moda
					lista.clear()
				except :
					#print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
					media = statistics.mean(lista)
					Inova[Lnova,Cnova] = media
					lista.clear()
				Cnova+=1
			Lnova+=1
		Inova = Inova.astype(np.uint8) 
		tamanho = Inova.shape

	return Inova

#-----------------CASO O VALOR DA JANELA NÃO SEJA EXATO FAZER INTERPOLAÇÃO--------------------------

def interpolacao(img,tipo, dimensions,janela1,janela2,alturaNova,larguraNova):
	Inova = np.zeros((alturaNova,larguraNova), dtype = int)
	Lnova = 0
	Cnova = 0

	try:
		float(janela1)
		janela1 =  round(janela1+0.5)
	except:
		janela1 = int(janela1)
	try:
		float(janela2)
		janela2 = round(janela2+0.5)
	except:
		janela2 = int(janela2)
	


	#MÉDIA 
	if tipo == 1:
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova=0
			if(linha+janela1 < dimensions[0]):
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media 
						Inova[Lnova,Cnova] = (Inova[Lnova,Cnova] / (janela1*janela2))	#aqui faz a media
						Cnova +=1
					else:
						#pular para a ultima jane
						coluna = dimensions[1] - janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media
						Inova[Lnova,Cnova] = (Inova[Lnova,Cnova] / (janela1*janela2))	#aqui faz a media 
						coluna = dimensions[1]+1
				Lnova+=1
			else:
				linha = dimensions[0] - janela1
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media 
						Inova[Lnova,Cnova] = (Inova[Lnova,Cnova] / (janela1*janela2))	#aqui faz a media
						Cnova +=1
					else:
						#pular para a ultima jane
						coluna = dimensions[1] - janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media
						Inova[Lnova,Cnova] = (Inova[Lnova,Cnova] / (janela1*janela2))	#aqui faz a media 
						coluna = dimensions[1]+1
				Lnova+=1
			linha = dimensions[0]+1
	
	#MODA 
	elif tipo ==2:
		lista = []
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova=0
			if(linha+janela1 < dimensions[0]):
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) #fazendo a soma dos elementos para a media 
						lista_ordenada = sorted(lista)
						if len(lista_ordenada) % 2 == 0:
							mediana = median(lista_ordenada)
							Inova[Lnova,Cnova] = mediana
							lista.clear()
						else:
							print("Janela não tem mediana")
						Cnova+=1
					else:
						#pular para a ultima jane
						coluna = dimensions[1] - janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) #fazendo a soma dos elementos para a media 
						lista_ordenada = sorted(lista)
						if len(lista_ordenada) % 2 == 0:
							mediana = median(lista_ordenada)
							Inova[Lnova,Cnova] = mediana
							lista.clear()
						else:
							print("Janela não tem mediana")
						Cnova+=1
						coluna = dimensions[1]+1
				Lnova+=1
			else:
				linha = dimensions[0] - janela1
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) #fazendo a soma dos elementos para a media
						lista_ordenada = sorted(lista)	#aqui faz a media 
						if len(lista_ordenada) % 2 == 0:
							mediana = median(lista_ordenada)
							Inova[Lnova,Cnova] = mediana
							lista.clear()
						else:
							print("Janela não pe redonda")
						Cnova +=1
					else:
						#pular para a ultima jane
						coluna = dimensions[1] - janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) #fazendo a soma dos elementos para a media
						lista_ordenada = sorted(lista)	#aqui faz a media 
						if len(lista_ordenada) % 2 == 0:
							mediana = median(lista_ordenada)
							Inova[Lnova,Cnova] = mediana
							lista.clear()
						else:
							print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
							media = statistics.mean(lista)
							Inova[Lnova,Cnova] = media
							lista.clear()
						Cnova+=1
						coluna = dimensions[1]+1
				Lnova+=1
			linha = dimensions[0]+1
		Inova = Inova.astype(np.uint8) 
		tamanho = Inova.shape
	
	#MODA
	else:
		lista = []
		for linha in range(0, dimensions[0],janela1):	#linha
			Cnova=0
			if(linha+janela1 < dimensions[0]):
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) 
						try:
							moda = statistics.mode(lista)
							Inova[Lnova,Cnova] = moda
							lista.clear()
						except :
							print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
							media = statistics.mean(lista)
							Inova[Lnova,Cnova] = media
							lista.clear()
						Cnova+=1
					else:
						coluna = dimensions[1]-janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) 
						try:
							moda = statistics.mode(lista)
							Inova[Lnova,Cnova] = moda
							lista.clear()
						except :
							print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
							media = statistics.mean(lista)
							Inova[Lnova,Cnova] = media
							lista.clear()
							Cnova+=1
						coluna = dimensions[1]+1
				Lnova+=1
			else:
				linha = dimensions[0] - janela1
				for coluna in range(0,dimensions[1], janela2):	#coluna
					if(coluna+janela2 < dimensions[1]):
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) 
						try:
							moda = statistics.mode(lista)
							Inova[Lnova,Cnova] = moda
							lista.clear()
						except :
							print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
							media = statistics.mean(lista)
							Inova[Lnova,Cnova] = media
							lista.clear()
						Cnova+=1
					else:
						#pular para a ultima jane
						coluna = dimensions[1] - janela2
						for x in range(linha, (linha+janela1)):
							for y in range(coluna, (coluna+janela2)):
								lista.append(img[x,y]) 
						try:
							moda = statistics.mode(lista)
							Inova[Lnova,Cnova] = moda
							lista.clear()
						except :
							print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
							media = statistics.mean(lista)
							Inova[Lnova,Cnova] = media
							lista.clear()
						Cnova+=1
						coluna = dimensions[1]+1
				Lnova+=1
			linha = dimensions[0]+1

	return Inova


#----------------QUANTIZAÇÃO PARA UMA IMAGEM COM APENAS DOIS NIVEIS DE CINZA-----------------------------

def quantizacao_binaria(img,altura,largura):

	for linha in range(0,altura):
		for coluna in range(0,largura):
			if img[linha,coluna] < 128:
				img[linha,coluna] = 0
			else:
				img[linha,coluna] = 255
		coluna = 0
	
	return img

#---------------------QUANTIZAÇÃO PARA IMAGENS COM MAIS DE DOIS NÍVEIS DE CINZA---------------------------

def quantizacao(img, altura,largura,niveis_cinza):

	Inova = np.zeros((altura,largura), dtype = int)

	nCores = niveis_cinza
	nCores = int(nCores)
	intervalo_quantizacao = (256 / (nCores))
	intervalo_quantizacao = int(intervalo_quantizacao)
	quantizada = np.zeros([largura, altura], dtype='uint8')
	
	#define os intervalos que utilizará
	lista_intervalos = []
	for i in range(0, 256, intervalo_quantizacao):
		lista_intervalos.append(i)

	#define a média de cada intervalo
	media_intervalos = []
	tamanho = len(lista_intervalos)
	for tam in range(0,(tamanho - 1)):
		if (tam+1):
			media_intervalos.append(((lista_intervalos[tam]+lista_intervalos[tam+1])/2))

	tam = 1
	for linha in range(0,altura):
		coluna = 0
		for coluna in range(0,largura):
			while tam != tamanho:
				if(img[linha,coluna] < lista_intervalos[tam]):
					Inova[linha,coluna] = media_intervalos[tam-1]
					tam=tamanho
				else:
					tam +=1
			tam = 1
			
	return Inova

#---------MAIN-----------------------------------------------------------------------

if __name__ == '__main__':

	verificaErroParametros()

	#pega percentual e tranforma em int
	percentual_amostragem = sys.argv[2]
	percentual_amostragem =  int(percentual_amostragem) /100

	#abre a imagem
	img = cv2 . imread (sys.argv[1], 0) 	
	dimensions = img.shape

	#pega a tecnica de amostragem e tranforma em int
	tecnica_amostragem = sys.argv[3] 
	tecnica_amostragem = int(tecnica_amostragem)

	#pega os niveis de cinza e tranforma em int
	niveis_cinza = sys.argv[4]
	niveis_cinza = int(niveis_cinza)

	janelas = tamanho_janela(percentual_amostragem,dimensions)	#retorna uma lista

	if(percentual_amostragem != 0):
	
		#SE O TAMANHO DA JANELA FOR REDONDO FAZ A AMOSTARGEM DE ACORDO COM A TÉCNICA PASSADA
		if dimensions[0] % janelas[0] == 0 and  dimensions [1] % janelas[1]== 0:
			imagem_amostrada = amostragem(img,tecnica_amostragem, dimensions,int(janelas[0]),int(janelas[1]),janelas[2],janelas[3])
				
		else:
			imagem_amostrada = interpolacao(img,tecnica_amostragem, dimensions,janelas[0],janelas[1],janelas[2],janelas[3] )
			
	else:
		print("O programa não fará amostragem dado que foi passado como parâmetro de amostreagem 0%")
		imagem_amostrada = img

	if niveis_cinza != 256 and niveis_cinza!= 0:
		if niveis_cinza == 2:
			imagem_quantizada = quantizacao_binaria(imagem_amostrada,janelas[2],janelas[3])
			imagem_quantizada = imagem_quantizada.astype(np.uint8)
			retval	=	cv2.imwrite(	'ImagemEDITADA.png', imagem_quantizada	)
			cv2.imshow('image',imagem_quantizada)
			cv2.waitKey(0)
		else:
			imagem_quantizada = quantizacao(imagem_amostrada,janelas[2],janelas[3],niveis_cinza)
			imagem_quantizada = imagem_quantizada.astype(np.uint8)
			retval	=	cv2.imwrite(	'ImagemEDITADA.png', imagem_quantizada	)
			cv2.imshow('image',imagem_quantizada)
			cv2.waitKey(0)
	else:
		time.sleep(3)    
		imagem_amostrada = imagem_amostrada.astype(np.uint8) 					
		retval	=	cv2.imwrite(	'ImagemEDITADA.png', imagem_amostrada	)
		cv2.imshow('image',imagem_amostrada)
		cv2.waitKey(0)