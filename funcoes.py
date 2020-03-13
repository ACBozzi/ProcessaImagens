#Implemente um programa que realize amostragem de quantização em uma imagem monocromática. O 
#programa deve receber como parâmetros o nome da imagem, o porcentual de amostragem, a técnica de 
#amostragem (média, mediana ou moda.) e a quantidade de níveis de cinza [2,4,8,16,32,64,128,256] 
#(quantização). A saída do programa deve ser a imagem amostrada. Utilize a imagem exemplo.png para 
#testar o programa.

import numpy as np
import cv2
import sys
from PIL import Image
from matplotlib import pylab
from pylab import *
import os
from numpy import *


def open(file):
	img = cv2 . imread (file, 0) 	
	dimensions = img.shape
	print(dimensions)

def histograma(file):
	histograma = histeq(file)
	imshow(histograma)
	subplot(2,2,3)

#def amostragem(img,percent):


if __name__ == '__main__':
	open(sys.argv[1])
	percentual_amostragem = sys.argv[2]
	tecnica_amostragem = sys.argv[3] 
	niveis_cinza = sys.argv[4]
	histograma(sys.argv[1])
	