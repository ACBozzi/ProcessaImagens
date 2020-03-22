import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

veorImagens = ['hulk1.png', 'hulk2.png', 'iron1.png', 'iron2.png', 'k3po1.png', 'k3po2.png',
'magneto1.png', 'magneto2.png','trooper1.png', 'trooper2.png', 'vader1.png', 'vader2.png', 'volve1.png', 'volve2.png']

#---------------------CRIA HISTOGRAMA---------------------------------

def cria_histograma(img, dimensions):
	plt.style.use('dark_background')

	histoVetor = []
	for i in range(0,256):
		histoVetor.append(0)

	#vetor de 0 a 256 com a quantidade de cada cor correspondente
	#arquivo = open ('matriz.txt', 'w')
	for i in range(0,dimensions[0]):
		for j in range(0,dimensions[1]):
			#arquivo.write(str(img[i,j]))
			#arquivo.write(", ")
			histoVetor[img[i,j]] +=1 

	#arquivo.close()
	indiceCores = []
	for i in range(0,256):
		indiceCores.append(i)

	plt.plot(indiceCores,histoVetor)
	plt.show()
#---------------------------------------------------------------------

if __name__ == '__main__':
	img = cv2.imread('hulk1.png', 0)
	dimensions = img.shape
	cria_histograma(img,dimensions)