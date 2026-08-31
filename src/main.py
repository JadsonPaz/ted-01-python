import csv


# 1) LER O ARQUIVO CSV

# Cada chamado vira uma tupla: (protocolo, cliente, categoria,
# atendente, prioridade, status, tempo_min)

def ler_arquivo():
    lista_chamados = []
    arquivo = open("dados/chamados.csv", newline="", encoding="utf-8")
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        chamado = (
            linha["protocolo"],
            linha["cliente"],
            linha["categoria"],
            linha["atendente"],
            linha["prioridade"],
            linha["status"],
            int(linha["tempo_min"])
        )
        lista_chamados.append(chamado)

    arquivo.close()
    return lista_chamados



# 2) REMOVER CHAMADOS DUPLICADOS (mesmo protocolo)


def remover_duplicados(lista_chamados):
    protocolos_vistos = set()
    lista_sem_duplicados = []

    for chamado in lista_chamados:
        protocolo = chamado[0]
        if protocolo not in protocolos_vistos:
            protocolos_vistos.add(protocolo)
            lista_sem_duplicados.append(chamado)

    return lista_sem_duplicados


# 3) CATEGORIAS MAIS FREQUENTES


def contar_categorias(lista_chamados):
    # List comprehension: pega só a categoria de cada chamado
    categorias = [chamado[2] for chamado in lista_chamados]

    # Dict comprehension: conta quantas vezes cada categoria aparece
    contagem = {categoria: categorias.count(categoria) for categoria in set(categorias)}

    return contagem



# 4) DESEMPENHO DOS ATENDENTES (volume e tempo médio)


def desempenho_atendentes(lista_chamados):
    tempos_por_atendente = {}

    for chamado in lista_chamados:
        atendente = chamado[3]
        tempo = chamado[6]

        if atendente not in tempos_por_atendente:
            tempos_por_atendente[atendente] = []

        tempos_por_atendente[atendente].append(tempo)

    resultado = {}
    for atendente in tempos_por_atendente:
        tempos = tempos_por_atendente[atendente]
        volume = len(tempos)
        media = sum(tempos) / volume
        resultado[atendente] = [volume, round(media, 1)]

    return resultado



# 5) CLIENTES EM COMUM ENTRE DUAS CATEGORIAS (usando set)


def clientes_da_categoria(lista_chamados, categoria):
    # List comprehension: pega os clientes de uma categoria específica
    clientes = [chamado[1] for chamado in lista_chamados if chamado[2] == categoria]
    return set(clientes)


# PROGRAMA PRINCIPAL


chamados_brutos = ler_arquivo()
chamados = remover_duplicados(chamados_brutos)

print("=" * 50)
print("RESUMO GERAL")
print("=" * 50)
print("Total de chamados lidos:", len(chamados_brutos))
print("Total sem duplicados:", len(chamados))

print()
print("=" * 50)
print("1) CATEGORIAS MAIS FREQUENTES")
print("=" * 50)
categorias_contadas = contar_categorias(chamados)
for categoria, total in categorias_contadas.items():
    print(categoria, "->", total, "chamados")

print()
print("=" * 50)
print("2) DESEMPENHO DOS ATENDENTES")
print("=" * 50)
desempenho = desempenho_atendentes(chamados)
for atendente, dados in desempenho.items():
    volume = dados[0]
    tempo_medio = dados[1]
    print(atendente, "-> volume:", volume, "| tempo médio:", tempo_medio, "min")

print()
print("=" * 50)
print("3) CLIENTES EM COMUM ENTRE DUAS CATEGORIAS")
print("=" * 50)
categoria_a = "Técnico"
categoria_b = "Financeiro"

clientes_a = clientes_da_categoria(chamados, categoria_a)
clientes_b = clientes_da_categoria(chamados, categoria_b)

em_comum = clientes_a & clientes_b      # interseção
somente_a = clientes_a - clientes_b     # diferença
somente_b = clientes_b - clientes_a     # diferença
todos_juntos = clientes_a | clientes_b  # união

print("Categorias comparadas:", categoria_a, "e", categoria_b)
print("Clientes em comum:", em_comum)
print("Só em", categoria_a, ":", len(somente_a), "clientes")
print("Só em", categoria_b, ":", len(somente_b), "clientes")
print("Total de clientes envolvidos (união):", len(todos_juntos))

