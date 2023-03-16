nota1 = float(input("Insira uma nota: "))
nota2 = float(input("Insira outra nota: "))
nota3 = float(input("Insira outra nota: "))
media1 = (nota1 + nota2 + nota3) / 3
if(media1 >= 7):
print(" A média foi de ", media1, "você está aprovado(a), parabéns!")
else:
print("A média foi de", media1, ", que pena, você está reprovado(a).")
