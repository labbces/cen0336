#!/usr/bin/end python3

def set_local_x_to_five(x):
  print('Dentro de def')
  x = 5 # localmente para set_local_x_to_five()
  y=5   # também local
  print("x =",x)
  print("y = ",y)

print('Após def')
x = 100 # global x
y = 100 # global
print('x=',x)
print('y=',y)

set_local_x_to_five(500)
print('Após chamada da função')
print('x=',x)
print('y=',y)
