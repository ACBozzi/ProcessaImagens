Trabalho de Amostragem e quantização referente a disciplina de Processamento de IMAGENS
																						
Aluna: Anna Caroline Bozzi																
GRR: 20173532		

Esse trabalho consiste em fazer Amostragem e Quantização de 
imagens passadas como parâmetro na linha de comando juntamente
com a execução, da da seguinte maneira:

trab1.py imagem %amostragem tecnica niveis_de_cinza

Caso seja passado %amostragem valendo 0, subentende-se que não
é para realizar a amostragem

O programa verificará a linha de comando sempre antes de executar
se passado alguma parâmetro inválido, será printado uma mensagem
e solicitado nova execução.

Cada execução plota uma imagem final de acordo com os parâmetros 
passados, do qual é necessário pressionar qualquer tecla para sair,
e iniciar uma nova execução.

Dado que possíveis inconsistências podem ocorrer em relação
ao tamanho da imagem e a Janela de amostragem, foi usado uma
técnica de arredondamento para valores de janela não inteiros.
