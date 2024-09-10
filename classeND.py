class TGrafoND:

    """7) Criar uma outra classe TGrafoND e modifique as funções insereA, removeA e show para representar um grafo não-dirigido utilizando matriz de adjacência.
    """
    def __init__(self, vertices: int):
        """INICIALIZA UMA NOVA INSTÂNCIA DA CLASSE TGRAFO ND (GRAFO NÃO-DIRIGIDO).

        ARGS:
            VERTICES (INT): O NÚMERO DE VÉRTICES NO GRAFO.
        """
        self.vertices = vertices
        # CRIA A MATRIZ DE ADJACÊNCIA COM ZEROS, INICIALMENTE NÃO HÁ ARESTAS ENTRE OS VÉRTICES
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]  

    def insereA(self, u: int, v: int):
        """

        INSERE UMA ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO.

        ARGS:
            U (INT): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            V (INT): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
        """
        # ADICIONA A ARESTA EM AMBAS AS DIREÇÕES (POIS O GRAFO NÃO É DIRECIONADO)
        self.grafo[u-1][v-1] = 1  
        self.grafo[v-1][u-1] = 1  

    def removeA(self, u: int, v: int):
        """REMOVE A ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO E EXIBE A MATRIZ RESULTANTE.

        ARGS:
            U (INT): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            V (INT): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
        """
        # REMOVE A ARESTA DEFININDO OS VALORES CORRESPONDENTES NA MATRIZ COMO 0
        self.grafo[u-1][v-1] = 0  
        self.grafo[v-1][u-1] = 0  
        print(f"ARESTA REMOVIDA ENTRE OS VÉRTICES {u} E {v}.")
        # CHAMA O MÉTODO PARA MOSTRAR A MATRIZ ATUALIZADA
        self.show()  

    def show(self):
        """EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO."""
        print('A MATRIZ DE ADJACÊNCIA É:')
        # IMPRIME A MATRIZ DE ADJACÊNCIA LINHA POR LINHA
        for i in range(self.vertices):
            print(self.grafo[i])

    def completo(self) -> bool:
        """
        10) Fazer um método que verifique e retorne se o grafo (não dirigido) é completo.
        ---
        VERIFICA SE O GRAFO NÃO-DIRIGIDO É COMPLETO.

        UM GRAFO É CONSIDERADO COMPLETO SE TODOS OS PARES DE VÉRTICES DISTINTOS 
        ESTIVEREM CONECTADOS POR UMA ARESTA.

        RETURNS:
            BOOL: RETORNA TRUE SE O GRAFO FOR COMPLETO, CASO CONTRÁRIO, RETORNA FALSE.
        """
        # PERCORRE TODA A MATRIZ PARA VERIFICAR SE TODOS OS VÉRTICES DISTINTOS ESTÃO CONECTADOS
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.grafo[i][j] == 0: 
                    # SE ALGUMA PAR DE VÉRTICES NÃO ESTÁ CONECTADO, O GRAFO NÃO É COMPLETO
                    return False
        return True

    def tipo_conexidade(self) -> int:
        """
        13) Fazer um método que retorne o tipo de conexidade de um grafo não direcionado (0 - conexo ou 1 - não conexo – desconexo).

        ---
        VERIFICA O TIPO DE CONEXIDADE DE UM GRAFO NÃO DIRECIONADO.

        REALIZA UMA BUSCA EM PROFUNDIDADE (DFS) PARA DETERMINAR SE O GRAFO É CONEXO.
        
        RETURNS:
            INT: RETORNA 0 SE O GRAFO É CONEXO E 1 SE O GRAFO É DESCONEXO.
        """
        # INICIALIZA UMA LISTA PARA RASTREAR SE OS VÉRTICES FORAM VISITADOS DURANTE A DFS
        visitados = [False] * self.vertices 

        def busca_profundidade(v: int):
            """REALIZA A BUSCA EM PROFUNDIDADE (DFS) A PARTIR DE UM VÉRTICE.

            ARGS:
                V (INT): O ÍNDICE DO VÉRTICE DE PARTIDA PARA A BUSCA EM PROFUNDIDADE.
            """
            # MARCA O VÉRTICE COMO VISITADO
            visitados[v] = True
            # VERIFICA TODOS OS VÉRTICES ADJACENTES AO VÉRTICE ATUAL
            for i in range(self.vertices):
                if self.grafo[v][i] == 1 and not visitados[i]:
                    # REALIZA A DFS RECURSIVAMENTE NOS VÉRTICES ADJACENTES
                    busca_profundidade(i)

        # INICIA A BUSCA EM PROFUNDIDADE A PARTIR DO VÉRTICE 0
        busca_profundidade(0)

        # VERIFICA SE TODOS OS VÉRTICES FORAM VISITADOS DURANTE A BUSCA
        if all(visitados):
            # O GRAFO É CONEXO SE TODOS OS VÉRTICES FORAM ALCANÇADOS
            return 0
        else:
            # CASO CONTRÁRIO, O GRAFO É DESCONEXO
            return 1


# EXEMPLO DE USO
gND = TGrafoND(4)
# INSERE ALGUMAS ARESTAS ENTRE OS VÉRTICES
gND.insereA(1, 2)
gND.insereA(2, 3)
gND.insereA(3, 4)

# EXIBE A MATRIZ DE ADJACÊNCIA
gND.show()

# REMOVE UMA ARESTA E EXIBE A MATRIZ ATUALIZADA
gND.removeA(2, 3)

# VERIFICA SE O GRAFO É COMPLETO
if gND.completo():
    print("É UM GRAFO COMPLETO")
else:
    print("NÃO É UM GRAFO COMPLETO")

# VERIFICA O TIPO DE CONEXIDADE DO GRAFO
resultado = gND.tipo_conexidade()
if resultado == 0:
    print("O GRAFO É CONEXO")
else:
    print("O GRAFO É DESCONEXO")
