def multiplos_de_m_mais_1(peças_restantes_no_jogo,m): # verificar multiplos de m +1 
        multiplos = []
        for x in range(m+1,(peças_restantes_no_jogo+1)):
            if (x % (m+1)) == 0:
                multiplos.append(x)
        
        return multiplos

def computador_escolhe_jogada(n, m, historico_peças):
    # Verificar se n é múltiplo de (m+1)
    if n % (m + 1) == 0:
        return m  # Computador pode retirar o máximo possível

    # Verificar se é possível deixar um múltiplo de (m+1) ao oponente
    for jogada in range(1, m + 1):
        if (n - jogada) % (m + 1) == 0 and jogada not in historico_peças:
            return jogada

    # Se não for possível deixar um múltiplo de (m+1), retirar o máximo permitido
    return m


def usuario_escolhe_jogada(n,m):
    peças_retiradas_usuario = int(input("Quantas peças você vai tirar? "))

    if peças_retiradas_usuario > m:
        while peças_retiradas_usuario > m:
            print("Oops! Jogada inválida! Tente de novo.")
            peças_retiradas_usuario = int(input("Quantas peças você vai tirar? "))

    return peças_retiradas_usuario

resultados = ["Fim do jogo! Você ganhou","Fim do jogo! O computador ganhou"]

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    c = 0
    peças_restantes_no_jogo = n

    if n in multiplos_de_m_mais_1(n,m): #usuario começa
        c = 0

        print("\nVocê começa!\n")

        peças_retiradas_usuario = usuario_escolhe_jogada(n,m)

        peças_restantes_no_jogo -= peças_retiradas_usuario

        print("Voce tirou",peças_retiradas_usuario,"peças.")
        print("Agora restam", peças_restantes_no_jogo ,"peças no tabuleiro.\n")        

    else: #computador começa
        c = 1

        print("\nComputador começa!\n")
        peças_retiradas_computador = computador_escolhe_jogada(n,m)

        peças_restantes_no_jogo -= peças_retiradas_computador

        print("O computador tirou",peças_retiradas_computador,"peças.")
        print("Agora restam", peças_restantes_no_jogo ,"peças no tabuleiro.\n")         

    while peças_restantes_no_jogo > 0:

        if c == 1: #usuario joga
            c = 0 # definir que o computador será o próximo a jogar
            peças_retiradas_usuario = usuario_escolhe_jogada(n,m)

            peças_restantes_no_jogo -= peças_retiradas_usuario

            print("Voce tirou",peças_retiradas_usuario,"peças")
            if peças_restantes_no_jogo == 0:
                return resultados[0]

        else: #computador joga
            c = 1 # definir que o computador NÃO será o PRÓXIMO a jogar
            peças_retiradas_computador = computador_escolhe_jogada(n,m)

            peças_restantes_no_jogo -= peças_retiradas_computador

            print("O computador tirou",peças_retiradas_computador,"peças.")
            if peças_restantes_no_jogo == 0:
                return resultados[1]

        if peças_restantes_no_jogo != 0:
            print("Agora restam", peças_restantes_no_jogo ,"peças no tabuleiro.\n")

        n = peças_restantes_no_jogo
    
def campeonato():
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
    print("\nVoce escolheu uma partida!\n")
    print(partida())
elif partida_ou_campeonato == 2:
    print("\nVoce escolheu um campeonato!")
    campeonato()

