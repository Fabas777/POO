import random
import time
from funcoes import (checar_frequencia, bot_escolhe_substituir, verificar_quadra, verificar_sequencia, verificar_general, verificar_fullhouse, pontuacao, jogada, printar_dados,jogar_alternado, rank)

if __name__ == '__main__':
    modo_jogo = input("Digite '1' para jogar contra outro jogador ou '2' para jogar contra o bot ou '3' para ver o Placar: ")
        
    while True:
        try:
            quantrodadas = int(input('Digite o número de rodadas de uma partida (máx 9): '))
        except ValueError:
            print("Digite um número inteiro")
            continue
        if quantrodadas > 9:
            raise Exception("Número inválido de rodadas")
        else:
            break
    
    print(f"Rodadas: {quantrodadas}")
    total_pontos = {}

    # Modo multiplayer
    if modo_jogo == '1':
        while True:
            try:    
                quantjogadores = int(input('Digite o número de jogadores de uma partida (máx 4): '))
            except ValueError:
                print("Digite um número inteiro")
                continue
            if quantjogadores > 4:
                raise Exception("Número inválido de jogadores")
            else:
                break

        jogadores = []
        for jogador in range(quantjogadores):
            nome = str(input(f"Insira o nome do jogador {jogador + 1}: "))
            jogadores.append(nome)
        
        # Inicia o jogo com alternância de rodadas
        jogar_alternado(jogadores, num_rodadas=quantrodadas)
    if modo_jogo == '3':
        print("n sei ainda acho que tem q fazer outra função")
    # Modo contra o Bot    
    else:
        nome = str(input("Insira seu nome: "))
        jogadores = [nome, "Bot"]

        # Inicia o jogo com alternância de rodadas (contra o bot)
        jogar_alternado(jogadores, num_rodadas=quantrodadas)

    print("\n--- Fim do Jogo ---")
