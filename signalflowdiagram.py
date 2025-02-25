from collections import defaultdict

# Estruturas de dados para armazenar os ciclos encontrados
resp = set()
resp_certo = []

# Lista de adjacência para representar o grafo
adjlist = defaultdict(list)

# Lista para marcar os nós visitados
vis = [-1] * 100

# Lista para armazenar o caminho atual
path = []

def dfs(at):
    # Marca o nó como visitado
    vis[at] = 1
    # Adiciona o nó ao caminho atual
    path.append(at)

    # Visita os vizinhos do nó atual
    for to in adjlist[at]:
        if vis[to] == 1:
            # Achou um ciclo quando ia revisitar o nó "to"
            cycle = []

            # Reconstrói o ciclo a partir do caminho atual
            for i in range(len(path) - 1, -1, -1):
                cycle.append(path[i])
                if path[i] == to:
                    break

            # Ordena o ciclo para verificar se já foi encontrado
            ord_cycle = sorted(cycle)

            # Se o ciclo não foi encontrado antes, adiciona ao conjunto de respostas
            if tuple(ord_cycle) not in resp:
                resp.add(tuple(ord_cycle))
                resp_certo.append(cycle)
        else:
            # Se não achou ciclo, continua a busca
            dfs(to)

    # Limpa o nó atual: marca como não visitado e remove do caminho
    vis[at] = -1
    path.pop()

def main():
    # Define a lista de adjacência do grafo
    adjlist[0] = [1, 4]
    adjlist[1] = [2, 5]
    adjlist[2] = [3]
    adjlist[3] = [0, 1]
    adjlist[4] = [1]
    adjlist[5] = [6]
    adjlist[6] = [2, 7]
    adjlist[7] = [8]
    adjlist[8] = [6]

    # Inicia a busca em profundidade a partir do nó 0
    dfs(0)

    # Exibe os ciclos encontrados
    for cycle in resp_certo:
        print(" ".join(map(str, cycle)))

if __name__ == "__main__":
    main()
