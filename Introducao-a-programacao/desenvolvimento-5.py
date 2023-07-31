def calculadora(numero1,numero2,operacao):
    resultado = 0
    if (operacao == 1):
        resultado = numero1 + numero2
    elif (operacao == 2):
        resultado = numero1 - numero2
    elif (operacao == 3):
        resultado = numero1 * numero2
    elif (operacao == 4 and numero2 != 0):
        resultado = numero1 / numero2
    return resultado

menu = """
1. Soma
2. Subtracao
3. Multiplicacao
4. Divisao
0. Sair
"""
   
while (True):
    codigo = int(input(f"""Selecione a operacao: """+ menu)) 
    if (codigo == 0):
        break
    
    numero1 = int(input("Digite o primeiro numero: ")) 
    numero2 = int(input("Digite o segundo numero: ")) 

    resultadoOperacao = calculadora(numero1, numero2, codigo)
    print("Resultado: ", resultadoOperacao)