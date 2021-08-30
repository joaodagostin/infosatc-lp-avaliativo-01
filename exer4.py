total = float(input("Digite o valor total do premio: "))
liqui = total-total*(7/100)
print("Valor em reais com desconto: {:.2f}".format(liqui))
g1 = liqui*0.46
g2 = liqui*0.32
g3 = liqui-(g1+g2)
print("Ganhador 1(em reais): {:.2f}".format(g1))
print("Ganhador 2(em reais): {:.2f}".format(g2))
print("Ganhador 3(em reais): {:.2f}".format(g3))