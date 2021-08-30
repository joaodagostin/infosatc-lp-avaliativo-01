#Calculo de latas e mostrar o valor gasto
altura = float(input("Digite a altura da parede em metros: "))
compri = float(input("Digite o comprimento da parede em metros: "))
m2 = (altura*compri)
consumo = m2/3
print("Consumo de {:.2f} litros".format(consumo))
latas = consumo/3.6
print("A quantidade de LATAS de 3,6 LITROS a ser usado é: {}".format(latas))
valor = latas * 107.0
print("O valor total é de: {:.2f} reais".format(valor))