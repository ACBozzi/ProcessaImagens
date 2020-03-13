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


def tamanho_janela(percentual_amostragem,dimensions):	
	nova_altura = dimensions[0] - (dimensions[0]*percentual_amostragem)
	nova_largura = dimensions[1] - (dimensions[1]*percentual_amostragem)
	janela1 = dimensions[0] / int(nova_altura)
	janela2 = dimensions[1] / int(nova_largura)
	print(janela1,janela2)
	return int(janela1), int(janela2)

# CASO O TAMANHO DA IMAGEM SEJA PAR, NÃO PRECISA INTERPOLAR E ENTRA AQUI PARA FAZER MODA MEDIANA E MEDIA 
def amostragem(img,tipo, dimensions):
	if tipo == 1:	#media
		for j in range(0, dimensions[1]-1,janela2):	#coluna
			for i in range(0,dimensions[0]-1, janela1):	#linha
				for x in range(i, (i+janela1)-1):
					for y in range(j, (j+janela2)-1):
						Inova[Lnova,Cnova] += img[x,y] #fazendo a soma dos elementos para a media 
				Inova[Lnova,Cnova] = Inova[Lnova,Cnova] / janela1*janela2	#aqui faz a media
	
	elif tipo ==2:
		for j in range(0, dimensions[1]-1,janela2):	#coluna
			for i in range(0,dimensions[0]-1, janela1):	#linha
				for x in range(i, (i+janela1)-1):
					for y in range(j, (j+janela2)-1):
						lista = []
						lista.push(img[x,y])
						lista_ordenada = sorted(lista) 
						#fazer o calculo aqui
		print("fazer mediana")
	
	else:
		print("fazer a moda")




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


if __name__ == '__main__':

	verificaErroParametros()

	#pega percentual e tranforma em int
	percentual_amostragem = sys.argv[2]
	percentual_amostragem =  int(percentual_amostragem) /100

	#abre a imagem
	img = cv2 . imread (sys.argv[1], 0) 	
	dimensions = img.shape

	#pega a tecnica de amostragem
	tecnica_amostragem = sys.argv[3] 
	tecnica_amostragem = int(tecnica_amostragem)

	#pega os niveis de cinza
	niveis_cinza = sys.argv[4]
	niveis_cinza = int(niveis_cinza)


	janelas = tamanho_janela(percentual_amostragem,dimensions)	#retorna uma lista
	if janelas[0] % dimensions[0] == 0 and janelas[1] % dimensions [1] == 0:
		#caso de não interpolação
		tecnica_amostragem(img,tecnica_amostragem)
	else:
		print("interpolacao")


	print(janelas)