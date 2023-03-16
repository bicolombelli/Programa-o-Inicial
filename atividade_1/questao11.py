num1 = int(input("Insira o primeiro valor a ser comparado:"))
num2 = int(input("Insira o segundo valor a ser comparado:"))
if (num1 = num2):
print("Que legal, o, num1, "é igual a", num2)
else:
print("O", num1, "é diferente de", num2)
Por que esse código não irá funcionar?
Porque o código devia estar assim:
num1 = int(input("Insira o primeiro valor a ser comparado:"))
num2 = int(input("Insira o segundo valor a ser comparado:"))
if (num1 == num2):
print("é igual a", num2)
else:
print("O", num1, "é diferente de", num2)
