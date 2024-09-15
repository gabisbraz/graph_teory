from loguru import logger


class TGrafoND:
    def __init__(self, vertices: int):
        """
        INICIALIZA O GRAFO COM UMA MATRIZ DE ADJACÊNCIA
        DE TAMANHO `VERTICES` x `VERTICES`.

        Args:
            vertices (int): NÚMERO DE VÉRTICES DO GRAFO.
        """
        # INICIALIZA O NÚMERO DE VÉRTICES
        self.vertices = vertices
        # CRIA A MATRIZ DE ADJACÊNCIA COM TODOS OS VALORES INICIALIZADOS EM 0
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

        self.lista_adjacencia = {}

    def show(self):
        """
        7)	Criar uma outra classe TGrafoND e modifique as funções insereA,
        removeA e show para representar um grafo não-dirigido
        utilizando matriz de adjacência.

        ---

        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """
        logger.info("A MATRIZ DE ADJACÊNCIA É: ")
        for i in range(self.vertices):
            logger.info(self.grafo[i])

    def insereA(self, u: int, v: int):
        """
        7)	Criar uma outra classe TGrafoND e modifique as funções insereA,
        removeA e show para representar um grafo não-dirigido
        utilizando matriz de adjacência.

        ---

        INSERE UMA ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO.

        Args:
            U (int): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            V (int): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
        """
        # ADICIONA UMA ARESTA ENTRE U E V (NÃO DIRIGIDO)
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1
        # INFORMA A INSERÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
        logger.info(f"ARESTA INSERIDA ENTRE OS VÉRTICES {u} E {v}.")
        # self.show()

    def removeA(self, u: int, v: int):
        """
        7)	Criar uma outra classe TGrafoND e modifique as funções insereA,
        removeA e show para representar um grafo não-dirigido
        utilizando matriz de adjacência.

        ---

        REMOVE A ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO E EXIBE A MATRIZ RESULTANTE.

        Args:
            U (int): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            V (int): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
        """
        # REMOVE A ARESTA ENTRE U E V (NÃO DIRIGIDO)
        self.grafo[u - 1][v - 1] = 0
        self.grafo[v - 1][u - 1] = 0

        # INFORMA A REMOÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
        logger.info(f"ARESTA REMOVIDA ENTRE OS VÉRTICES {u} E {v}.")
        self.show()

    def remove_vertice_nao_direcionado(self, vertice: int):
        """
        9)	Fazer um método que permita remover um vértice do Grafo (não dirigido e dirigido).
        Não se esqueça de remover as arestas associadas

        ---

        REMOVE UM VÉRTICE DE UM GRAFO NÃO-DIRECIONADO E TODAS AS ARESTAS ASSOCIADAS.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO (1-INDEXADO).
        """

        # AJUSTA O ÍNDICE PARA 0-INDEXADO
        vertice = vertice - 1

        # REMOVER TODAS AS ARESTAS ASSOCIADAS AO VÉRTICE (NÃO DIRECIONADO)
        for i in range(self.vertices):
            # REMOVE AS ARESTAS ENTRE O VÉRTICE E TODOS OS OUTROS
            self.grafo[vertice][i] = 0  # REMOVE DA LINHA
            self.grafo[i][
                vertice
            ] = 0  # REMOVE DA COLUNA (REFLETE NOS NÃO-DIRECIONADOS)

        # REMOVER O VÉRTICE DA MATRIZ
        # REMOVE A LINHA DO VÉRTICE
        self.grafo.pop(vertice)

        # REMOVE A COLUNA DO VÉRTICE EM CADA LINHA RESTANTE
        for i in range(len(self.grafo)):
            self.grafo[i].pop(vertice)

        # ATUALIZAR O NÚMERO DE VÉRTICES
        self.vertices -= 1

        # INFORMA A REMOÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
        print(
            f"VÉRTICE {vertice + 1} E TODAS AS ARESTAS ASSOCIADAS FORAM REMOVIDAS (NÃO DIRECIONADO)."
        )
        self.mostra_matriz()

    def ehCompleto(self) -> bool:
        """
        10)	Fazer um método que verifique e retorne se o grafo (não dirigido) é completo.

        ---

        UM GRAFO É CONSIDERADO COMPLETO SE TODOS OS PARES DE VÉRTICES DISTINTOS
        ESTIVEREM CONECTADOS POR UMA ARESTA.

        Returns:
            bool: RETORNA TRUE SE O GRAFO FOR COMPLETO, CASO CONTRÁRIO, RETORNA FALSE.
        """
        # PERCORRE TODOS OS VÉRTICES DO GRAFO
        for i in range(self.vertices):
            for j in range(self.vertices):
                # SE I E J SÃO VÉRTICES DISTINTOS E NÃO EXISTE ARESTA ENTRE ELES, O GRAFO NÃO É COMPLETO
                if i != j and self.grafo[i][j] == 0:
                    return False
        # SE NÃO HÁ FALTA DE CONEXÃO ENTRE NENHUM PAR DE VÉRTICES, O GRAFO É COMPLETO
        return True

    def complemento_nao_dirigido(self) -> list:
        """
        12)	Fazer um método que retorne o complemento (grafo complementar) de um grafo
        (dirigido ou não) na forma de uma matriz de adjacência.

        ---

        CALCULA O GRAFO COMPLEMENTAR DE UM GRAFO NÃO DIRECIONADO - POSSUI AS ARESTAS
        INVERTIDAS EM RELAÇÃO AO GRAFO ORIGINAL, MANTENDO
        A DIAGONAL PRINCIPAL INALTERADA (SEM LAÇOS).

        Returns:
            list: A MATRIZ DE ADJACÊNCIA DO GRAFO COMPLEMENTAR.
        """
        # CRIA UMA NOVA MATRIZ PARA ARMAZENAR O COMPLEMENTO
        complemento_grafo = [
            [0 for _ in range(self.vertices)] for _ in range(self.vertices)
        ]

        # PERCORRE TODOS OS PARES DE VÉRTICES (M, N)
        for m in range(self.vertices):
            for n in range(m, self.vertices):
                if m != n:
                    # SE EXISTE UMA ARESTA NO GRAFO ORIGINAL, NÃO EXISTE NO COMPLEMENTO
                    if self.grafo[m][n] == 1:
                        complemento_grafo[m][n] = 0
                        complemento_grafo[n][
                            m
                        ] = 0  # SIMETRIA EM GRAFOS NÃO DIRECIONADOS
                    else:
                        complemento_grafo[m][n] = 1
                        complemento_grafo[n][
                            m
                        ] = 1  # SIMETRIA EM GRAFOS NÃO DIRECIONADOS

        return complemento_grafo

    def matriz_para_lista_adjacencia(self) -> dict:
        """
        18)	Escreva um método que converta uma representação de um grafo em outra. Por exemplo,
        converta um grafo armazenado em matriz de adjacência em uma lista de adjacência.

        ---

        CONVERTE UMA MATRIZ DE ADJACÊNCIA EM UMA LISTA DE ADJACÊNCIA.

        RETURNS:
            DICT: UM DICIONÁRIO ONDE CADA CHAVE REPRESENTA UM VÉRTICE E O VALOR ASSOCIADO
                É UMA LISTA DOS VÉRTICES VIZINHOS (ARESTAS CONECTADAS).
        """
        # CRIA UM DICIONÁRIO VAZIO PARA ARMAZENAR A LISTA DE ADJACÊNCIA
        lista_adjacencia = {}

        # PERCORRE TODOS OS VÉRTICES DO GRAFO
        for i in range(self.vertices):
            # INICIALIZA A LISTA DE VIZINHOS PARA O VÉRTICE ATUAL
            vizinhos = []
            for j in range(self.vertices):
                # SE HÁ UMA ARESTA ENTRE O VÉRTICE I E O VÉRTICE J, ADICIONA J NA LISTA DE VIZINHOS
                if self.grafo[i][j] == 1:
                    vizinhos.append(j + 1)

            # ASSOCIA O VÉRTICE I À SUA LISTA DE VIZINHOS NO DICIONÁRIO
            lista_adjacencia[i + 1] = vizinhos

        self.lista_adjacencia = lista_adjacencia

        return lista_adjacencia

    def tipo_conexidade(self) -> int:
        """
        13)	Fazer um método que retorne o tipo de conexidade de um grafo não direcionado
        (0 - conexo ou 1 - não conexo – desconexo).

        ---

        VERIFICA O TIPO DE CONEXIDADE DE UM GRAFO NÃO DIRECIONADO.

        Returns:
            int: RETORNA 0 SE O GRAFO É CONEXO E 1 SE O GRAFO É DESCONEXO.
        """
        # LISTA PARA MARCAR OS VÉRTICES VISITADOS
        visitados = [False] * self.vertices

        def busca_profundidade(v: int):
            """
            REALIZA A BUSCA EM PROFUNDIDADE (DFS) A PARTIR DE UM VÉRTICE.

            Args:
                v (int): O ÍNDICE DO VÉRTICE DE PARTIDA PARA A BUSCA EM PROFUNDIDADE.
            """
            visitados[v] = True
            # PERCORRE OS VÉRTICES VIZINHOS DO VÉRTICE ATUAL
            for i in range(self.vertices):
                # SE HÁ UMA ARESTA E O VÉRTICE AINDA NÃO FOI VISITADO, CONTINUA A BUSCA
                if self.grafo[v][i] == 1 and not visitados[i]:
                    busca_profundidade(i)

        # INICIA A BUSCA EM PROFUNDIDADE A PARTIR DO VÉRTICE 0
        busca_profundidade(0)

        # VERIFICA SE TODOS OS VÉRTICES FORAM VISITADOS
        if all(visitados):
            return 0  # O GRAFO É CONEXO
        else:
            return 1  # O GRAFO É DESCONEXO

    def remove_vertice(self, vertice: int):
        """
        24)	Fazer um método que permita remover um vértice do Grafo (não dirigido).
        Não se esqueça de remover as arestas associadas.

        ---

        REMOVE UM VÉRTICE DO GRAFO NÃO DIRECIONADO E AS ARESTAS ASSOCIADAS A ELE.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO (1-INDEXADO).

        """
        self.matriz_para_lista_adjacencia()

        logger.info(
            f"LISTA DE ADJACÊNCIA ANTERIOR A REMOÇÃO DO VÉRTICE: {self.lista_adjacencia}"
        )

        # Converte o índice do vértice de 1-indexado para 0-indexado
        vertice -= 1

        if vertice < 0 or vertice >= self.vertices:
            logger.info(f"O vértice {vertice + 1} não está no intervalo válido.")
            return

        # Remove o vértice da lista de adjacência
        for v in self.lista_adjacencia:
            if vertice + 1 in self.lista_adjacencia[v]:
                self.lista_adjacencia[v].remove(vertice + 1)

        # Remove o vértice do dicionário
        del self.lista_adjacencia[vertice + 1]

        # Atualiza os índices dos vértices no dicionário
        for v in self.lista_adjacencia:
            if v > vertice + 1:
                self.lista_adjacencia[v - 1] = self.lista_adjacencia.pop(v)

        # Atualiza o número de vértices
        self.vertices -= 1

        logger.info(f"VÉRTICE {vertice + 1} REMOVIDO COM SUCESSO!")
        return self.lista_adjacencia


if __name__ == "__main__":
    gND = TGrafoND(4)
    gND.insereA(1, 2)
    gND.insereA(2, 3)
    gND.insereA(3, 4)

    gND.show()

    gND.removeA(2, 3)  # Remove a aresta e imprime a matriz junto com a mensagem

    if gND.completo():
        logger.info("É um grafo completo")
    else:
        logger.info("Não é um grafo completo")

    resultado = gND.tipo_conexidade()
    if resultado == 0:
        logger.info("O grafo é conexo")
    else:
        logger.info("O grafo é desconexo")
