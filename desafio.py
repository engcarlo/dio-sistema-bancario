# Importação de Pacotes
from datetime import datetime

# Constantes
LIMITE_NUMERO_SAQUES = 3
LIMITE_VALOR_SAQUES = 500

# Variáveis
G_saldo, G_n_saques = 0, 0
extrato = ""

# Booleano de Controle do Sistema
sys_on = True
input_deposito_valido = False
input_saque_valido = False

# Loop do Sistema
while sys_on == True:

    menu()
    menu_opcao = input("Selecione a opção desejada: ").upper()

    # Operação de Depósito
    if menu_opcao == "D":
        # Input de Depósito e Validação
        while input_deposito_valido == False:
            input_deposito = input("Digite a quantia a ser depositada: ")
            input_deposito_valido = transacao_valida(input_deposito)

        # Realização da Transação e Registro no Extrato
        G_saldo += input_deposito
        horario = hora_atual()
        extrato += f"[{horario}] Depósito: R$ {input_deposito:5.2f}\n"

        print(f"""
              =============== Operação de Depósito ================
              STATUS: Depósito realizado com sucesso.
              - Valor da Transação: R$ {input_deposito:5.2f}
              - Saldo Atual: R$ {G_saldo:5.2f}
              - Horário: {horario}
              =====================================================
              """)
        
    # Operação de Saque
    elif menu_opcao == "S":
        # Verificação da Quantidade Limite de Saques Diários
        if G_n_saques < LIMITE_NUMERO_SAQUES:
            # Input de Saque e Validação
            while input_deposito_valido == False:
                input_saque = input("Digite a quantia a ser depositada: ")
                input_saque_valido = transacao_valida(input_saque)

            # Verificação do Limite de Valor de Saque            
            if input_saque <= LIMITE_VALOR_SAQUES:
                # Verificação do Saldo Disponível
                if input_saque <= G_saldo:
                    G_saldo -= input_saque
                    G_n_saques += 1
                    horario = hora_atual()
                    extrato += f"[{horario}] Saque: R$ {input_saque:5.2f}\n"

                    print(f"""
                        ================= Operação de Saque =================
                        STATUS: Saque realizado com sucesso.
                        - Valor da Transação: R$ {input_saque:5.2f}
                        - Saldo Atual: R$ {G_saldo:5.2f}
                        - Horário: {horario}
                        ======================================================
                        """)
                else: 
                    print(f"""
                          ===================== ATENÇÃO! ======================
                          O valor do saque excede o seu saldo de R$ {G_saldo:5.2f}.
                          Tente novamente.
                          =====================================================
                          """)
            else:
                print(f"""
                      ===================== ATENÇÃO! ======================
                      O valor do saque excede o seu limite de R$ {LIMITE_VALOR_SAQUES:5.2f}.
                      Tente novamente.
                      =====================================================
                      """)

        else:
            print(f"""
                  ===================== ATENÇÃO! ======================
                  Você atingiu o seu limite de {LIMITE_NUMERO_SAQUES} saques diários.
                  Tente novamente amanhã.
                  =====================================================
                  """)
            
    # Operação de Extrato
    elif menu_opcao == "E":
        horario = hora_atual()
        if len(extrato) == 0:
            print(f"""
                  ================= Extrato Bancário ==================
                  STATUS.: Não Foram Realizadas Transações.
                  - Saldo Atual: R$ {G_saldo:5.2f}
                  - Número de Saques Realizados: {G_n_saques}
                  - Horário: {horario}
                  =====================================================
                  """)
        print(f"""
              ================= Extrato Bancário ==================
              STATUS: Solicitação de Extrato Realizada com Sucesso.
              - Saldo Atual: R${G_saldo:5.2f}
              - Número de Saques Realizados: {G_n_saques}
              - Horário: {horario}
              - Registro de Transações: 
              {extrato}
              =====================================================
              """)
        
    # Encerramento do Sistema
    elif menu_opcao == "Q":
        sys_on = False
        print("Sistema Encerrado.")
    
    # Opção Inválida
    else:
        print("Opção Inválida. Selecione uma opção válida.")

#%% Funções
# Função de Menu
def menu():
    horario = hora_atual()
    print(f"""
    =====================================================
    =================== Banco Dio.ME ====================
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    =====================================================
    Horário: {horario}
    =====================================================
    """)
    return

# Função de Validação de Transação
def transacao_valida(input_transacao):
    # Validação de Input Numérico
    input_valido = False
    if isinstance(input_transacao, (int, float)):
        input_transacao = float(input_transacao)
        input_valido = True
    else:
        print("Valor inválido. Digite um valor numérico.")
    return input_valido

# Função de Horário Atual
def hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Função de Resumo de Solicitação
def resumo_solicitacao(tipo_operacao, *args):
    if tipo_operacao == "deposito":
        print(f"""
            =============== Operação de Depósito ================
            STATUS: Depósito realizado com sucesso.
            - Valor da Transação: R$ {input_deposito:5.2f}
            - Saldo Atual: R$ {G_saldo:5.2f}
            - Horário: {horario}
            =====================================================
            """)
    elif tipo_operacao == "saque":
        print(f"""
            ================= Operação de Saque =================
            STATUS: Saque realizado com sucesso.
            - Valor da Transação: R$ {input_saque:5.2f}
            - Saldo Atual: R$ {G_saldo:5.2f}
            - Horário: {horario}
            ======================================================
            """)
    elif tipo_operacao == "extrato":
        if len(extrato) == 0:
            print(f"""
                ================= Extrato Bancário ==================
                STATUS.: Não Foram Realizadas Transações.
                Extrato Bancário
                - Saldo Atual: R$ {G_saldo:5.2f}
                - Número de Saques Realizados: {G_n_saques}
                - Horário: {horario}
                =====================================================
                """)
        else:
            print(f"""
                ================= Extrato Bancário ==================
                STATUS: Solicitação de Extrato Realizada com Sucesso.
                - Saldo Atual: R${G_saldo:5.2f}
                - Número de Saques Realizados: {G_n_saques}
                - Horário: {horario}
                - Registro de Transações: 
                {extrato}
                =====================================================
                """)
    else:
        print("Operação Inválida.")