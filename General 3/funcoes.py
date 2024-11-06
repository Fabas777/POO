import random
import time

def checar_frequencia(resultado:list):
    '''Cria um dicionario cujo armazenará os dados da lista Resultado no seguinte formato:
    Dado:2 (valor do dado, e quantas vezes ele aparece)'''
    frequencia = {}
    for dado in resultado:
        if dado in frequencia:
            frequencia[dado] += 1
        else:
            frequencia[dado] = 1
    return frequencia

def jogada(jogador:str, e_bot=False) -> int:
    '''Função onde se passa o jogo principal, com a criação da lista dos valores dos dados'''
    resultado = list()
    for jogadas in range(5):
        dado = random.randint(1, 6)
        resultado.append(dado)
    print(f"Jogador {jogador}:")
    printar_dados(resultado)

    substituir(resultado, jogador, e_bot)
    pontos = pontuacao(resultado, jogador)
    return pontos

def jogar_alternado(jogadores:str, num_rodadas:int) -> None:
    '''função que gerencia o jogo entre varios jogadores e alterna as rodadas'''
    pontuacao_total = {}
    for jogador in jogadores:
        pontuacao_total[jogador] = 0  # armazena a pontuação total de cada jogador
    rodada_atual = 1

    # for pra as rodadas ficarem alternadas tipo rodada 1 jogador 1 e rodada 1 jogador 2 ao inves de rodada 1 2 3 jogador 1 e rodada 1 2 3 jogador 2
    for rodada in range(num_rodadas):
        print(f"\n--- Rodada {rodada_atual} ---")
        rodada_atual += 1
        
        # for para alternar entre jogadores
        for jogador in jogadores:
            print(f"\nÉ a vez do jogador {jogador}")
            e_bot = jogador == "Bot"  # Verifica se e o bot se for true ai diz q o jogador é o bot na hora de exibir
            pontuacao_jogador = jogada(jogador, e_bot)  # realiza a jogada
            pontuacao_total[jogador] += pontuacao_jogador  # muda a pontuação

    # printa a pontuação de cada jogador
    print("\n--- Pontuação Final ---")
    for jogador, pontos in pontuacao_total.items():
        print(f"Jogador {jogador}: {pontos} pontos")
    rank(pontuacao_total)

def substituir(resultado:list,jogador:str, e_bot=False) -> None:
    '''Função onde acontece os "reroll" dos valores dos dados tanto do jogador quanto do bot'''  
    for repeticoes in range(3):
        if e_bot==False:
            substituto = str(input('Informe as posições (índices) dos dados que deseja mudar (separados por espaço), ou pressione Enter se não quiser mudar: '))
        else:
            frequencia = checar_frequencia(resultado)
            substituto = bot_escolhe_substituir(resultado, frequencia)
            if substituto == "":
                print("Bot não substitui nenhum dado.")
                return
            else:
                posbot=[]
                print(f"Bot substitui os dados nas posições: {substituto}")
                for i in substituto.split():
                    posbot.append(int(i))
                # posbot = [int(i) for i in substituto.split()]
                time.sleep(1)
        if substituto == '':
            return
        else:
            #posicao = [int(i)-1 for i in substituto.split(' ')]  
            posicao=[]
            for i in substituto.split(' '):
                posicao.append(int(i)-1)
        for x in posicao:
            resultado[x] = random.randint(1, 6)
        print(f"Jogador {jogador}:")
        printar_dados(resultado)

def bot_escolhe_substituir(resultado:list, frequencia:dict) -> str:
    '''Bot Checará as possibilidades de combinações e retornará as posições dos dados que seraão trocados'''
    #Parece ta meio desorganizado, mas essa ordem estranha é essencial para que o bot possa checar e tentar todas as combinações
    #Não existe um check de quadra pois não é nescessario, porque o bot ao tentar um general ele não tem nada a perder, ent um check de quadra é desnecessario 

    # Check General
    if check_general(frequencia):
        #o if retornará string vazia caso a função check_general retorne True, a string vazia serve como se o bot estivesse apertando enter para confirmar sua jogada
        return ""
    
    # Tentativa de General
    resultado_final = tentativa_general(resultado, frequencia)
    if resultado_final: #esse if serve pra saber se essa variavel "resultado_final" não está vazia, se estiver vazia o if dará errado, se estiver com alguma coisa o if continua
        return resultado_final

    # Check de Full house
    if check_full_house(frequencia):
        #o if retornará string vazia caso a função check_full_house retorne True, a string vazia serve como se o bot estivesse apertando enter para confirmar sua jogada
        return ""
    
    # Tentativa de Quadra
    resultado_final = tentativa_quadra(resultado, frequencia)
    if resultado_final: #Checar se a variavel nao está vazia, sem isso, caso estivesse vazia ela retornaria "None" e o código daria erro
        return resultado_final
    
    # Tentativa de Full House
    resultado_final = tentativa_com_par(resultado, frequencia)
    if resultado_final: #Checar se a variavel nao está vazia, sem isso, caso estivesse vazia ela retornaria "None" e o código daria erro
        return resultado_final

    # Check Sequência
    if check_sequencia(resultado):
        #o if retornará string vazia caso a função check_sequencia retorne True, a string vazia serve como se o bot estivesse apertando enter para confirmar sua jogada
        return ""
    
    # Tentativa de Sequência
    resultado_final = tentativa_sequencia(resultado)
    if resultado_final: #Checar se a variavel nao está vazia, sem isso, caso estivesse vazia ela retornaria "None" e o código daria erro
        return resultado_final


def check_general(frequencia:dict) -> bool:
    '''Checará no dicionario de frequencias se algum dado se repete 5 vezes, caso sim retornará True e vai validar o if de checagem'''
    valores = list(frequencia.values())
    return valores == [5]


def tentativa_general(resultado:list, frequencia:dict) -> str:
    '''A função tentará conseguir um general (5 dados iguais) caso previamente ja tenha 4 dados iguais'''
    for dado, contagem in frequencia.items():
        if contagem == 4: #Caso o if não seja executado a função retornará "None", oque não é um problema, porque outras funções retornarão algum valor, só seria problema caso tivesse alguma combinação que nao se encaixasse em nenhuma das outras funções
            resultadofiltrado = []
            for i in range(5):
                if resultado[i] != dado:
                    resultadofiltrado.append(str(i + 1))
            return " ".join(resultadofiltrado)


def check_full_house(frequencia:dict)-> bool:
    '''Checará se existe um full house através da seguinte forma
    Se os valores do dicionario de frequencias são um par e uma trinca ou seja se um numero se repete 2 vezes e o outro 3'''
    valores = list(frequencia.values())
    return sorted(valores) == [2, 3]


def tentativa_quadra(resultado:list, frequencia:dict)-> str:
    '''Tentará um quadra da seguinte forma
    Se houver um dado se repetindo 3 vezes, a função irá analisar os dados e salvará os indices dos 2 dados que nao se repetem'''
    for dado, contagem in frequencia.items():
        if contagem == 3:
            resultadofiltrado = []
            indices_encontrados = 0
            for i in range(5):
                if resultado[i] != dado:
                    resultadofiltrado.append(str(i + 1))
                    indices_encontrados += 1
                    if indices_encontrados == 2:
                        break
            return " ".join(resultadofiltrado)


def tentativa_com_par(resultado:list, frequencia:dict)-> str:
    '''a função checará a lista de dados e o dicionario de quantas vezes eles se repetem
    para buscar quantos pares de dados tem, se tiver apenas 1 ele mudará os outros 3 dados e se tiver 2 pares ele mudará o unico que é diferente'''
    par = 0
    dadosPares = []
    for dado, contagem in frequencia.items():
        if contagem == 2:
            par += 1
            dadosPares.append(dado)
            dadoE = dado
    
    if par == 1:
        resultadofiltrado = []
        indices_encontrados = 0
        for i in range(5):
            if resultado[i] != dadoE:
                resultadofiltrado.append(str(i + 1))
                indices_encontrados += 1
                if indices_encontrados == 3:
                    break
        return " ".join(resultadofiltrado)

    if par == 2:
        resultadofiltrado = []
        for i in range(5):
            if resultado[i] != dadosPares[0] and resultado[i] != dadosPares[1]:
                resultadofiltrado.append(str(i + 1))
        return " ".join(resultadofiltrado)

def check_sequencia(resultado:list)-> bool:
    '''Checa se os dados formam uma sequencia, ordenando a lista e vendo se encaixa em uma dessas'''
    resultado_ordenado = sorted(resultado)
    return resultado_ordenado == [2, 3, 4, 5, 6] or resultado_ordenado == [1, 2, 3, 4, 5]

def printar_dados(resultado:list)-> None:
    '''Receberá uma lista e printará a lista como se fosse varios dados'''
    dados_faces = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
        }
    # printa as 5 linhas de todos os dados lado a lado
           #("┌─────────┐",
           # "│  ●   ●  │",
           # "│  ●   ●  │",
           # "│  ●   ●  │",
           # "└─────────┘")
    for i in range(5):  # cada dado tem 5 linhas exemplo acima
        linha = ''
        for valor in resultado:
            linha += dados_faces[valor][i]# adiciona a uma borda vertical para ficar mais facil a visao em cada linha ai fica na forma (borda)+linha do dado+(borda2)
        print(linha)

def rank(pontuacao_total:dict)-> None:
    '''Função que criará um arquivo txt chamado ranking e adicionará e exibirá as pontuações dos jogadores'''
    # abre e fecha o arquivo pra garantir q ele ta ai
    open('ranking.txt', 'a').close()
    # Ler o conteúdo do arquivo
    arq = open('ranking.txt', 'r')
    linhas = arq.readlines()
    arq.close()
    # att o dicionário com o conteúdo do arquivo
    ranking = pontuacao_total.copy()
    for i in range(0, len(linhas), 2):
        jogador = linhas[i].strip()  # remove quebra de linha e espaços tipo \n
        pontuacao = int(linhas[i + 1].strip())  # Converter pontuação para inteiro (n sei se prescisa mas ta ai)
        ranking[jogador] = pontuacao  # adiciona um jogador novo ou atualiza um jogador ja no ranking
    # att o dicionário com as novas pontuações recebidas
    for jogador, pontuacao in pontuacao_total.items():
        ranking[jogador] = pontuacao
    # atualiza o codigo com a nova pontuação
    with open('ranking.txt', 'a') as arq:
        for jogador, pontuacao in pontuacao_total.items():
            arq.write(jogador + '\n')
            arq.write(str(pontuacao) + '\n')
    # Pinrta o ranking atualizado
    print("Ranking atualizado:")
    for jogador, pontuacao in ranking.items():
        print(f"{jogador}: {pontuacao} pontos")

def tentativa_sequencia(resultado:list)-> str:
    '''A função ordenará a lista e vai ver se encaixa em alguma dessas, se sim vai tentar trocar o indice que tem o 6'''
    resultado_ordenado = sorted(resultado)
    if resultado_ordenado in [[1, 2, 4, 5, 6], [1, 2, 3, 5, 6], [1, 2, 3, 4, 6], [1, 3, 4, 5, 6]]:
        resultadofiltrado = []
        for i in range(5):
            if resultado[i] == 6:
                resultadofiltrado.append(str(i + 1))
        return " ".join(resultadofiltrado) 

  
def verificar_quadra(frequencia:dict)-> bool:
    '''Retornará True caso tenha 4 nos valores do dicionario de frequencias'''
    return 4 in frequencia.values()

def verificar_sequencia(resultado:list)-> bool:
    '''Retornará True caso os valores do dicionario sejam únicos (5 dos 6 dados aparecem apenas 1 vez)'''
    resultado_ordenado = sorted(resultado)
    return resultado_ordenado == [1, 2, 3, 4, 5] or resultado_ordenado == [2, 3, 4, 5, 6]

def verificar_general(frequencia:dict)-> bool:
    '''Retornará True caso tenha 5 nos valores do dicionario de frequencias'''
    return 5 in frequencia.values()

def verificar_fullhouse(frequencia:dict)-> bool:
    '''Retornará True caso os valores do dicionario de frequencia tenham 2 e 3'''
    valor = list(frequencia.values())
    return valor == [2, 3] or valor == [3, 2]

#Funcão que faz a checagem de jogadas e soma com os pontos tanto do jogador quanto do bot que consiste de uma soma total + os pontos de cada alternativa
def pontuacao(resultado:list, jogador:str)-> int:
    ''' Função que faz a verificação das possibilidades
    E em seguida soma todos os valores dos dados + o valor da combinação'''
    # os ifs serão executados se for true
    frequencia = checar_frequencia(resultado)
    
    if verificar_fullhouse(frequencia):
        somadosdados = sum(resultado)
        pontos = somadosdados + 20
        print(f"Jogador {jogador} obteve um FULLHOUSE! Parabéns, seus pontos são: {pontos}")
        
    elif verificar_quadra(frequencia):
        somadosdados = sum(resultado)
        pontos = somadosdados + 40
        print(f"Jogador {jogador} obteve uma QUADRA! Seus pontos são: {pontos}")
        
    elif verificar_general(frequencia):
        somadosdados = sum(resultado)
        pontos = somadosdados + 50
        print(f"Jogador {jogador} obteve um GENERAL! Seus pontos são: {pontos}")
        
    elif verificar_sequencia(resultado):
        somadosdados = sum(resultado)
        pontos = somadosdados + 30
        print(f"Jogador {jogador} obteve uma SEQUÊNCIA! Seus pontos são: {pontos}")
        
    else:
        somadosdados = sum(resultado)
        pontos = somadosdados
        print(f"Jogador {jogador} não obteve nada ;( sua pontuação foi {pontos}")

    return pontos