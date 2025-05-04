# Calcular multa sobre excedente de quantidade de pescados
LIMITE = 100.0

MULTA = 4.00

qtde = float(input("Informe a quantidade de peixes: "))
if qtde > LIMITE:
    excesso = qtde - LIMITE
    multa = excesso * MULTA
    print(f"Excedeu {excesso:.2f} kg e a multa é de R$ {multa:.2f}")
else:
    print("Não houve excesso de peso")

# print("Fim do programa")