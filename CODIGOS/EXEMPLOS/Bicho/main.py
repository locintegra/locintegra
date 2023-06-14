import csv
import os
import random

# Dicionário com as informações dos bichos
bichos = {
    'Grupo 01': {'Bicho': 'AVESTRUZ', 'Dezenas': '01, 02, 03, 04', 'Centenas': '001-904', 'Milhares': '0001-9904'},
    'Grupo 02': {'Bicho': 'ÁGUIA', 'Dezenas': '05, 06, 07, 08', 'Centenas': '005-908', 'Milhares': '0005-9908'},
    'Grupo 03': {'Bicho': 'BURRO', 'Dezenas': '09, 10, 11, 12', 'Centenas': '009-912', 'Milhares': '0009-9912'},
    'Grupo 04': {'Bicho': 'BORBOLETA', 'Dezenas': '13, 14, 15, 16', 'Centenas': '013-916', 'Milhares': '0013-9916'},
    'Grupo 05': {'Bicho': 'CACHORRO', 'Dezenas': '17, 18, 19, 20', 'Centenas': '017-920', 'Milhares': '0017-9920'},
    'Grupo 06': {'Bicho': 'CABRA', 'Dezenas': '21, 22, 23, 24', 'Centenas': '021-924', 'Milhares': '0021-9924'},
    'Grupo 07': {'Bicho': 'CARNEIRO', 'Dezenas': '25, 26, 27, 28', 'Centenas': '025-928', 'Milhares': '0025-9928'},
    'Grupo 08': {'Bicho': 'CAMELO', 'Dezenas': '29, 30, 31, 32', 'Centenas': '029-932', 'Milhares': '0029-9932'},
    'Grupo 09': {'Bicho': 'COBRA', 'Dezenas': '33, 34, 35, 36', 'Centenas': '033-936', 'Milhares': '0033-9936'},
    'Grupo 10': {'Bicho': 'COELHO', 'Dezenas': '37, 38, 39, 40', 'Centenas': '037-940', 'Milhares': '0037-9940'},
    'Grupo 11': {'Bicho': 'CAVALO', 'Dezenas': '41, 42, 43, 44', 'Centenas': '041-944', 'Milhares': '0041-9944'},
    'Grupo 12': {'Bicho': 'ELEFANTE', 'Dezenas': '45, 46, 47, 48', 'Centenas': '045-948', 'Milhares': '0045-9948'},
    'Grupo 13': {'Bicho': 'GALO', 'Dezenas': '49, 50, 51, 52', 'Centenas': '049-952', 'Milhares': '0049-9952'},
    'Grupo 14': {'Bicho': 'GATO', 'Dezenas': '53, 54, 55, 56', 'Centenas': '053-956', 'Milhares': '0053-9956'},
    'Grupo 15': {'Bicho': 'JACARÉ', 'Dezenas': '57, 58, 59, 60', 'Centenas': '057-960', 'Milhares': '0057-9960'},
    'Grupo 16': {'Bicho': 'LEÃO', 'Dezenas': '61, 62, 63, 64', 'Centenas': '061-964', 'Milhares': '0061-9964'},
    'Grupo 17': {'Bicho': 'MACACO', 'Dezenas': '65, 66, 67, 68', 'Centenas': '065-968', 'Milhares': '0065-9968'},
    'Grupo 18': {'Bicho': 'PORCO', 'Dezenas': '69, 70, 71, 72', 'Centenas': '069-972', 'Milhares': '0069-9972'},
    'Grupo 19': {'Bicho': 'PAVÃO', 'Dezenas': '73, 74, 75, 76', 'Centenas': '073-976', 'Milhares': '0073-9976'},
    'Grupo 20': {'Bicho': 'PERU', 'Dezenas': '77, 78, 79, 80', 'Centenas': '077-980', 'Milhares': '0077-9980'},
    'Grupo 21': {'Bicho': 'TOURO', 'Dezenas': '81, 82, 83, 84', 'Centenas': '081-984', 'Milhares': '0081-9984'},
    'Grupo 22': {'Bicho': 'TIGRE', 'Dezenas': '85, 86, 87, 88', 'Centenas': '085-988', 'Milhares': '0085-9988'},
    'Grupo 23': {'Bicho': 'URSO', 'Dezenas': '89, 90, 91, 92', 'Centenas': '089-992', 'Milhares': '0089-9992'},
    'Grupo 24': {'Bicho': 'VEADO', 'Dezenas': '93, 94, 95, 96', 'Centenas': '093-996', 'Milhares': '0093-9996'},
    'Grupo 25': {'Bicho': 'VACA', 'Dezenas': '97, 98, 99, 00', 'Centenas': '097-900', 'Milhares': '0097-9900'}
}


def gerar_dados_fake():
    dados = []
    for _ in range(50):
        data = '2023-01-10'  # Exemplo de data fixa
        tipo = random.choice(['PT', 'PTN', 'CRJ', 'FDL'])  # Tipo de jogo aleatório
        jogo = [random.randint(0, 9999) for _ in range(5)]  # Valores aleatórios para o jogo
        dados.append([data, tipo] + jogo)

    with open('dados_treinamento.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['data', 'tipo', '1p', '2p', '3p', '4p', '5p'])
        writer.writerows(dados)


def carregar_dados_treinamento():
    with open('dados_treinamento.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ignorar o cabeçalho
        dados = [row for row in reader]
    return header, dados


def salvar_dados_treinamento(header, dados):
    with open('dados_treinamento.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(dados)


def obter_palpite(data, tipo):
    header, dados = carregar_dados_treinamento()

    # Filtrar dados com base na data e tipo
    dados_filtrados = [row for row in dados if row[0] == data and row[1] == tipo]

    # Verificar a frequência de cada jogo
    frequencia_jogos = {}
    for row in dados_filtrados:
        jogo = tuple(row[2:])
        frequencia_jogos[jogo] = frequencia_jogos.get(jogo, 0) + 1

    # Ordenar os jogos por frequência (do maior para o menor)
    jogos_ordenados = sorted(frequencia_jogos, key=frequencia_jogos.get, reverse=True)

    if jogos_ordenados:
        # Escolher o jogo mais frequente como palpite
        palpite = list(jogos_ordenados[0])
        print("Palpite para o jogo do Bicho:")
        print(f"Tipo: {tipo}")
        print("Jogo:", ", ".join(str(num) for num in palpite))
    else:
        print("Não há dados suficientes para gerar um palpite.")


def verificar_resultado(data, tipo, resultado):
    header, dados = carregar_dados_treinamento()

    # Adicionar o resultado aos dados de treinamento
    dados.append([data, tipo] + resultado)
    salvar_dados_treinamento(header, dados)

    # Verificar se o último palpite foi igual ao resultado
    ultimo_palpite = dados[-2][2:]  # Último jogo antes do resultado
    if ultimo_palpite == resultado:
        print("A IA acertou o palpite!")
        # Dar recompensa à IA
    else:
        print("A IA errou o palpite!")
        # Dar punição à IA


# Exemplo de uso
if not os.path.isfile('dados_treinamento.csv'):
    gerar_dados_fake()

obter_palpite('2023-06-02', 'PT')

verificar_resultado('2023-06-02', 'PT', [1560, 8460, 1098, 7654, 2109])
