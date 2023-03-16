litros = float(input("Digite quantos litros você quer abastecer: "))
combustível = input("Digite A para álcool ou G para gasolina: ")
preço = 0
if combustível == "A" or combustível == "a":
preço = litros * 1.90
if litros <= 20:
preço -= 1.90 * litros * 3 / 100
else:
preço -= 1.90 * litros * 5 / 100
elif combustível == "G" or combustível == "g":
preço = litros * 2.5
if litros <= 20:
preço -= 2.50 * litros * 4 / 100
else:
preço -= 2.50 * litros * 6 / 100
print(f"O preço a pagar é R${preço:.2f}")
