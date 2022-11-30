from functools import reduce

impares = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f'Lista de elementos impares: \n {list(impares)}')

print(f'La suma de elementos impares es:\n {reduce(lambda a, b: a+b, impares)}')
