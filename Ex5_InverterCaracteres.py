#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = input('Digite a palavra que deseja inverter: ')

string_invertida = palavra[::-1]

print(f'Palavra original: {palavra}, Palavra invertida: {string_invertida}')