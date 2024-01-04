menu= """  
[d]deposito
[s]sacar
[e]extrato
[q]sair
=> """
#String multilínea - docstring
saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:

    opcao = input(menu)
    #Solução de depósito:
    if opcao == "d":
         valor= float(input("Informe o valor do depósito:"))
      #Verifica valor, evita depósito negativo
         if valor > 0:
              saldo += valor #atribuição com operação de adição
              extrato += f'Depósito: R$ {valor:.2f}\n' #concatenação     
         else: #caso valor de depósito negativo
          print("Operação inválida!Valor informado inválido.")

    elif opcao == "s":
         valor= float(input("Informa o valor do saque:"))
         excedeu_saldo= valor > saldo #Não permite saque
         excedeu_limite= valor > limite #Não permite saque
         excedeu_saques= numero_saques >= limite_saque #Passou limte diarios de 3 saques

         if excedeu_saldo:
          print("Operação falhou! Saldo insuficiente.")

         elif excedeu_limite:
          print("Operação falhou! Valor de saque excedeu limite.")

         elif excedeu_saques:
          print("Número máximo de saques excedidos!")

         elif valor > 0:
          saldo -= valor

          extrato += f"saque: R$ {valor:.2f}\n"

          numero_saques +=1
         else:
            print("Operação falhou! Valor informado inválido!")
    
    elif opcao == "e":
        print("\n =================EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato) #If ternário
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        break
    else:
       print("Opção inválida!Por favor selecione novamente a opção desejada.")
          
    





