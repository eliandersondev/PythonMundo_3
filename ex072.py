'''
Desafio 072
Crie um programa que tenha uma tuola total preenchida com uma contagen por extensão,
de zero até vinte. Seu programa deverá ler um número pelo teclaçdo (entre 0 e 20)
e mostrá-lo por extenso.
'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
while n > 20:
    n = int(input('Tente novamengte. Digite um número entre 0 e 20: '))

print('Você digitou o número {}'.format(numeros[n]))
