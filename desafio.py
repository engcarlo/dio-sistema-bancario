# Importação de Pacotes
from datetime import datetime


# Menu do programa
menu = """
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
"""

# Constantes
LIMITE_NUMERO_SAQUES = 3
LIMITE_VALOR_SAQUES = 500

# Variáveis
G_saldo, G_n_saques = 0, 0
extrato = ""


sys_on = True

def hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

while sys_on == True:

    print(menu)
    menu_opcao = input("Selecione a opção desejada: ".upper())

    if menu_opcao == "D":
        input_deposito = float(input("Digite a quantia a ser depositada: "))
        saldo += input_deposito
        horario = hora_atual()
        extrato += f"[" + horario + "] Depósito: R${input_deposito:5.2f}\n"

        print(f"""
              Depósito realizado com sucesso.
              - Valor da Transação: R${input_deposito:5.2f}
              - Saldo Atual: R${G_saldo:5.2f}
              - Horário: {horario}
              """)
        
    elif menu_opcao == "S":
        if G_n_saques <= LIMITE_NUMERO_SAQUES:
            input_saque = float(input("Digite a quantia a ser sacada: "))
            if input_saque <= LIMITE_VALOR_SAQUES:
                if input_saque <= G_saldo:
                    G_saldo -= input_saque
                    G_n_saques += 1
                    horario = hora_atual()
                    extrato += f"[" + horario + "] Saque: R${input_saque:5.2f}\n"

                    print(f"""
                        Saque realizado com sucesso.
                        - Valor da Transação: R${input_saque:5.2f}
                        - Saldo Atual: R${G_saldo:5.2f}
                        - Horário: {horario}
                        """)
                else: 
                    print(f"""
                          O valor do saque excede o seu saldo de R${G_saldo:5.2f}.
                          Tente novamente.
                          """)
            else:
                print(f"""
                      O valor do saque excede o seu limite de R${LIMITE_VALOR_SAQUES:5.2f}.
                      Tente novamente.
                      """)

        else:
            print(f"""
                  Você atingiu o seu limite de {LIMITE} saques diários.
                  Tente novamente amanhã.
                  """)
    elif menu_opcao == "E":
        horario = hora_atual()
        if len(extrato) == 0:
            print(f"""
                  OBS.: Não Foram Realizadas Transações.
                  Extrato Bancário
                  - Saldo Atual: R${G_saldo:5.2f}
                  - Número de Saques Realizados: {G_n_saques}
                  - Horário: {horario}
                  """)
        print(f"""
              ================= Extrato Bancário =================
              - Saldo Atual: R${G_saldo:5.2f}
              - Número de Saques Realizados: {G_n_saques}
              - Horário: {horario}
              - Registro de Transações: 
              {extrato}
              =====================================================
              """)
    elif menu_opcao == "Q":
        sys_on = False
        print("Sistema Encerrado.")
    
    else:
        print("Opção Inválida. Selecione uma opção válida.")

