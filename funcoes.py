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


def open(file):
	print(dimensions)
	return dimensions

#-------------------------------------------------------------------------------------------------------------------
#FUNÇÃO PARA DEFINIR O TAMANHO DA JANELA
def tamanho_janela(percentual_amostragem,dimensions):	
	nova_altura = dimensions[0] - (dimensions[0]*percentual_amostragem)
	nova_largura = dimensions[1] - (dimensions[1]*percentual_amostragem)
	janela1 = dimensions[0] / int(nova_altura)
	janela2 = dimensions[1] / int(nova_largura)
	print("TAMANHO DA JANELA:",janela1,janela2)
	return int(janela1), int(janela2), int(nova_altura), int(nova_largura)

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

#-------------------------------------------------------------------------------------------------------------------------
# CASO O TAMANHO DA IMAGEM SEJA PAR, NÃO PRECISA INTERPOLAR E ENTRA AQUI PARA FAZER MODA, MEDIANA OU MEDIA 
def amostragem(img,tipo, dimensions,janela1,janela2,alturaNova,larguraNova):
	Inova = np.zeros((alturaNova,larguraNova), dtype = int)
	Lnova = 0
	Cnova = 0

	# se o parametro passado for um então a técnica é a media
	if tipo == 1:
		print("ENTROU NA MEDIA")
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
		print("REDUZIDA:", tamanho)

	# se o parâmetro for dois então é mediana
	elif tipo ==2:
		for linha in range(0, dimensions[0],janela1):	#coluna
			Cnova = 0
			for coluna in range(0,dimensions[1], janela2):	#linha
				for x in range(linha, (linha+janela1)):
					for y in range(coluna, (coluna+janela2)):
						lista = []
						lista.append(img[x,y])
						lista_ordenada = sorted(lista) 
					if len(lista_ordenada) % 2 == 0:
						print("a janela é par")
		print("fazer mediana")
	
	#senão é a moda
	else:
		print("fazer a moda")

#----------------------------------------------------------------------------------------------------------
#MAIN
if __name__ == '__main__':

	verificaErroParametros()

	#pega percentual e tranforma em int
	percentual_amostragem = sys.argv[2]
	percentual_amostragem =  int(percentual_amostragem) /100
	print("percentual de amostragem:", percentual_amostragem)

	#abre a imagem
	img = cv2 . imread (sys.argv[1], 0) 	
	#print("Original", img)
	dimensions = img.shape
	print("DIMENÇÃO ORIGINAL:", dimensions)

	#pega a tecnica de amostragem e tranforma em int
	tecnica_amostragem = sys.argv[3] 
	tecnica_amostragem = int(tecnica_amostragem)
	print("tecnica de amostragem:", tecnica_amostragem)

	#pega os niveis de cinza e tranforma em int
	niveis_cinza = sys.argv[4]
	niveis_cinza = int(niveis_cinza)
	print("niveis de cinza:", niveis_cinza)

	# PEGA AS DIMENSÕES DA IMAGEM ORIGINAL E DESCOBRE O TAMANHO DA JANELA
	janelas = tamanho_janela(percentual_amostragem,dimensions)	#retorna uma lista
	
	#SE O TAMANHO DA JANELA FOR REDONDO FAZ A AMOSTARGEM DE ACORDO COM A TÉCNICA PASSADA
	if dimensions[0] % janelas[0] == 0 and  dimensions [1] % janelas[1]== 0:
		amostragem(img,tecnica_amostragem, dimensions,janelas[0],janelas[1],janelas[2],janelas[3])
	else:
		print("interpolacao")


	print("jnaela1,janela2, altura e largura: ",janelas)