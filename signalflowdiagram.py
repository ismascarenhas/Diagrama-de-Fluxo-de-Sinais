from collections import defaultdict

# Conjuntos para armazenar ciclos encontrados
resp = set()
respCerto = []

# Lista de adjacências para o grafo
adjlist = defaultdict(list)

# Variáveis auxiliares
pos = [-1] * 100
vis = [-1] * 100

# Lista temporária para armazenar o caminho atual
v = []

# Função recursiva para percorrer o grafo e encontrar ciclos
def f(at, cnt):
    v.append(at)
    pos[at] = cnt
    vis[at] = 1

    for to in adjlist[at]:
        if vis[to] != -1:  # Se o nó já foi visitado
            ciclo = []
            for i in range(pos[to], len(v)):
                ciclo.append(v[i])
            cicloOrdenado = sorted(ciclo)

            if tuple(cicloOrdenado) not in resp:
                resp.add(tuple(cicloOrdenado))
                respCerto.append(ciclo)
        else:
            f(to, cnt + 1)

    v.pop()  # Remove o último elemento após a recursão
    vis[at] = -1  # Marca o nó como não visitado

# Função principal
if __name__ == "__main__":
    # Definindo a lista de adjacências (exemplo dado)
    adjlist[0] = [1, 7]
    adjlist[1] = [2]
    adjlist[2] = [1, 3]
    adjlist[3] = [2, 4]
    adjlist[4] = []
    adjlist[5] = [4, 6]
    adjlist[6] = [5, 7]
    adjlist[7] = [6]
    # Chama a função para o nó inicial
    f(0, 0)
    #f(3, 0)
    # Imprime todos os ciclos encontrados
    for ciclo in respCerto:
        print(" ".join(map(str, ciclo)))
