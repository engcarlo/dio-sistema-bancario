# Importação de Pacotes
from datetime import datetime

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
    =====================================================""")
    return

# Função de Validação de Transação
def transacao_valida(input_transacao):
    # Validação de Input Numérico
    input_valido = False
    try:
        input_transacao = float(input_transacao)
        if isinstance(input_transacao, (int, float)):
            input_valido = True
        else:
            print("Valor inválido. Digite um valor numérico.")
    except ValueError:
        print("Valor inválido. Digite um valor numérico.")
    return input_valido, input_transacao

# Função de Horário Atual
def hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Função de Resumo de Solicitação
def resumo_solicitacao(tipo_operacao, *args):
    if tipo_operacao == "D":
        print(f"""
        =============== Operação de Depósito ================
              
        STATUS: Depósito realizado com sucesso.
        - Valor da Transação: R$ {input_deposito:5.2f}
        - Saldo Atual: R$ {G_saldo:5.2f}
        - Horário: {horario}

        =====================================================""")
    elif tipo_operacao == "S":
        print(f"""
        ================= Operação de Saque =================
              
        STATUS: Saque realizado com sucesso.
        - Valor da Transação: R$ {input_saque:5.2f}
        - Saldo Atual: R$ {G_saldo:5.2f}
        - Horário: {horario}

        ======================================================""")
    elif tipo_operacao == "E":
        if len(extrato) == 0:
            print(f"""
            ================= Extrato Bancário ==================
                  
            STATUS.: Não Foram Realizadas Transações.
            Extrato Bancário
            - Saldo Atual: R$ {G_saldo:5.2f}
            - Número de Saques Realizados: {G_n_saques}
            - Horário: {horario}

            =====================================================""")
        else:
            print(f"""
            ================= Extrato Bancário ==================
                  
            STATUS: Solicitação de Extrato Realizada com Sucesso.
            - Saldo Atual: R${G_saldo:5.2f}
            - Número de Saques Realizados: {G_n_saques}
            - Horário: {horario}
            - Registro de Transações: """)
            extrato_lista = extrato.split('\n')    
            for i in range(len(extrato_lista)-1):
                print(f"""              [{i+1}] - {extrato_lista[i]}""")
            print(f"""              
            =====================================================""")
    else:
        print("Operação Inválida.")
    return

# Função de Mensagem de Alerta
def msg_alerta(*args):
    print(f"""
                    ===================== ATENÇÃO! ======================""")
    if args[0] == LIMITE_NUMERO_SAQUES:
        print(f"""
                    Você atingiu o seu limite de {LIMITE_NUMERO_SAQUES} saques diários.
                    Tente novamente amanhã.

                    =====================================================""")
    elif args[0] == LIMITE_VALOR_SAQUES:
        print(f"""
                    O valor do saque excede o seu limite de R$ {LIMITE_VALOR_SAQUES:5.2f}.
                    Tente novamente um valor menor que R$ {LIMITE_VALOR_SAQUES:5.2f}.

                    =====================================================""")
    elif args[0] <= 0.0:
        print(f"""
                    O valor do saque não é válido.
                    Digite valores positivos ou diferente de R$ 0.00.

                    =====================================================""")
    else:
        print(f"""
                    O valor do saque excede o seu saldo de R$ {G_saldo:5.2f}.
                    Tente novamente um valor menor que R$ {G_saldo:5.2f}.

                    =====================================================""")          
    return

#%% Desafio - Sistema de Banco

# Constantes
LIMITE_NUMERO_SAQUES = 3
LIMITE_VALOR_SAQUES = 500

# Variáveis
G_saldo, G_n_saques = 0, 0
input_saque, input_deposito = 0, 0
extrato, horario = "",""

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
            input_deposito_valido, input_deposito = transacao_valida(input_deposito)

        # Realização da Transação e Registro no Extrato
        G_saldo += input_deposito
        horario = hora_atual()
        extrato += f"[{horario}] Depósito: R$ {input_deposito:5.2f}\n"
        resumo_solicitacao(menu_opcao, input_deposito, G_saldo, horario)
        input_deposito_valido = False
        input_deposito = None
        
    # Operação de Saque
    elif menu_opcao == "S":
        # Verificação da Quantidade Limite de Saques Diários
        if G_n_saques < LIMITE_NUMERO_SAQUES:
            # Input de Saque e Validação
            while input_saque_valido == False:
                input_saque = input("Digite a quantia a ser depositada: ")
                input_saque_valido, input_saque = transacao_valida(input_saque)

            # Verificação do Limite de Valor de Saque            
            if input_saque <= LIMITE_VALOR_SAQUES and input_saque > 0:
                # Verificação do Saldo Disponível
                if input_saque <= G_saldo and input_saque > 0:
                    G_saldo -= input_saque
                    G_n_saques += 1
                    horario = hora_atual()
                    extrato += f"[{horario}] Saque: R$ {input_saque:5.2f}\n"
                    resumo_solicitacao(menu_opcao, input_saque, G_saldo, horario)
                    input_saque_valido = False
                    input_saque = None
                else: 
                    msg_alerta(G_saldo)
            else:
                if input_saque <= 0:

                else:
                    msg_alerta(LIMITE_VALOR_SAQUES)
        else:
            msg_alerta(LIMITE_NUMERO_SAQUES)

    # Operação de Extrato
    elif menu_opcao == "E":
        horario = hora_atual()
        resumo_solicitacao(menu_opcao, G_saldo, G_n_saques, horario, extrato)
        
    # Encerramento do Sistema
    elif menu_opcao == "Q":
        sys_on = False
        print("Sistema Encerrado.")
    
    # Opção Inválida
    else:
        print("Opção Inválida. Selecione uma opção válida.")
