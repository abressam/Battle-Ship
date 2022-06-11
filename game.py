# Informa ao jogador as regras do jogo
def instrucoes_iniciais():
    print("\nBem-vindo (a) ao jogo Batalha Naval!")
    print("\n--> Instruções")
    print("""São necessários 2 jogadores para jogar, o jogador 1 é responsável por posicionar todas as embarcações
e o jogador 2 deve naufragar cada um desses navios escondidos no tabuleiro. Ao todo, são 12 embarcações com 3 tama-
nhos diferentes: o porta-aviões, o cruzador e a fragata, possuindo respectivamente 4, 3 e 2 partes. 
Portanto, o jogador 2 deve acertar todas as partes de uma embarcação para naufragá-la e obter a pontuação 
correspondente, sendo 30 pontos para o porta-aviões, 20 pontos para o cruzador e 10 pontos para a fragata.
    """)
    iniciar = verifica_escolha()  # Confere se o jogador deseja continuar

    return iniciar


# Informa ao Jogador 2 os símbolos do tabuleiro
def legenda_jogador_2():
    print("[*] - Representa uma coordenada não atingida")
    print("[~] - Representa uma coordenada atingida, mas que não possui nenhuma parte de embarcação")
    print("[X] - Representa que uma parte de uma foi embarcação atingida\n")


# Informa ao Jogador 1 a quantidade restante de cada navio
def legenda_jogador_1():
    global total_porta_avioes
    global total_cruzador
    global total_fragata

    print("Escolha abaixo, qual navio deseja posicionar, informando o número correspondente de cada embarcação.")
    print("Porta-aviões [1]\tCruzador[2]\t\tFragata[3]")
    print("\nTipo de Embarcação | Quantidade Restante")
    print("Porta-aviões", "      |", total_porta_avioes)
    print("Cruzador", "          |", total_cruzador)
    print("Fragata", "           |", total_fragata)


# Valida se o valor do navio inserido pelo usuário é válido e retorna o valor
def valida_navio():
    navio = int(input("\nInforme a embarcação que deseja posicionar: "))

    # Caso o valor do navio não seja válido, deve inserir novamente
    while navio < 1 or navio > 3:
        print("-> O tipo de navio informado é inválido, tente novamente.")
        navio = int(input("\nInforme a embarcação que deseja posicionar: "))

    return navio


# Valida se o valor da linha inserido pelo usuário é válido
def informe_linha(letras):
    linha = input("Informe a linha (A até T): ").upper()  # método upper() retorna sempre o valor inserido maiúsculo

    # Caso o valor da linha não seja válido, deve inserir novamente
    # O valor inserido é convertido ao seu número correspondente na tabela ASCII usando o método ord()
    while ord(linha) < 65 or ord(linha) > 84:
        print("-> O valor de linha escolhido é inválido, tente novamente.")
        linha = input("Informe a linha (A até T): ").upper()

    coordenada = letras.index(linha)

    return coordenada  # Retorna o index do valor correspondente na lista


# Valida se o valor da coluna inserido pelo usuário é válido e retorna o valor
def informe_coluna():
    coordenada_coluna = int(input("Informe a coluna (1 até 20): "))

    # Caso o valor da coluna não seja válido, deve inserir novamente
    while coordenada_coluna < 1 or coordenada_coluna > 20:
        print("-> O valor de coluna inserido é inválido, tente novamente.")
        coordenada_coluna = int(input("Informe a coluna (1 até 20): "))

    return coordenada_coluna


# Valida se o valor da escolha inserido pelo usuário é válido e retorna o valor
def verifica_escolha():
    escolha = int(input("\nDeseja continuar? Não [0] Sim [1]: "))

    # Caso o valor da escolha não seja válido, deve inserir novamente
    while escolha < 0 or escolha > 1:
        print("Valor inválido, tente novamente.")
        escolha = int(input("\nDeseja continuar? Não [0] Sim [1]: "))

    return escolha


# Funcionalidades do Jogador 1
def jogador_1():
    legenda_jogador_1()
    valor_navio = valida_navio()  # Obtêm o navio escolhido

    primeiro_jogador_linha = informe_linha(lista_letras)  # Obtêm a linha escolhida
    primeiro_jogador_coluna = informe_coluna()  # Obtêm a coluna escolhida

    # Posiciona um determinado navio na coordenada especificada pelo Jogador 1
    navio_posicionado = armazena_navio(valor_navio, primeiro_jogador_linha, primeiro_jogador_coluna,
                                       tabuleiro_jogador_1)
    # Atualiza o tabuleiro do Jogador 1
    imprime_tabuleiro(navio_posicionado, lista_letras)


# Funcionalidades do Jogador 2
def jogador_2():
    legenda_jogador_2()

    segundo_jogador_linha = informe_linha(lista_letras)  # Obtêm a linha escolhida
    segundo_jogador_coluna = informe_coluna()  # Obtêm a coluna escolhida

    # Modifica a posição atingida pelo Jogador 2
    posicao_atacada = dispara_projetil(tabuleiro_jogador_1, tabuleiro_jogador_2, segundo_jogador_linha,
                                       segundo_jogador_coluna)
    # Atualiza o tabuleiro do Jogador 2
    imprime_tabuleiro(posicao_atacada, lista_letras)


# A posição escolhida pelo Jogador 2 no tabuleiro é modificada, e essa modificação será retornada
def dispara_projetil(tabuleiro, tabuleiro_escondido, linha, coluna):
    global acertou_porta_avioes
    global acertou_cruzador
    global acertou_fragata

    # Caso o Jogador 2 não tenha atingido a posição escolhida
    if tabuleiro_escondido[linha][coluna - 1] == '*':

        # Ao atingir tal posição no tabuleiro do Jogador 1 e encontrar o valor '*'
        if tabuleiro[linha][coluna - 1] == '*':
            # No tabuleiro do Jogador 2, a mesma posição será modificada para o valor '~'
            tabuleiro_escondido[linha][coluna - 1] = '~'
            print("\nO jogador 2 acertou a água!\nNenhum navio foi atingido.\n")
            return tabuleiro_escondido

        # Ao atingir tal posição no tabuleiro do Jogador 1 e encontrar o valor '2'
        elif tabuleiro[linha][coluna - 1] == '2':
            # No tabuleiro do Jogador 2, a mesma posição será modificada para o valor 'X'
            tabuleiro_escondido[linha][coluna - 1] = 'X'
            acertou_fragata += 1  # Foi acertado uma parte de uma fragata
            print("\nO jogador 2 acertou um navio!\n")

            if acertou_fragata == 2:  # Se todas as partes de uma fragata forem acertadas
                pontuacao(acertou_fragata)  # Informa a pontuação obtida por naufragar a fragada
                acertou_fragata = 0  # Zera a variável para utilizar novamente

            return tabuleiro_escondido

        # Ao atingir tal posição no tabuleiro do Jogador 1 e encontrar o valor '3'
        elif tabuleiro[linha][coluna - 1] == '3':
            # No tabuleiro do Jogador 2, a mesma posição será modificada para o valor 'X'
            tabuleiro_escondido[linha][coluna - 1] = 'X'
            acertou_cruzador += 1  # Foi acertado uma parte de um cruzador

            if acertou_cruzador == 3:  # Se todas as partes de um cruzador forem acertadas
                pontuacao(acertou_cruzador)  # Informa a pontuação obtida por naufragar o cruzador
                acertou_cruzador = 0  # Zera a variável para utilizar novamente

            print("\nO jogador 2 acertou um navio!\n")
            return tabuleiro_escondido

        # Ao atingir tal posição no tabuleiro do Jogador 1 e encontrar o valor '4'
        elif tabuleiro[linha][coluna - 1] == '4':
            # No tabuleiro do Jogador 2, a mesma posição será modificada para o valor 'X'
            tabuleiro_escondido[linha][coluna - 1] = 'X'
            acertou_porta_avioes += 1  # Foi acertado uma parte de um porta-aviões

            if acertou_porta_avioes == 4:  # Se todas as partes de um porta-aviões forem acertadas
                pontuacao(acertou_porta_avioes)  # Informa a pontuação obtida por naufragar o porta-aviões
                acertou_porta_avioes = 0  # Zera a variável para utilizar novamente

            print("\nO jogador 2 acertou um navio!\n")
            return tabuleiro_escondido

    # Caso o Jogador 2 já tenha atingido essa posição, o tabuleiro retorna sem modificação
    else:
        print("\n--> Essa coordenada já foi atingida! Escolha outra posição.\n")
        return tabuleiro_escondido


# Imprime a pontuação obtida pelos naufrágios
def pontuacao(partes_navio):
    pontos = 0
    global total_pontos

    if partes_navio == 4:  # Porta-aviões
        pontos += 30
        total_pontos += pontos
        print("O jogador 2 naufragou um porta-aviões!")
        print("Pontuação:", total_pontos, "\n")

    elif partes_navio == 3:  # Cruzador
        pontos += 20
        total_pontos += pontos
        print("O jogador 2 naufragou um cruzeiro!")
        print("Pontuação:", total_pontos, "\n")

    else:  # Fragata
        pontos += 10
        total_pontos += pontos
        print("O jogador 2 naufragou uma fragata!")
        print("Pontuação:", total_pontos, "\n")


# Os navios são posicionados no tabuleiro do Jogador 1
def armazena_navio(tipo_navio, linha_escolhida, coluna_escolhida, tabuleiro):
    # Número de partes de cada embarcação
    porta_aviao_partes = 4
    cruzador_partes = 3
    fragata_partes = 2

    global total_porta_avioes
    global total_cruzador
    global total_fragata
    global numero_navios

    espaco_livre = 0

    # Se o porta-aviões foi escolhido e há porta-aviões disponíveis para posicionar
    if tipo_navio == 1 and total_porta_avioes > 0:
        for linha in range(1):
            # Se houver espaço, o porta-avião será posicionado para a direita
            if coluna_escolhida + (porta_aviao_partes - 1) < 21:
                for coluna in range(coluna_escolhida, coluna_escolhida + porta_aviao_partes):
                    # Se nas posições escolhidas para armazenar o navio, apresentar o símbolo '*'
                    if tabuleiro[linha_escolhida][coluna - 1] == '*':
                        espaco_livre += 1  # Aumenta a variável espaço livre

        # Se houver 4 espaços livres o porta-aviões é posicionado no local
        if espaco_livre == 4:
            total_porta_avioes -= 1  # Diminui em 1 o total de porta-aviões disponíveis
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!\n")
                for coluna in range(coluna_escolhida, coluna_escolhida + porta_aviao_partes):
                    tabuleiro[linha_escolhida][coluna - 1] = '4'  # As posições serão substituidas pelo valor '4'
            numero_navios -= 1  # O número total de navios para posicionar diminui em 1
            return tabuleiro

        # Caso não haja espaços livres suficientes para o porta-aviões, o tabuleiro retorna sem modificação
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.\n")
            return tabuleiro

    # Se o cruzador foi escolhido e há cruzadores disponíveis para posicionar
    elif tipo_navio == 2 and total_cruzador > 0:
        for linha in range(1):
            # Se houver espaço, o cruzador será posicionado para a direita
            if coluna_escolhida + (cruzador_partes - 1) < 21:
                for coluna in range(coluna_escolhida, coluna_escolhida + cruzador_partes):
                    if tabuleiro[linha_escolhida][coluna - 1] == '*':
                        espaco_livre += 1

        # Se houver 3 espaços livres o cruzador é posicionado no local
        if espaco_livre == 3:
            total_cruzador -= 1  # Diminui em 1 o total de cruzadores disponíveis
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!\n")
                for coluna in range(coluna_escolhida, coluna_escolhida + cruzador_partes):
                    tabuleiro[linha_escolhida][coluna - 1] = '3'  # As posições serão substituidas pelo valor '3'
            numero_navios -= 1  # O número total de navios para posicionar diminui em 1

            return tabuleiro

        # Caso não haja espaços livres suficientes para o cruzador, o tabuleiro retorna sem modificação
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.\n")
            return tabuleiro

    # Se a fragata foi escolhida e há fragatas disponíveis para posicionar
    elif tipo_navio == 3 and total_fragata > 0:
        for linha in range(1):
            # Se houver espaço, a fragata será posicionado para a direita
            if coluna_escolhida + (fragata_partes - 1) < 21:
                for coluna in range(coluna_escolhida, coluna_escolhida + fragata_partes):
                    if tabuleiro[linha_escolhida][coluna - 1] == '*':
                        espaco_livre += 1

        # Se houver 2 espaços livres a fragata é posicionado no local
        if espaco_livre == 2:
            total_fragata -= 1  # Diminui em 1 o total de fragatas disponíveis
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!\n")
                for coluna in range(coluna_escolhida, coluna_escolhida + fragata_partes):
                    tabuleiro[linha_escolhida][coluna - 1] = '2'  # As posições serão substituidas pelo valor '2'
            numero_navios -= 1  # O número total de navios para posicionar diminui em 1

            return tabuleiro

        # Caso não haja espaços livres suficientes para a fragata, o tabuleiro retorna sem modificação
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.\n")
            return tabuleiro

    # Caso o jogador já tenha posicionado todos os navios de um determinado tipo
    else:
        print("--> Não há mais embarcações desse tipo disponíveis, escolha outro navio para posicionar\n")
        return tabuleiro


# Cria a lista da coordenada de letras
def coordenada_letras():
    coordenada = []

    # Pega o valor correspondente das letras na tabela ASCII e converte para char
    for letra in range(65, 85):
        coordenada.append(chr(letra))  # Armazena na lista

    return coordenada


# Imprime o tabuleiro na tela
def imprime_tabuleiro(tabuleiro, letras):
    coordenada_numeros = []

    # Adiciona os espaçamentos necessários para que a coordenada dos números centralize com a coluna do tabuleiro
    for numeros in range(1, 21):
        if numeros < 2:
            espacamento = "    " + str(numeros) + "   "
        elif numeros >= 2 and numeros < 10:
            espacamento = str(numeros) + "   "
        else:
            espacamento = str(numeros) + "  "
        coordenada_numeros.append(espacamento)

    # Imprime as coordenadas numéricas antes do tabuleiro
    print(*coordenada_numeros)

    for linha in range(20):
        # Adiciona as coordenadas de letras em cada linha do tabuleiro
        primeira_coluna = str(letras[linha]) + " " + str(tabuleiro[linha]) + " " + str(
            letras[linha])
        print(primeira_coluna)

    # Imprime as coordenadas numéricas após o tabuleiro
    print(*coordenada_numeros)


# Cria a matriz do tabuleiro
def cria_tabuleiro():
    numero_linhas = 20
    numero_colunas = 20

    tabuleiro = ['*'] * numero_linhas

    for linhas in range(numero_linhas):
        tabuleiro[linhas] = ['*'] * numero_colunas

    return tabuleiro


# Variáveis Globais
total_porta_avioes = 3
total_cruzador = 4
total_fragata = 5

acertou_porta_avioes = 0
acertou_cruzador = 0
acertou_fragata = 0

total_pontos = 0

numero_navios = total_porta_avioes + total_cruzador + total_fragata
lista_letras = coordenada_letras()

# Inicia o jogo
comecar_jogo = instrucoes_iniciais()

# Se o usuário digitar 1, inicia o turno do jogador 1
if comecar_jogo == 1:

    tabuleiro_jogador_1 = cria_tabuleiro()  # Tabuleiro do Jogador 1
    imprime_tabuleiro(tabuleiro_jogador_1, lista_letras)  # Imprime tabuleiro do Jogador 1

    # Enquanto todos os navios não forem posicionados corretamente, o jogador 1 continuará jogando
    while numero_navios > 0:
        print("\nJogador 1, posicione as embarcações.\n")
        jogador_1()

    print("\nJogador 1 finalizou a sua vez\n")
    print("--> As embarcações serão escondidas e iniciará a vez do Jogador 2")

    inicia_jogador_2 = verifica_escolha()

    # Inicia o turno do Jogador 2 se o usuário digitar 1
    if inicia_jogador_2 == 1:

        tabuleiro_jogador_2 = cria_tabuleiro()  # Tabuleiro do Jogador 2
        imprime_tabuleiro(tabuleiro_jogador_2, lista_letras)  # Imprime tabuleiro do Jogador 2

        while inicia_jogador_2 == 1:
            print("\nJogador 2, escolha uma posição para disparar o projétil.\n")
            jogador_2()

            if total_pontos < 220:
                inicia_jogador_2 = verifica_escolha()

            else:
                print("Pontuação:", total_pontos, "\n")
                print("\n--> Jogador 2 atingiu todas as embarcações! Obrigada por jogar! :D")

        print("\nO jogo foi encerrado.")

    else:
        print("\nO jogo foi encerrado.")

# Finaliza o jogo quando o usuário digita 0
else:
    print("\nO jogo foi encerrado.")
