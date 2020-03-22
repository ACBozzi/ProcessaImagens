
import cv2
import matplotlib.pyplot as plt

#Funcao para comparacao com correlacao
def comparadorCorrelacao(imagem, vetorImagens):
	maisParecido = 0
	for img in vetorImagens:
		if(img != imagem):
			img1 = cv2.imread(imagem)
			img2 = cv2.imread(img)
			color = [(255,0,0),(0,255,0),(0,0,255)]
			soma = 0
			for ch,col in   enumerate(color):
				hist_item1 = cv2.calcHist([img1] ,[ch] ,None,[256] ,[0 ,255])
				hist_item2 = cv2.calcHist([img2] ,[ch] ,None,[256] ,[0 ,255])
				cv2.normalize(hist_item1 , hist_item1 ,0 ,255 ,cv2 .NORM_MINMAX)
				cv2.normalize(hist_item2 , hist_item2 ,0 ,255 ,cv2 .NORM_MINMAX)
				sc= cv2.compareHist(hist_item1 ,  hist_item2 , cv2.HISTCMP_CORREL)
				soma+=sc
			if( (soma<= 3 and soma>maisParecido) or maisParecido == 0):
				maisParecido = soma
				imagemParecida= img
	return imagemParecida

#COmparacao com quiquadrado
def comparadorCHISQR(imagem, vetorImagens):
	maisParecido = 0
	for img in vetorImagens:
		if(img != imagem):
			img1 = cv2.imread(imagem)
			img2 = cv2.imread(img)
			color = [(255,0,0),(0,255,0),(0,0,255)]
			soma = 0
			for ch,col in   enumerate(color):
				hist_item1 = cv2.calcHist([img1] ,[ch] ,None,[256] ,[0 ,255])
				hist_item2 = cv2.calcHist([img2] ,[ch] ,None,[256] ,[0 ,255])
				cv2.normalize(hist_item1 , hist_item1 ,0 ,255 ,cv2 .NORM_MINMAX)
				cv2.normalize(hist_item2 , hist_item2 ,0 ,255 ,cv2 .NORM_MINMAX)
				sc= cv2.compareHist(hist_item1 ,  hist_item2 , cv2.HISTCMP_CHISQR)
				soma+=sc
			if( soma < maisParecido or maisParecido == 0):
				maisParecido = soma
				imagemParecida= img
			soma=0
	return imagemParecida

#Comparacao com intercessao
def comparadorIntercessao(imagem, vetorImagens):
	maisParecido = 0
	for img in vetorImagens:
		if(img != imagem):
			img1 = cv2.imread(imagem)
			img2 = cv2.imread(img)
			color = [(255,0,0),(0,255,0),(0,0,255)]
			soma = 0
			for ch,col in   enumerate(color):
				hist_item1 = cv2.calcHist([img1] ,[ch] ,None,[256] ,[0 ,255])
				hist_item2 = cv2.calcHist([img2] ,[ch] ,None,[256] ,[0 ,255])
				cv2.normalize(hist_item1 , hist_item1 , 1.0, 0.0, cv2.NORM_L1)
				cv2.normalize(hist_item2 , hist_item2 , 1.0, 0.0, cv2.NORM_L1)
				sc= cv2.compareHist(hist_item1 ,  hist_item2 , cv2.HISTCMP_INTERSECT)
				soma+=sc
			if(soma > maisParecido):
				maisParecido = soma
				imagemParecida= img
			soma=0
	return imagemParecida

#Comparacao com BHATTACHARYYA
def comparadorBHATTACHARYYA(imagem, vetorImagens):
	maisParecido = 100
	for img in vetorImagens:
		if(img != imagem):
			img1 = cv2.imread(imagem)
			img2 = cv2.imread(img)
			color = [(255,0,0),(0,255,0),(0,0,255)]
			soma = 0
			for ch,col in   enumerate(color):
				hist_item1 = cv2.calcHist([img1] ,[1] ,None,[256] ,[0 ,255])
				hist_item2 = cv2.calcHist([img2] ,[1] ,None,[256] ,[0 ,255])
				cv2.normalize(hist_item1 , hist_item1 ,0 ,255 ,cv2 .NORM_MINMAX)
				cv2.normalize(hist_item2 , hist_item2 ,0 ,255 ,cv2 .NORM_MINMAX)
				sc= cv2.compareHist(hist_item1 ,  hist_item2 , cv2.HISTCMP_BHATTACHARYYA)
				soma+=sc
			if(soma < maisParecido and soma>0):
				maisParecido = soma
				imagemParecida= img
			soma=0
	return imagemParecida

#Vetor de imagens
vetorImagens = ['hulk1.png', 'hulk2.png', 'iron1.png', 'iron2.png', 'k3po1.png', 'k3po2.png',
'magneto1.png', 'magneto2.png','trooper1.png', 'trooper2.png', 'vader1.png', 'vader2.png', 'volve1.png', 'volve2.png']

#vetor de respostas(imagens semelhantes)
vetorImagensCorrespondentes = ['hulk2.png', 'hulk1.png', 'iron2.png', 'iron1.png','k3po2.png',
'k3po1.png', 'magneto2.png', 'magneto1.png', 'trooper2.png', 'trooper1.png',
'vader2.png', 'vader1.png', 'volve2.png', 'volve1.png']

i=0
BHATTACHARYYA=0
correlacao=0
CHISQR = 0
intercessao =0
#Percorre a lista de imagens comparando com as 13 demais
for imagem in vetorImagens:
	 if(comparadorCorrelacao(imagem, vetorImagens) == vetorImagensCorrespondentes[i]):
		 correlacao+=1
	 if(comparadorCHISQR(imagem, vetorImagens) == vetorImagensCorrespondentes[i]):
		 CHISQR+=1
	 if(comparadorIntercessao(imagem, vetorImagens) == vetorImagensCorrespondentes[i]):
		 intercessao+=1
	 if(comparadorBHATTACHARYYA(imagem, vetorImagens) == vetorImagensCorrespondentes[i]):
		 BHATTACHARYYA+=1
	 i+=1

print('--------------------------------------------')
print('Taxa de acerto de CV_COMP_CORREL ')
print(str((correlacao/14.0)*100)+'%' )
print('--------------------------------------------')
print('Taxa de acerto de CV_COMP_CHISQR: ')
print(str((CHISQR/14.0)*100)+'%' )
print('--------------------------------------------')
print('Taxa de acerto de CV_COMP_INTERSECT: ')
print(str((intercessao/14.0)*100)+'%' )
print('--------------------------------------------')
print('Taxa de acerto de CV_COMP_BHATTACHARYYA: ')
print(str((BHATTACHARYYA/14.0)*100)+'%' )
