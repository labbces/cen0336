#!/usr/bin/env python3
print('Antes do bloco if')
x = 100
print('x=',x)
if True:  # esta condição if será sempre Verdadeira     
  # queremos garantir que o bloco seja executado
  # para que possamos mostrar o que acontece
  print('Dentro do bloco if')
  x = 30
  y = 10
  print("x=", x)
  print("y=", y)

print('Após o bloco if')
print("x=", x)
print("y=", y)
