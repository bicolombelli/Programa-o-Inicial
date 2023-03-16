print("Olá, seja bem vindo a nossa loja!") 
menu = " " 
conta_caixa = 0 
while(menu != "s"): 
menu = input("a. compra - b. pagamento - c. consultar caixa - s. sair ") 
if (menu == "a"): 
compra = float(input("Insira o valor da sua compra: ")) print("O valor da sua compra é de: ", conta_caixa + compra) conta_caixa + conta_caixa 
if (menu == "b"): 
pagamento = float(input("Insira o pagamento: ")) 
print("O valor do pagamento é: ", conta_caixa + pagamento) conta_caixa + conta_caixa 
if (menu == "c"): 
consultar = print("O valor da sua conta é ", conta_caixa) compra + pagamento 
if (menu == "s"): 
print("você escolheu sair! Até logo.")
