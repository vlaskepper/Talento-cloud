# Desenvolvimento 2

var int quantidadeRodas

var int quantidadePessoas

var float pesoBruto


## Inicio

print(“Digite a quantidade de rodas do veículo”)

input(quantidadeRodas)

print(“Digite o peso do veículo”)

input(pesoBruto)

print(“Digite a quantidade de pessoas”)

input(quantidadePessoas)

if(quantidadeRodas == 2) or (quantidadeRodas == 3):
print(“Sua habilitação é A”)

elif(quantidadeRodas == 4) and (quantidadePessoas <=8) and (pesoBruto <= 3500):

print(“Sua habilitação é B”)

elif(quantidadeRodas == 4) or (pesoBruto >3500) and (pesoBruto <=6000)

print(“Sua habilitação é C”)

elif((quantidadeRodas >= 4) and (quantidadePessoas >8)) and ((quantidadeRodas >= 4) and (pesoBruto >6000))

print(“Sua habilitação é D”)
