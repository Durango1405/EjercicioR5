# cálculo de una suma
suma = 0
x = 20 
# a la suma inicial, se le agrega el valor de x
suma = suma + x
y = 40
# al valor de x, le sumamos el valor de y pero elevado al cuadrado
x = x + y**2
# al valor actual de la suma, se le añade el resultado de la división entre la variable x y la variable y
suma = suma + (x/y)
#resultado final de la suma
print("El valor de la suma es:", suma)