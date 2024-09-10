class TGrafo:
    def __init__(self, vertices: int):
        """ INICIALIZA UMA NOVA INSTÂNCIA DA CLASSE TGRAFO.

        ARGS:
            VERTICES (INT): O NÚMERO DE VÉRTICES NO GRAFO.
        """
        self.vertices = vertices
        # CRIAÇÃO DA MATRIZ DE ADJACÊNCIA
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

    def add_aresta(self, u: int, v: int, peso: float):
        """
        16) Modifique a classe TGrafo e os métodos correspondentes para permitir a criação de um grafo direcionado rotulado (valor float) nas arestas.
        ---
        ADICIONA UMA ARESTA DIRECIONADA DO VÉRTICE U AO VÉRTICE V.

        ARGS:
            U (INT): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            V (INT): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
            PESO (FLOAT): O PESO DA ARESTA.
        """
        # AJUSTA PARA INDEXAÇÃO COMEÇANDO EM 1
        self.grafo[u-1][v-1] = peso

    def mostra_matriz(self):
        """EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO."""
        print('A MATRIZ DE ADJACÊNCIA É:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def inDegree(self, v: int) -> int:
        """
        1) Escreva um método “int inDegree(int v)” que calcula e retorna o grau de entrada de um vértice v de um grafo dirigido. O método deve ser implementado na classe TGrafo da matriz  de adjacência. Obs: Grau de entrada de v é o total de arestas que chegam no vértice v. 

        ---
        CALCULA O GRAU DE ENTRADA (CONTAGEM DE ARESTAS) DE UM VÉRTICE V EM UM GRAFO DIRECIONADO.

        ARGS:
            V (INT): O ÍNDICE DO VÉRTICE CUJO GRAU DE ENTRADA SERÁ CALCULADO (1-INDEXADO).

        RETURNS:
            INT: O GRAU DE ENTRADA DO VÉRTICE V.
        """
        grau = 0
        # PERCORRE A COLUNA DO VÉRTICE V PARA VERIFICAR QUANTAS ARESTAS CHEGAM A ELE
        for i in range(self.vertices):
            if self.grafo[i][v-1] != 0:
                grau += 1
        return grau

    def outDegree(self, v: int) -> int:
        """CALCULA O GRAU DE SAÍDA (CONTAGEM DE ARESTAS) DE UM VÉRTICE V EM UM GRAFO DIRECIONADO.

        ARGS:
            V (INT): O ÍNDICE DO VÉRTICE CUJO GRAU DE SAÍDA SERÁ CALCULADO (1-INDEXADO).

        RETURNS:
            INT: O GRAU DE SAÍDA DO VÉRTICE V.
        """
        grau = 0
        # PERCORRE A LINHA DO VÉRTICE V PARA VERIFICAR QUANTAS ARESTAS SAEM DELE
        for i in range(self.vertices):
            if self.grafo[v-1][i] != 0:
                grau += 1
        return grau

    def sorvedouro(self, v: int) -> int:
        """
        4) Escreva um método para um grafo direcionado que recebe um vértice como parâmetro, retorne 1 se vértice for um sorvedouro (grau de entrada maior que zero e grau de saída igual a 0), ou 0 caso contrário. O método deve ser implementado para a classe TGrafo que utiliza matriz de adjacência.

        ---
        VERIFICA SE O VÉRTICE V É UM SORVEDOURO.

        UM VÉRTICE É CONSIDERADO UM SORVEDOURO SE SEU GRAU DE ENTRADA FOR MAIOR QUE 0 
        E SEU GRAU DE SAÍDA FOR 0.

        ARGS:
            V (INT): O ÍNDICE DO VÉRTICE A SER VERIFICADO (1-INDEXADO).

        RETURNS:
            INT: RETORNA 1 SE O VÉRTICE FOR UM SORVEDOURO, CASO CONTRÁRIO, 0.
        """
        # VERIFICA SE O GRAU DE ENTRADA É MAIOR QUE 0 E O GRAU DE SAÍDA É IGUAL A 0
        if self.inDegree(v) > 0 and self.outDegree(v) == 0:
            return 1
        else:
            return 0
  
# EXEMPLO DE USO
g = TGrafo(4)
g.add_aresta(1, 2, 1.5)
g.add_aresta(3, 2, 1.0)
g.add_aresta(2, 4, 2.1)

g.mostra_matriz()

vertice = 4
print(f'GRAU DE ENTRADA DO VÉRTICE {vertice}: {g.inDegree(vertice)}')
print(f'GRAU DE SAÍDA DO VÉRTICE {vertice}: {g.outDegree(vertice)}')
print(f'O VÉRTICE {vertice} É UM SORVEDOURO? {g.sorvedouro(vertice)}')

