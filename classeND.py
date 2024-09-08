class TGrafoND:
    def __init__(self, vertices: int):
        """Inicializa uma nova instância da classe TGrafoND.

        Args:
            vertices (int): O número de vértices no grafo.
        """
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]  

#Exercício 7
    def insereA(self, u: int, v: int):
        """Insere uma aresta entre os vértices u e v em um grafo não-dirigido.

        Args:
            u (int): O índice do vértice de origem (1-indexado).
            v (int): O índice do vértice de destino (1-indexado).
        """
        self.grafo[u-1][v-1] = 1  
        self.grafo[v-1][u-1] = 1  

    def removeA(self, u: int, v: int):
        """Remove a aresta entre os vértices u e v em um grafo não-dirigido e exibe a matriz resultante.

        Args:
            u (int): O índice do vértice de origem (1-indexado).
            v (int): O índice do vértice de destino (1-indexado).
        """
        self.grafo[u-1][v-1] = 0  
        self.grafo[v-1][u-1] = 0  
        print(f"Aresta removida entre os vértices {u} e {v}.")
        self.show()  

    def show(self):
        """Exibe a matriz de adjacência do grafo.
        """
        print('A matriz de adjacência é:')
        for i in range(self.vertices):
            print(self.grafo[i])

#Exercício 10
    def completo(self: bool):
        """Verifica se o grafo não-dirigido é completo.
        Um grafo é considerado completo se todos os pares de vértices distintos 
        estiverem conectados por uma aresta.

        Args:
            None (Este método não requer parâmetros adicionais além de `self`).

        Returns:
            bool: Retorna True se o grafo for completo, caso contrário, retorna False.
    """
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.grafo[i][j] == 0: 
                    return False
        return True
    
#Exercício 13
    def tipo_conexidade(self: int):
        """
        Verifica o tipo de conexidade de um grafo não direcionado.

        Args:
            self (int): Número de vértices no grafo e a estrutura da matriz de adjacência.
            
        Returns:
            int: Retorna 0 se o grafo é conexo e 1 se o grafo é desconexo.
        """
        visitados = [False] * self.vertices 

        def busca_profundidade(v: int):
            """
            Realiza a busca em profundidade (DFS) a partir de um vértice.

            Args:
                v (int): O índice do vértice de partida para a busca em profundidade.
            """
            visitados[v] = True
            for i in range(self.vertices):
                if self.grafo[v][i] == 1 and not visitados[i]:
                    busca_profundidade(1)

        busca_profundidade(0)

        if all(visitados):
            return 0
        else:
            return 1
        


# Exemplo de uso
gND = TGrafoND(4)
gND.insereA(1, 2)
gND.insereA(2, 3)
gND.insereA(3, 4)

gND.show()

gND.removeA(2, 3)  # Remove a aresta e imprime a matriz junto com a mensagem

if gND.completo():
    print("É um grafo completo")
else:
    print("Não é um grafo completo")

resultado = gND.tipo_conexidade()
if resultado == 0:
    print("O grafo é conexo")
else:
    print("O grafo é desconexo")

