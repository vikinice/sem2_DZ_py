#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    count = 1
    for i in range (1, n+1):
        count*= i
        print(count)
n = int(input('Введите число N: '))
factorial(n)