"""
Sistema de avaliação de membros de academia
"""

def checar_liberacao():
    print("\n=== VERIFICACAO DE LIBERACAO ===")
    pagamento = input("Pagamento em dia? (s/n): ").strip().lower()
    exame = input("Exame médico válido? (s/n): ").strip().lower()

    if pagamento == "s":
        print("Pagamento OK")
        if exame == "s":
            print("RESULTADO: LIBERADO - Pagamento e exame em dia")
        else:
            print("RESULTADO: BLOQUEADO - Pagamento OK, mas exame vencido")
    else:
        print("RESULTADO: BLOQUEADO - Pagamento pendente")


def definir_plano():
    print("\n=== CLASSIFICACAO DE PLANO ===")
    meses = int(input("Quantos meses o aluno contratou? "))

    if meses >= 12:
        tipo_plano = "ANUAL"
    elif meses >= 6:
        tipo_plano = "SEMESTRAL"
    elif meses >= 3:
        tipo_plano = "TRIMESTRAL"
    else:
        tipo_plano = "MENSAL"

    print(f"PLANO: {tipo_plano}")


def exibir_opcoes():
    print("\n=== PROCESSADOR DE MENU ===")
    print("1 - Listar alunos")
    print("2 - Cadastrar aluno")
    print("3 - Calcular mensalidade")
    print("4 - Sair")

    escolha = input("Digite a opcao desejada: ")

    match escolha:
        case "1":
            print("OPCAO 1: Listar alunos")
        case "2":
            print("OPCAO 2: Cadastrar aluno")
        case "3":
            print("OPCAO 3: Calcular mensalidade")
        case "4" | "sair":
            print("OPCAO 4: Sair do sistema")
        case _:
            print(f"OPCAO INVALIDA: {escolha}")


def avaliar_frequencia():
    print("\n=== AVALIACAO DO MEMBRO ===")
    nome_aluno = input("Nome do aluno: ")
    dias_treino = int(input("Quantos dias por semana treina: "))

    match dias_treino:
        case d if d >= 5:
            print(f"{nome_aluno}: MEMBRO DEDICADO - {d} dias por semana")
        case d if d >= 3:
            print(f"{nome_aluno}: MEMBRO REGULAR - {d} dias por semana")
        case d if d >= 1:
            print(f"{nome_aluno}: MEMBRO OCASIONAL - {d} dias por semana")
        case _:
            print(f"{nome_aluno}: SEM FREQUENCIA REGISTRADA")


def rodar_sistema():
    print("=" * 50)
    print("SISTEMA DE ACADEMIA")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Verificar Liberacao")
        print("2 - Classificar Plano")
        print("3 - Processar Menu")
        print("4 - Avaliar Membro")
        print("5 - Sair")

        escolha_menu = input("\nEscolha uma opcao (1-5): ")

        if escolha_menu == "1":
            checar_liberacao()
        elif escolha_menu == "2":
            definir_plano()
        elif escolha_menu == "3":
            exibir_opcoes()
        elif escolha_menu == "4":
            avaliar_frequencia()
        elif escolha_menu == "5":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    rodar_sistema()
