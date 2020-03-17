Trabalho de Amostragem e quantização referente a disciplina de Processamento de IMAGENS
																						
Aluna: Anna Caroline Bozzi																
GRR: 20173532		

Esse trabalho consiste em fazer Amostragem e Quantização de 
imagens passadas como parâmetro na linha de comando juntamente
com a execução, da da seguinte maneira:

trab1.py imagem %amostragem tecnica niveis_de_cinza, 
Por exemplo : python3 trab1.py exemplo.png 50 1 8
redução de 50% usando a média com 8 níeis

Caso seja passado %amostragem valendo 0, subentende-se que não
é para realizar a amostragem

O programa verificará a linha de comando sempre antes de executar
se passado alguma parâmetro inválido, será printado uma mensagem
e solicitado nova execução.

Cada execução plota uma imagem final de acordo com os parâmetros 
passados, do qual é necessário pressionar qualquer tecla para sair,
e iniciar uma nova execução. Juntamente com um arquivo salvo com
a imagem, que é sobrescrito a cada execução

Dado que possíveis inconsistências podem ocorrer em relação
ao tamanho da imagem e a Janela de amostragem, foi usado uma
técnica de arredondamento para valores de janela não inteiros.

Foi feito a implementação da ampliação, ela funciona quando digitado
valores acima de 100 na %amostragem, ESSA EXECUÇÃO DE AMPLIAÇÃO COM
QUANTIZAÇÃO DEMORA MAIS PARA EXECUTAR CONFORME MAIOR O NÚMERO DO 
NIVEL DE CINZA