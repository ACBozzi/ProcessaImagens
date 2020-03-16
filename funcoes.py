#Implemente um programa que realize amostragem de quantização em uma imagem monocromática. O 
#programa deve receber como parâmetros o nome da imagem, o porcentual de amostragem, a técnica de 
#amostragem (média, mediana ou moda.) e a quantidade de níveis de cinza [2,4,8,16,32,64,128,256] 
#(quantização). A saída do programa deve ser a imagem amostrada. Utilize a imagem exemplo.png para 
#testar o programa.

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
#----------------------------------------------------------------------------------------------------------------------
#### FUNÇÃO PARA VERIFICAÇÃO DE ERROS PASSADOS EM PARÂMETRO##
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


#-------------------------------------------------------------------------------------------------------------------
#FUNÇÃO PARA DEFINIR O TAMANHO DA JANELA
def tamanho_janela(percentual_amostragem,dimensions):	
	nova_altura = dimensions[0] - (dimensions[0]*percentual_amostragem)
	nova_largura = dimensions[1] - (dimensions[1]*percentual_amostragem)
	janela1 = dimensions[0] / int(nova_altura)
	janela2 = dimensions[1] / int(nova_largura)
	return float(janela1), float(janela2), int(nova_altura), int(nova_largura)


#-------------------------------------------------------------------------------------------------------------------------
# CASO O TAMANHO DA IMAGEM SEJA PAR, NÃO PRECISA INTERPOLAR E ENTRA AQUI PARA FAZER MODA, MEDIANA OU MEDIA 
def amostragem(img,tipo, dimensions,janela1,janela2,alturaNova,larguraNova):
	Inova = np.zeros((alturaNova,larguraNova), dtype = int)
	Lnova = 0
	Cnova = 0

	# se o parametro passado for um então a técnica é a media
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
		Inova = Inova.astype(np.uint8) 
		cv2.imshow('image',Inova)
		cv2.waitKey(0)
		tamanho = Inova.shape

	# se o parâmetro for dois então é mediana
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
	
	#senão é a moda
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
					print("Essa janela não pode usar a moda para calculo, foi utilizado a media")
					media = statistics.mean(lista)
					Inova[Lnova,Cnova] = media
					lista.clear()
				Cnova+=1
			Lnova+=1
		Inova = Inova.astype(np.uint8) 
		tamanho = Inova.shape

	return Inova

#----------------------------------------------------------------------------------------------------------

#CASO O VALOR DA JANELA NÃO SEJA EXATO FAZER INTERPOLAÇÃO
def interpolacao(img,janela1,janela2,alturaNova,larguraNova):
	Inova = np.zeros((alturaNova,larguraNova), dtype = int)
	
	k = 0
	l = 0
    
	for i in range(0, alturaNova, janela1):
		for j in range(0, larguraNova, janela2):
			Inova[k,l] = img[i,j]
			l+=1
		l = 0
		k+=1
	
	return Inova
#----------------------------------------------------------------------------------------------------------

#def interpolacao_add_zeros(img,nova_altura,nova_largura):

#----------------------------------------------------------------------------------------------------------

def quantizacao_binaria(img,altura,largura):

	for linha in range(0,altura):
		for coluna in range(0,largura):
			if img[linha,coluna] < 128:
				img[linha,coluna] = 0
			else:
				img[linha,coluna] = 255
		coluna = 0
	
	return img

#----------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------------

#MAIN
if __name__ == '__main__':

	verificaErroParametros()

	#pega percentual e tranforma em int
	percentual_amostragem = sys.argv[2]
	percentual_amostragem =  int(percentual_amostragem) /100

	#abre a imagem
	img = cv2 . imread (sys.argv[1], 0) 	
	#print("Original", img)
	dimensions = img.shape
	#print("DIMENÇÃO ORIGINAL:", dimensions)

	#pega a tecnica de amostragem e tranforma em int
	tecnica_amostragem = sys.argv[3] 
	tecnica_amostragem = int(tecnica_amostragem)
	#print("tecnica de amostragem:", tecnica_amostragem)

	#pega os niveis de cinza e tranforma em int
	niveis_cinza = sys.argv[4]
	niveis_cinza = int(niveis_cinza)
	#print("niveis de cinza:", niveis_cinza)

	janelas = tamanho_janela(percentual_amostragem,dimensions)	#retorna uma lista

	
	if(percentual_amostragem != 0):

		# PEGA AS DIMENSÕES DA IMAGEM ORIGINAL E DESCOBRE O TAMANHO DA JANELA
		
		
		#SE O TAMANHO DA JANELA FOR REDONDO FAZ A AMOSTARGEM DE ACORDO COM A TÉCNICA PASSADA
		if dimensions[0] % janelas[0] == 0 and  dimensions [1] % janelas[1]== 0:
			imagem_amostrada = amostragem(img,tecnica_amostragem, dimensions,int(janelas[0]),int(janelas[1]),janelas[2],janelas[3])
			
			#imagem_amostrada = imagem_amostrada.astype(np.uint8) 					
			#cv2.imshow('image',imagem_amostrada)
			#cv2.waitKey(0)
		
		else:
			imagem_amostrada = interpolacao(img,int(janelas[0]),int(janelas[1]),janelas[2],janelas[3] )
			
			#imagem_amostrada = imagem_amostrada.astype(np.uint8)
			#cv2.imshow('image',imagem_amostrada)
			#cv2.waitKey(0)
	else:
		print("O programa não fará amostragem dado que foi passado como parâmetro de amostreagem 0%")
		imagem_amostrada = img

	if niveis_cinza != 256 and niveis_cinza!= 0:
		if niveis_cinza == 2:
			imagem_quantizada = quantizacao_binaria(imagem_amostrada,janelas[2],janelas[3])
			imagem_quantizada = imagem_quantizada.astype(np.uint8)
			cv2.imshow('image',imagem_quantizada)
			cv2.waitKey(0)
		else:
			imagem_quantizada = quantizacao(imagem_amostrada,janelas[2],janelas[3],niveis_cinza)
			imagem_quantizada = imagem_quantizada.astype(np.uint8)
			cv2.imshow('image',imagem_quantizada)
			cv2.waitKey(0)
	else:
		time.sleep(3)    
		imagem_quantizada = imagem_quantizada.astype(np.uint8) 					
		cv2.imshow('image',imagem_quantizada)
		cv2.waitKey(0)


	

	#print("jnaela1,janela2, altura e largura: ",janelas)