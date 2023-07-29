numero1=5
numero2=0
operador=4

def calculadora(numero1,numero2,operador):
    if(operador == 1):
      return (numero1 + numero2)
    elif(operador == 2):
      return(numero1 - numero2)
    elif(operador == 3):
      return(numero1 * numero2)
    elif(operador == 4):
      if(numero2 == 0):
        return("Não é possivel realizar a divisao")
      else:
       return(numero1 / numero2)

resultado = calculadora(numero1,numero2,operador)
print(resultado)