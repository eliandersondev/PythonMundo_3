'''
Desafio 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.
'''

from random import randint

t = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),)
t = sorted(t)
print('O maior é: ', t[4])
print('O manor é: ', t[0])
print(t)
print(max(t))
print(min(t))