def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        # Verifica se a jogada atual de remoção do computador deixa um múltiplo de (m+1) para o adversário
        if (n - computadorRemove) % (m + 1) == 0:
            return computadorRemove
        else:
            computadorRemove += 1

    return computadorRemove

def usuario_escolhe_jogada(n, m):
    # Função para a escolha de jogada pelo usuário
    peças_retiradas_usuario = int(input("Quantas peças você vai tirar? "))

    # Verifica se a jogada do usuário é válida
    if peças_retiradas_usuario > m or peças_retiradas_usuario < 1:
        while peças_retiradas_usuario > m or peças_retiradas_usuario > n or peças_retiradas_usuario <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
            peças_retiradas_usuario = int(input("Quantas peças você vai tirar? "))

    return peças_retiradas_usuario

resultados = ["Fim do jogo! Você ganhou", "Fim do jogo! O computador ganhou"]

def partida():
    # Função para jogar uma partida isolada
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Verifica se o limite de peças por jogada é maior ou igual ao total de peças
    if m >= n:
        print("Oops! Jogada inválida! O limite de peças por jogada deve ser menor que o total de peças.")
        return

    c = 0  # Indica se o computador joga ou não

    if n % (m + 1) == 0:  # Usuário começa
        c = 1  # Computador é o próximo a jogar

        print("\nVocê começa!\n")

        peças_retiradas_usuario = usuario_escolhe_jogada(n, m)

        n -= peças_retiradas_usuario

        if peças_retiradas_usuario == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou", peças_retiradas_usuario, "peças.")

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam", n, "peças no tabuleiro.\n")

    else:  # Computador começa
        c = 0  # Usuário é o próximo a jogar

        print("\nComputador começa!\n")
        peças_retiradas_computador = computador_escolhe_jogada(n, m)

        n -= peças_retiradas_computador

        if peças_retiradas_computador == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", peças_retiradas_computador, "peças.")
        print("Agora restam", n, "peças no tabuleiro.\n")

    while n > 0:

        if c == 0:  # Usuário joga
            c = 1  # Indica que o computador será o próximo a jogar
            peças_retiradas_usuario = usuario_escolhe_jogada(n, m)

            n -= peças_retiradas_usuario
            if peças_retiradas_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", peças_retiradas_usuario, "peças.")

            if n == 0:
                return resultados[0]

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n != 0:
                print("Agora restam", n, "peças no tabuleiro.\n")

        else:  # Computador joga
            c = 0  # Indica que o computador NÃO será o próximo a jogar
            peças_retiradas_computador = computador_escolhe_jogada(n, m)

            n -= peças_retiradas_computador
            if peças_retiradas_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", peças_retiradas_computador, "peças.")

            if n == 0:
                return resultados[1]

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n != 0:
                print("Agora restam", n, "peças no tabuleiro\n")


def campeonato():
    # Função para jogar um campeonato
    pontos_usuario = 0
    pontos_computador = 0

    print("\n*** Rodada 1 ***\n")
    resultado_partida_1 = partida()
    if resultado_partida_1 == resultados[1]:
        pontos_computador += 1
    else:
        pontos_usuario += 1
    print(resultado_partida_1)

    print("\n*** Rodada 2 ***\n")
    resultado_partida_2 = partida()
    if resultado_partida_2 == resultados[1]:
        pontos_computador += 1
    else:
        pontos_usuario += 1
    print(resultado_partida_2)

    print("\n*** Rodada 3 ***\n")
    resultado_partida_3 = partida()
    if resultado_partida_3 == resultados[1]:
        pontos_computador += 1
    else:
        pontos_usuario += 1
    print(resultado_partida_3)

    print("\n**** Final do campeonato! ****")
    return print(f"\nPlacar: Você {pontos_usuario} X {pontos_computador} Computador")

partida_ou_campeonato = int(input("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if partida_ou_campeonato == 1:
    print("\nVocê escolheu uma partida!\n")
    print(partida())
elif partida_ou_campeonato == 2:
    print("\nVocê escolheu um campeonato!")
    campeonato()
