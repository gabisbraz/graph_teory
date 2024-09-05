class TGrafo:
    def __init__(self, vertices: int):
        """Inicializa uma nova instância da classe TGrafo.

        Args:
            vertices (int): O número de vértices no grafo.
        """
        self.vertices = vertices 
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)] # Criação da matriz de adjacência

    def add_aresta(self, u: int, v: int):
        """Adiciona uma aresta direcionada do vértice u ao vértice v.

        Args:
            u (int): O índice do vértice de origem (1-indexado).
            v (int): O índice do vértice de destino (1-indexado).
        """
        self.grafo[u-1][v-1] = 1 # Ajusta para indexação começando em 1

    def mostra_matriz(self):
        """Exibe a matriz de adjacência do grafo.
        """
        print('A matriz de adjacência é:')
        for i in range(self.vertices):
            print(self.grafo[i])

     #Exercício 1       
    def inDegree(self, v: int) -> int:
        """Calcula o grau de entrada de um vértice v em um grafo direcionado.

        Args:
            v (int): O índice do vértice cujo grau de entrada será calculado (1-indexado).

        Returns:
            int: O grau de entrada do vértice v.
        """
        grau = 0 
        for i in range(self.vertices):
            grau += self.grafo[i][v-1]
        return grau
    
    def outDegree(self, v: int) -> int:
        """Calcula o grau de saída de um vértice v em um grafo direcionado.

        Args:
            v (int): O índice do vértice cujo grau de saída será calculado (1-indexado).

        Returns:
            int: O grau de saída do vértice v.
        """
        grau = 0
        for i in range(self.vertices):
            grau += self.grafo[v-1][i]
        return grau
    
    #Exercício 4
    def sorvedouro(self, v: int) -> int:
        """Verifica se o vértice v é um sorvedouro.

        Um vértice é considerado um sorvedouro se seu grau de entrada for maior que 0 
        e seu grau de saída for 0.

        Args:
            v (int): O índice do vértice a ser verificado (1-indexado).

        Returns:
            int: Retorna 1 se o vértice for um sorvedouro, caso contrário, 0.
        """
        if self.inDegree(v) > 0 and self.outDegree(v) == 0:
            return 1
        else:
            return 0

def main():
    # Exemplo de uso
    g = TGrafo(4)
    g.add_aresta(1, 2)
    g.add_aresta(3, 2)
    g.add_aresta(2, 4)

    g.mostra_matriz()

    vertice = 4
    print(f'Grau de entrada do vértice {vertice}: {g.inDegree(vertice)}')
    print(f'Grau de saída do vértice {vertice}: {g.outDegree(vertice)}')
    print(f'O vértice {vertice} é um sorvedouro? {g.sorvedouro(vertice)}')
