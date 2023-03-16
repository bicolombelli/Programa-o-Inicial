print("Bem vindo a DrogariaT2")
farmacia = ["Dorflex", "Dramin", "Ibuprofeno", "Fluoxetina", "Omeprazol", "Paracetamol"]
menu = ""
caixa = 0
a = 0
while(menu != "s"):
    menu = input("a. Venda - b. Compra - c. Substituição - s. Sair \n")
    if(menu == "a"):
        print("Esses são os remédios disponíveis para venda: ")
        for i in farmacia:
            print(i)
        deletar = input("Insira o nome do remédio vendido: ")
        deletar_titulo = deletar.title()
        farmacia.remove(deletar_titulo)
        venda = float(input("Insira o valor da venda: "))
        caixa = caixa + venda
        print("Você vendeu o", deletar, "e o saldo do caixa é: ", caixa)
        print("O seu estoque ficou:")
        for i in farmacia:
            print(i)
 elif(menu == "b"):
        inserir = input("Insira o nome do remédio comprado: ")
        if (inserir == ""):
            print("O valor é inválido")
            break
        farmacia.append(inserir)
        compra = float(input("Insira o valor da compra"))
        caixa = caixa - compra
        print("Esses são os remédios do estoque")
        print("Você comprou o", inserir, "e o saldo do caixa é: ", caixa)
        for i in farmacia:
            print(i)
 elif(menu == "c"):
        print("Lista para inserir o valor")
        for i in farmacia:
           print(a, i)
           a += 1 
        substituir = int(input("Insira o NÚMERO do índice que será substituido: "))
        subst_dois = input("Insira o remédio que irá entrar no estoque: ")
        print("Lista atualizada: ")
        farmacia[substituir] = subst_dois
        for i in farmacia:
           print(i)
  elif(menu == "s"):
        print("Você saiu, até mais!")
   else:
        print("Valor inválido")
