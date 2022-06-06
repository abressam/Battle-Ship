total_porta_navio = 3
total_cruzador = 4
total_fragata = 5
total_pontos = 0
acertou_porta_aviao = 0
acertou_cruzeiro = 0
acertou_fragata = 0

def quantidade_navio():
    print("\nEscolha abaixo, qual navio deseja posicionar, informando o número correspondente de cada embarcação.")
    print("Porta-aviões [0]\tCruzador[1]\t\tFragata[2]")
    print("\nTipo de Embarcação | Quantidade Restante")
    print("Porta-aviões", "      |", total_porta_navio)
    print("Cruzador", "          |", total_cruzador)
    print("Fragata", "           |", total_fragata)

def instrucoes_jogador_2():
    print("\nJogador 2, você deve encontrar as embarcações escondidas no tabuleiro!")
    print("São ao todo 12 embarcações, com tamanhos variados, podendo ser de 2, 3 ou 4 partes.\n")
    print("Exemplo: se atingir um espaço que releve o número 4, significa que é uma embarcação com 4 partes no total "
          + "e será necessário antingir mais 3 partes para naufragá-la")
    print("Se atingir um espaço que revele o número 1, significa que não há nenhuma parte de embarcação naquele local,"
          + "a célula ficará marcada com esse valor para não ser atingida novamente")
    print("Os espaços que apresentam o número 0 significam que ainda não foram atingidos.\n")

def jogador_1():
    tipo_navio = int(input("\nJogador 1 selecione a embarcação que deseja posicionar: "))
    verifica_embarcacao(tipo_navio)

    j1_linha = int(input("\nInforme a linha que deseja do tabuleiro: "))
    verifica_linha(j1_linha)

    j1_coluna = int(input("Informe a coluna que deseja do tabuleiro: "))
    verifica_coluna(j1_coluna)

    armazena_navio(tipo_navio, j1_linha, j1_coluna)

def jogador_2():
    j2_linha = int(input("\nInforme a linha que deseja do tabuleiro: "))
    verifica_linha(j2_linha)

    j2_coluna = int(input("Informe a coluna que deseja do tabuleiro: "))
    verifica_coluna(j2_coluna)

    dispara_projetil(j2_linha, j2_coluna)

def verifica_linha(linha):
    # Vefiricador se o número da linha digitada é válido
    while linha < 1 or linha > 20:
        print("\nA coordenada de linha escolhida está fora do limite do tabuleiro! Tente novamente")
        linha = int(input("Informe a linha que deseja do tabuleiro: "))

def verifica_coluna(coluna):
    # Vefiricador se o número da linha digitada é válido
    while coluna < 1 or coluna > 20:
        print("\nA coordenada de coluna escolhida está fora do limite do tabuleiro! Tente novamente")
        coluna = int(input("Informe a linha que deseja do tabuleiro: "))

def verifica_embarcacao(tipo_navio):
    while tipo_navio < 0 or tipo_navio > 2:
        print("\nNenhuma embarcação corresponde ao valor informado, tente novamente.")
        tipo_navio = int(input("Jogador 1 selecione a embarcação que deseja posicionar: "))

def armazena_navio(tipo_navio, j1_linha, j1_coluna):
    porta_aviao_partes = 4
    cruzeiro_partes = 3
    fragata_partes = 2

    global total_porta_navio
    global total_cruzador
    global total_fragata

    espaco_livre = 0

    if tipo_navio == 0 and total_porta_navio > 0:
        for linha in range(1):
            # Se houver espaço, o restante do navio é posicionado na direita
            if j1_coluna + (porta_aviao_partes - 1) < 21:
                for coluna in range(j1_coluna, j1_coluna + porta_aviao_partes):
                    if tabuleiro[j1_linha - 1][coluna - 1] == 0:
                        espaco_livre += 1

            else:
                print("--> Ops! Não há espaço suficiente, escolha outra posição.")
                jogador_1()

        if espaco_livre == 4:
            total_porta_navio -= 1
            print(total_porta_navio)
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!")
                for coluna in range(j1_coluna, j1_coluna + porta_aviao_partes):
                    tabuleiro[j1_linha - 1][coluna - 1] = 4
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.")
            jogador_1()

    elif tipo_navio == 1 and total_cruzador > 0:
        for linha in range(1):
            # Se houver espaço, o restante do navio é posicionado na direita
            if j1_coluna + (cruzeiro_partes - 1) < 21:
                for coluna in range(j1_coluna, j1_coluna + cruzeiro_partes):
                    if tabuleiro[j1_linha - 1][coluna - 1] == 0:
                        espaco_livre += 1

            else:
                print("--> Ops! Não há espaço suficiente, escolha outra posição.")
                jogador_1()

        if espaco_livre == 3:
            total_cruzador -= 1
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!")
                for coluna in range(j1_coluna, j1_coluna + cruzeiro_partes):
                    tabuleiro[j1_linha - 1][coluna - 1] = 3
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.")
            jogador_1()

    elif tipo_navio == 2 and total_fragata > 0:
        for linha in range(1):
            # Se houver espaço, o restante do navio é posicionado na direita
            if j1_coluna + (fragata_partes - 1) < 21:
                for coluna in range(j1_coluna, j1_coluna + fragata_partes):
                    if tabuleiro[j1_linha - 1][coluna - 1] == 0:
                        espaco_livre += 1

            else:
                print("--> Ops! Não há espaço suficiente, escolha outra posição.")
                jogador_1()

        if espaco_livre == 2:
            total_fragata -= 1
            for linha in range(1):
                print("\nSeu navio foi posicionado com sucesso!")
                for coluna in range(j1_coluna, j1_coluna + fragata_partes):
                    tabuleiro[j1_linha - 1][coluna - 1] = 2
        else:
            print("--> Ops! Não há espaço suficiente, escolha outra posição.")
            jogador_1()

    else:
        print("--> Não há mais embarcações desse tipo disponíveis, escolha outro navio para posicionar")
        jogador_1()


def pontuacao(partes_navio):

    pontos = 0
    global total_pontos

    if partes_navio == 4:
        pontos += 30
        total_pontos += pontos
        print("O jogador 2 naufragou um porta-aviões!")
        print("Pontuação:", total_pontos)

    elif partes_navio == 3:
        pontos += 20
        total_pontos += pontos
        print("O jogador 2 naufragou um cruzeiro!")
        print("Pontuação:", total_pontos)

    else:
        pontos += 10
        total_pontos += pontos
        print("O jogador 2 naufragou uma fragata!")
        print("Pontuação:", total_pontos)

def dispara_projetil(j2_linha, j2_coluna):

    global acertou_porta_aviao
    global acertou_cruzeiro
    global acertou_fragata

    if matriz_escondida[j2_linha - 1][j2_coluna - 1] == 0:
        if tabuleiro[j2_linha - 1][j2_coluna - 1] == 0:
            matriz_escondida[j2_linha - 1][j2_coluna - 1] = 1
            tabuleiro_escondido()
            print("O jogador 2 acertou a água!\nNenhum navio foi atingido.")

        elif tabuleiro[j2_linha - 1][j2_coluna - 1] == 2:
            matriz_escondida[j2_linha - 1][j2_coluna - 1] = 2
            acertou_fragata += 1
            tabuleiro_escondido()
            print("O jogador 2 acertou uma fragata!")

        elif tabuleiro[j2_linha - 1][j2_coluna - 1] == 3:
            matriz_escondida[j2_linha - 1][j2_coluna - 1] = 3
            acertou_cruzeiro += 1
            tabuleiro_escondido()
            print("O jogador 2 acertou um cruzeiro!")

        else:
            matriz_escondida[j2_linha - 1][j2_coluna - 1] = 4
            acertou_porta_aviao += 1
            tabuleiro_escondido()
            print("O jogador 2 acertou um porta-aviões!")

    else:
        print("\nEsse espaço já foi atingido, insira outra posição.")
        jogador_2()

    if acertou_porta_aviao == 4:
        pontuacao(acertou_porta_aviao)
        acertou_porta_aviao = 0

    elif acertou_cruzeiro == 3:
        pontuacao(acertou_cruzeiro)
        acertou_cruzeiro = 0

    elif acertou_fragata == 2:
        pontuacao(acertou_fragata)
        acertou_fragata = 0

# Criando o tabuleiro

numero_linhas = 20
num_colunas = 20

coordenadas = []

for numeros in range(0, 21):

    espacamento = 0
    if numeros == 0:
        espacamento = " " + str(numeros)
        coordenadas.append(espacamento)

    elif numeros > 0 and numeros < 10:
        espacamento = " " + str(numeros)
        coordenadas.append(espacamento)

    else:
        coordenadas.append(numeros)

# Criando a Matriz
tabuleiro = [0] * numero_linhas

for linhas in range(numero_linhas):
    tabuleiro[linhas] = [0] * num_colunas

# Cria matriz escondida
matriz_escondida = [0] * numero_linhas

for linhas in range(numero_linhas):
    matriz_escondida[linhas] = [0] * num_colunas

# Imprimindo a Matriz
def imprime_tabuleiro():
    print(*coordenadas)

    for linha in range(numero_linhas):
        if linha < 9:
            corrige_coluna = " " + str(linha + 1) + " " + str(tabuleiro[linha])
        else:
            corrige_coluna = str(linha + 1) + " " + str(tabuleiro[linha])
        print(corrige_coluna)
        for coluna in range(num_colunas):
            tabuleiro[linha][coluna]

def tabuleiro_escondido():
    print(*coordenadas)

    for linha in range(numero_linhas):
        if linha < 9:
            corrige_coluna = " " + str(linha + 1) + " " + str(matriz_escondida[linha])
        else:
            corrige_coluna = str(linha + 1) + " " + str(matriz_escondida[linha])
        print(corrige_coluna)
        for coluna in range(num_colunas):
            matriz_escondida[linha][coluna]

for num_embarcacoes in range(12):
    imprime_tabuleiro()
    quantidade_navio()
    jogador_1()

print("Posição de todas as embarcações")
imprime_tabuleiro()

iniciar_jogo = int(input("\nDeseja começar o jogo?\tNão [0]\tSim [1]: "))

if iniciar_jogo == 1:
    instrucoes_jogador_2()

    continuar_jogando = 1

    while continuar_jogando == 1 and total_pontos < 220:
        tabuleiro_escondido()
        jogador_2()
        continuar_jogando = int(input("\nDeseja jogar novamente?\tNão [0]\tSim [1]: "))
        print("")

    print("Jogador 2 atingiu todas as embarcações! Obrigada por jogar! :D")

else:
    print("O jogo foi encerrado.")
