class TGrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, linha, coluna):
        self.grafo[linha - 1][coluna - 1] = 1

    def mostra_matriz(self):
        print("A matriz de adjacência é: ")
        for i in range(self.vertices):
            print(self.grafo[i])

    def inDegree(self, v):
        grau = 0
        for i in range(self.vertices):
            if len(self.grafo[i]) < v:
                return None
            grau += self.grafo[i][v - 1]
        return grau

    def outDegree(self, v):
        grau = 0
        if len(self.grafo) < v:
            return None
        for i in range(self.vertices):
            grau += self.grafo[v - 1][i]
        return grau

    def ehFonte(self, v):
        if v is not None:
            try:
                if (self.outDegree(v) > 0) and (self.inDegree(v) == 0):
                    return 1
            except TypeError as ex:
                return 0
        return None

    def sorvedouro(self, v):
        if v is not None:
            try:
                if (self.inDegree(v) > 0) and (self.outDegree(v) == 0):
                    return 1
            except TypeError as ex:
                return 0
        return None

    def leGraphFile(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            file_data = file.readlines()
        for idx, row in enumerate(file_data):
            if idx == 0:
                v = row.strip()
            elif idx == 1:
                a = row.strip()
            else:
                try:
                    v1, v2 = row.split(" ")
                    self.add_aresta(v1.strip(), v2.strip())
                    self.mostra_matriz()
                except Exception as ex:
                    pass


# INSTANCIANDO O OBJETO
grafo = TGrafo(4)

# ADICIONA ARESTAS AO GRAFO
grafo.add_aresta(1, 2)
grafo.add_aresta(3, 2)
grafo.add_aresta(2, 4)

# VISUALIZA GRAFO RESULTANTE
grafo.mostra_matriz()

grafo.inDegree(6)

grafo.ehFonte(5)
grafo.leGraphFile("app/utils/graph_files/grafo_exemplo.txt")
print(1)
