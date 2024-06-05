#!/usr/bin/env python3

def set_global_variable():
  global greeting  # torna a variável "greeting" global
  greeting = "Eu digo olá"


greeting = 'Bom dia'
print('Antes da chamada de função')
print('greeting =',greeting)

#fazendo a chamada da função
set_global_variable()
print('Após a chamada de função')
print('greeting =',greeting)
