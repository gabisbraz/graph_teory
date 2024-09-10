from loguru import logger


class TGrafo:
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
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, linha: int, coluna: int):
        """
        ADICIONA UMA ARESTA DIRECIONADA AO GRAFO ENTRE OS
        VÉRTICES `LINHA` E `COLUNA`.

        Args:
            linha (int): ÍNDICE DA LINHA (VÉRTICE DE PARTIDA).
            coluna (int): ÍNDICE DA COLUNA (VÉRTICE DE CHEGADA).
        """

        # ADICIONA A ARESTA, DEFININDO O VALOR 1 NA POSIÇÃO ESPECÍFICA DA MATRIZ
        self.grafo[linha - 1][coluna - 1] = 1
        logger.success(f"ARESTA ADICIONADA DO VÉRTICES {linha} PARA {coluna}")

    def mostra_matriz(self):
        """
        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """
        logger.info("A MATRIZ DE ADJACÊNCIA É: ")
        for i in range(self.vertices):
            logger.info(self.grafo[i])

    def inDegree(self, vertice: int) -> int:
        """
        1) CALCULA O GRAU DE ENTRADA DO VÉRTICE, OU SEJA, O NÚMERO DE
        ARESTAS QUE ENTRAM NO VÉRTICE ESPECIFICADO.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE PARA O QUAL O GRAU DE
                ENTRADA SERÁ CALCULADO.

        Returns:
            int: O GRAU DE ENTRADA DO VÉRTICE.
        """
        grau = 0
        # PERCORRE CADA LINHA DA MATRIZ E SOMA AS ARESTAS QUE CHEGAM AO VÉRTICE
        for i in range(self.vertices):
            grau += self.grafo[i][vertice - 1]
        return grau

    def outDegree(self, vertice: int) -> int:
        """
        2) CALCULA O GRAU DE SAÍDA DO VÉRTICE, OU SEJA, O NÚMERO DE ARESTAS
        QUE SAEM DO VÉRTICE ESPECIFICADO.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE PARA O QUAL O GRAU DE
                SAÍDA SERÁ CALCULADO.

        Returns:
            int: O GRAU DE SAÍDA DO VÉRTICE.
        """
        grau = 0
        # PERCORRE A LINHA CORRESPONDENTE AO VÉRTICE E SOMA AS ARESTAS QUE SAEM DO VÉRTICE
        for i in range(self.vertices):
            grau += self.grafo[vertice - 1][i]
        return grau

    def ehFonte(self, vertice: int) -> int:
        """
        3) Escreva um método para um grafo direcionado que recebe um vértice como parâmetro e
        retorne 1 se vértice for uma fonte (grau de saída maior que zero e grau de entrada igual a 0),
        ou 0 caso contrário. O método deve ser implementado para a classe TGrafo como matriz
        de adjacência.

        ---

        VERIFICA SE UM VÉRTICE É UMA FONTE, OU SEJA, SE POSSUI GRAU
        DE SAÍDA > 0 E GRAU DE ENTRADA = 0.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER VERIFICADO.

        Returns:
            int: RETORNA 1 SE O VÉRTICE É FONTE, CASO CONTRÁRIO RETORNA 0.
        """
        if (self.outDegree(vertice) > 0) and (self.inDegree(vertice) == 0):
            return 1
        return 0

    def sorvedouro(self, vertice: int) -> int:
        """
        4) VERIFICA SE UM VÉRTICE É UM SORVEDOURO, OU SEJA, SE
        POSSUI GRAU DE ENTRADA > 0 E GRAU DE SAÍDA = 0.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER VERIFICADO.

        Returns:
            int: RETORNA 1 SE O VÉRTICE É SORVEDOURO, CASO CONTRÁRIO RETORNA 0.
        """
        # VERIFICA AS CONDIÇÕES PARA O VÉRTICE SER SORVEDOURO
        if (self.inDegree(vertice) > 0) and (self.outDegree(vertice) == 0):
            return 1
        return 0

    def ehSimetrico(self) -> int:
        """
        5) Escreva um método que receba um grafo dirigido como parâmetro e retorna 1
        se o grafo for simétrico e 0 caso contrário. O método deve ser implementado
        para a classe TGrafo que utiliza matriz de adjacência.

        ---

        UM GRAFO É CONSIDERADO SIMÉTRICO SE, PARA TODAS AS ARESTAS, O VÉRTICE `I`
        ESTIVER CONECTADO AO VÉRTICE `J`, ENTÃO O VÉRTICE `J` TAMBÉM DEVE
        ESTAR CONECTADO AO VÉRTICE `I`.

        Returns:
            int: RETORNA 1 SE A MATRIZ É SIMÉTRICA (GRAFO NÃO DIRECIONADO),
            CASO CONTRÁRIO RETORNA 0 (GRAFO DIRECIONADO).
        """
        # PERCORRE OS VÉRTICES DA MATRIZ DE ADJACÊNCIA
        for i in range(self.vertices):
            # VERIFICA A SIMETRIA SOMENTE NA METADE SUPERIOR DA MATRIZ
            for j in range(i, self.vertices):
                # SE A MATRIZ NÃO FOR SIMÉTRICA, O GRAFO É DIRECIONADO
                if self.grafo[i][j] != self.grafo[j][i]:
                    return 0
        # SE A MATRIZ FOR SIMÉTRICA, O GRAFO NÃO É DIRECIONADO
        return 1

    def leArquivoGrafo(self, file_name: str):
        """
        6) Um grafo pode ser armazenado em um arquivo com o seguinte formato:

        6
        8
        0 1
        0 5
        1 0
        1 5
        2 4
        3 1
        4 3
        3 5

        Onde na primeira linha contém um inteiro V (vértice), na segunda contém um inteiro A
        (arestas) e nas demais linha contém dois inteiros pertencentes ao intervalo 0..V-1.
        Se interpretarmos cada linha do arquivo como uma aresta, podemos dizer que o arquivo
        define um grafo com vértices 0..V-1. Escreva um método que receba um nome de arquivo
        com o formato acima e construa a representação do grafo como matriz de adjacência.

        ---

        LÊ UM ARQUIVO QUE CONTÉM A REPRESENTAÇÃO DO GRAFO E CARREGA ESSA REPRESENTAÇÃO NO OBJETO `TGRAFO`.

        Args:
            file_name (str): O NOME DO ARQUIVO QUE CONTÉM A REPRESENTAÇÃO DO GRAFO.
        """
        try:
            with open(file_name, "r") as file:
                # LÊ O NÚMERO DE VÉRTICES
                vertices = int(file.readline().strip())

                self.vertices = vertices
                self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

                # LÊ O NÚMERO DE ARESTAS (ATUALMENTE NÃO UTILIZADO)
                arestas = int(file.readline().strip())

                # PERCORRE CADA LINHA DO ARQUIVO PARA ADICIONAR AS ARESTAS
                for row in file:
                    u, vertice = map(int, row.strip().split())
                    self.add_aresta(u, vertice)
            # EXIBE A MATRIZ DE ADJACÊNCIA
            self.mostra_matriz()

        except FileNotFoundError:
            logger.info(f"ARQUIVO {file_name} NÃO ENCONTRADO.")
        except ValueError:
            logger.info("FORMATO DO ARQUIVO INVÁLIDO.")

    def remove_vertice_direcionado(self, vertice: int):
        """
        9) Fazer um método que permita remover um vértice do Grafo (não dirigido e dirigido).
        Não se esqueça de remover as arestas associadas.

        ---

        REMOVE UM VÉRTICE DE UM GRAFO DIRECIONADO E TODAS AS ARESTAS ASSOCIADAS.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO (1-INDEXADO).
        """
        # AJUSTA O ÍNDICE PARA 0-INDEXADO
        vertice = vertice - 1

        # REMOVER TODAS AS ARESTAS ASSOCIADAS AO VÉRTICE (DIRECIONADO)
        for i in range(self.vertices):
            # REMOVE AS ARESTAS QUE PARTEM OU CHEGAM AO VÉRTICE
            self.grafo[vertice][i] = 0  # REMOVE A LINHA (SAÍDA DO VÉRTICE)
            self.grafo[i][vertice] = 0  # REMOVE A COLUNA (ENTRADA NO VÉRTICE)

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
            f"VÉRTICE {vertice + 1} E TODAS AS ARESTAS ASSOCIADAS FORAM REMOVIDAS (DIRECIONADO)"
        )
        self.mostra_matriz()

    def ehCompleto(self) -> int:
        """
        11)	Fazer um método que verifique e retorne e o grafo (dirigido) é completo

        ---

        UM GRAFO DIRECIONADO É CONSIDERADO COMPLETO SE, PARA TODOS OS PARES
        DE VÉRTICES DISTINTOS `(I, J)`, EXISTIR UMA ARESTA DE `I` PARA `J`
        E UMA ARESTA DE `J` PARA `I`.

        RETURNS:
            int: RETORNA 1 SE O GRAFO É COMPLETO, CASO CONTRÁRIO, RETORNA 0.
        """
        # PERCORRE TODOS OS VÉRTICES DO GRAFO
        for i in range(self.vertices):
            for j in range(self.vertices):
                # VERIFICA SE EXISTE UMA ARESTA EM AMBAS AS DIREÇÕES ENTRE OS VÉRTICES DISTINTOS
                if i != j and (self.grafo[i][j] == 0 or self.grafo[j][i] == 0):
                    return 0  # SE FALTAR ALGUMA CONEXÃO, O GRAFO NÃO É COMPLETO
        return 1  # SE TODAS AS CONEXÕES EXISTIREM, O GRAFO É COMPLETO

    def complemento(self) -> list:
        """
        12)	Fazer um método que retorne o complemento (grafo complementar) de um grafo
        (dirigido ou não) na forma de uma matriz de adjacência.

        ---

        CALCULA O GRAFO COMPLEMENTAR, OU SEJA, UM GRAFO QUE POSSUI AS
        ARESTAS INVERTIDAS EM RELAÇÃO AO GRAFO ORIGINAL.

        Returns:
            list: A MATRIZ DE ADJACÊNCIA DO GRAFO COMPLEMENTAR.
        """
        # CRIA UMA CÓPIA DA MATRIZ DE ADJACÊNCIA
        complemento_grafo = self.grafo
        # INVERTE OS VALORES DA MATRIZ, EXCETO NA DIAGONAL PRINCIPAL
        for m in range(self.vertices):
            for n in range(self.vertices):
                if m != n:
                    if self.grafo[m][n] == 1:
                        complemento_grafo[m][n] = 0
                    else:
                        complemento_grafo[m][n] = 1

        return complemento_grafo

    def categoria_conexidade(self) -> int:
        """
        Retorna a categoria de conexidade de um grafo direcionado:
        - 3 (C3): Grafo fortemente conexo.
        - 2 (C2): Grafo unicamente conexo.
        - 1 (C1): Grafo fracamente conexo.
        - 0 (C0): Grafo desconexo.

        Returns:
            int: Categoria de conexidade (3 – C3, 2 – C2, 1 – C1 ou 0 – C0).
        """

        def bfs(start, grafo):
            """
            Realiza uma busca em largura (BFS) a partir de um vértice inicial `start`
            e verifica se todos os vértices são alcançáveis.
            """
            visitados = [False] * self.vertices
            fila = [start]
            visitados[start] = True

            while fila:
                v = fila.pop(0)
                for i in range(self.vertices):
                    if grafo[v][i] == 1 and not visitados[i]:
                        fila.append(i)
                        visitados[i] = True
            return all(visitados)

        # Verifica a conectividade forte (C3)
        for i in range(self.vertices):
            if not bfs(
                i, self.grafo
            ):  # Verifica se todos os vértices são acessíveis a partir de `i`
                break
        else:
            return 3  # Se todos os vértices são fortemente conectados

        # Cria o grafo inverso (transposto)
        grafo_transposto = [
            [self.grafo[j][i] for j in range(self.vertices)]
            for i in range(self.vertices)
        ]

        # Verifica a conectividade fraca (C1)
        for i in range(self.vertices):
            if not bfs(
                i,
                [
                    [
                        1 if self.grafo[j][i] or grafo_transposto[j][i] else 0
                        for i in range(self.vertices)
                    ]
                    for j in range(self.vertices)
                ],
            ):
                break
        else:
            return 1  # Se o grafo é fracamente conexo

        # Verifica se o grafo é unicamente conexo (C2)
        for i in range(self.vertices):
            if not bfs(i, self.grafo) or not bfs(i, grafo_transposto):
                return 0  # Desconexo

        return 2  # Unicamente conexo (C2)

    def reduzido(self) -> list:
        """
        15) Fazer um método que retorne o grafo reduzido de um grafo direcionado no
        formato de uma matriz de adjacência.

        ---

        CALCULA O GRAFO REDUZIDO DE UM GRAFO DIRECIONADO, QUE CONSISTE EM COLAPSAR
        AS COMPONENTES FORTEMENTE CONEXAS (CFCs) DO GRAFO EM VÉRTICES ÚNICOS.

        Returns:
            list: A MATRIZ DE ADJACÊNCIA DO GRAFO REDUZIDO.
        """

        def dfs(v, visitados, pilha):
            """
            REALIZA A BUSCA EM PROFUNDIDADE (DFS) E ADICIONA OS VÉRTICES NA PILHA APÓS COMPLETAR A BUSCA.

            ARGS:
                v (int): VÉRTICE ATUAL.
                visitados (list): LISTA QUE INDICA SE UM VÉRTICE JÁ FOI VISITADO.
                pilha (list): PILHA QUE ARMAZENA OS VÉRTICES EM ORDEM DE FINALIZAÇÃO DA DFS.
            """
            visitados[v] = True
            for i in range(self.vertices):
                if self.grafo[v][i] == 1 and not visitados[i]:
                    dfs(i, visitados, pilha)
            pilha.append(v)

        def dfs_invertido(v, visitados, componente):
            """
            REALIZA A BUSCA EM PROFUNDIDADE NO GRAFO TRANSPOSTO PARA ENCONTRAR COMPONENTES FORTEMENTE CONEXAS.

            ARGS:
                V (int): VÉRTICE ATUAL.
                visitados (list): LISTA QUE INDICA SE UM VÉRTICE JÁ FOI VISITADO.
                componente (list): LISTA QUE ARMAZENA OS VÉRTICES DA COMPONENTE FORTEMENTE CONEXA.
            """
            visitados[v] = True
            componente.append(v)
            for i in range(self.vertices):
                if grafo_transposto[v][i] == 1 and not visitados[i]:
                    dfs_invertido(i, visitados, componente)

        # REALIZAR DFS NO GRAFO ORIGINAL E ARMAZENAR A ORDEM DOS VÉRTICES EM UMA PILHA
        pilha = []
        visitados = [False] * self.vertices
        for i in range(self.vertices):
            if not visitados[i]:
                dfs(i, visitados, pilha)

        # TRANSFORMAR O GRAFO EM SEU GRAFO TRANSPOSTO
        grafo_transposto = [
            [0 for _ in range(self.vertices)] for _ in range(self.vertices)
        ]
        for i in range(self.vertices):
            for j in range(self.vertices):
                grafo_transposto[i][j] = self.grafo[j][i]

        # REALIZAR DFS NO GRAFO TRANSPOSTO, NA ORDEM DA PILHA, PARA ENCONTRAR CFCs
        visitados = [False] * self.vertices
        componentes_fortemente_conexas = []
        while pilha:
            v = pilha.pop()
            if not visitados[v]:
                componente = []
                dfs_invertido(v, visitados, componente)
                componentes_fortemente_conexas.append(componente)

        # CRIAR O GRAFO REDUZIDO COM BASE NAS COMPONENTES FORTEMENTE CONEXAS
        num_componentes = len(componentes_fortemente_conexas)
        grafo_reduzido = [
            [0 for _ in range(num_componentes)] for _ in range(num_componentes)
        ]

        # MAPEAR OS VÉRTICES ORIGINAIS PARA SUAS RESPECTIVAS COMPONENTES
        componente_de = [-1] * self.vertices
        for idx, componente in enumerate(componentes_fortemente_conexas):
            for v in componente:
                componente_de[v] = idx

        # PREENCHER AS ARESTAS NO GRAFO REDUZIDO ENTRE COMPONENTES DIFERENTES
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] == 1:
                    comp_i = componente_de[i]
                    comp_j = componente_de[j]
                    if comp_i != comp_j:
                        grafo_reduzido[comp_i][comp_j] = 1

        return grafo_reduzido

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
                    vizinhos.append(j)

            # ASSOCIA O VÉRTICE I À SUA LISTA DE VIZINHOS NO DICIONÁRIO
            lista_adjacencia[i] = vizinhos

        return lista_adjacencia

    def verifica_sorvedor(self, vertice: int) -> int:
        """
        21)	Escreva um método que receba um grafo e um vértice como parâmetro, retorne 1
        se vértice for um sorvedouro (grau de entrada maior que zero e grau de saída igual a 0),
        ou 0 caso contrário. O método deve ser implementado para a classe TGrafo que utiliza
        lista de adjacência.

        ---

        VERIFICA SE O VÉRTICE DADO É UM SORVEDOURO NO GRAFO.

        UM VÉRTICE É CONSIDERADO SORVEDOURO SE TEM UM GRAU DE ENTRADA MAIOR QUE ZERO E
        UM GRAU DE SAÍDA IGUAL A ZERO.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER VERIFICADO.

        Returns:
            int: RETORNA 1 SE O VÉRTICE FOR UM SORVEDOURO, CASO CONTRÁRIO RETORNA 0.
        """
        # VERIFICA SE O VÉRTICE ESTÁ NO GRAFO
        if vertice not in self.lista_adjacencia:
            raise ValueError(f"O vértice {vertice} não está no grafo.")

        grau_saida = len(self.lista_adjacencia[vertice])
        grau_entrada = 0

        # CALCULA O GRAU DE ENTRADA
        for v, vizinhos in self.lista_adjacencia.items():
            if vertice in vizinhos:
                grau_entrada += 1

        # CHECA SE O VÉRTICE É UM SORVEDOURO
        if grau_entrada > 0 and grau_saida == 0:
            return 1
        else:
            return 0

    def percurso_profundidade(self, start: int) -> list:
        """
        REALIZA UM PERCURSO EM PROFUNDIDADE A PARTIR DE UM VÉRTICE INICIAL.

        Args:
            start (int): O ÍNDICE DO VÉRTICE INICIAL.

        Returns:
            list: LISTA DOS VÉRTICES NA ORDEM DO PERCURSO.
        """

        def dfs(v: int, visitados: list, percurso: list):
            # MARCA O VÉRTICE 'v' COMO VISITADO E ADICIONA À LISTA DE PERCURSO.
            visitados[v] = True
            percurso.append(v)
            # ITERA SOBRE TODOS OS VÉRTICES PARA ENCONTRAR VIZINHOS NÃO VISITADOS.
            for i in range(self.vertices):
                if self.grafo[v][i] == 1 and not visitados[i]:
                    # CHAMA A FUNÇÃO DFS RECURSIVAMENTE PARA VIZINHOS NÃO VISITADOS.
                    dfs(i, visitados, percurso)

        # INICIALIZA A LISTA DE VÉRTICES VISITADOS COMO FALSA PARA TODOS.
        visitados = [False] * self.vertices
        # INICIALIZA A LISTA DE PERCURSO.
        percurso = []
        # INICIA O PERCURSO EM PROFUNDIDADE A PARTIR DO VÉRTICE INICIAL.
        dfs(start - 1, visitados, percurso)
        # CONVERTE A LISTA DE VÉRTICES PARA A FORMA ORIGINAL (ADICIONA 1).
        percurso = [n + 1 for n in percurso]
        # RETORNA A LISTA DE VÉRTICES NA ORDEM DO PERCURSO.
        return percurso

    def percurso_largura(self, vertice_inicial: int) -> list:
        """
        REALIZA UM PERCURSO EM LARGURA A PARTIR DE UM VÉRTICE INICIAL.

        Args:
            vertice_inicial (int): O ÍNDICE DO VÉRTICE INICIAL.

        Returns:
            list: LISTA DOS VÉRTICES NA ORDEM DO PERCURSO.
        """

        def noAdjacente(n: int, visitados: list):
            # PROCURA UM VÉRTICE ADJACENTE NÃO VISITADO AO VÉRTICE 'n'.
            for i in range(self.vertices):
                if self.grafo[n][i] == 1 and not visitados[i]:
                    return i
            return -1

        # INICIALIZA A LISTA DE VÉRTICES VISITADOS COMO FALSA PARA TODOS.
        visitados = [False] * self.vertices
        # INICIALIZA A FILA PARA O PERCURSO EM LARGURA.
        fila = []
        # INICIALIZA A LISTA DE PERCURSO.
        percurso = []

        # MARCA O VÉRTICE INICIAL COMO VISITADO E ADICIONA NA FILA.
        visitados[vertice_inicial - 1] = True
        fila.append(vertice_inicial - 1)

        # INICIA O PERCURSO EM LARGURA.
        while fila:
            # REMOVE O VÉRTICE DO INÍCIO DA FILA.
            n = fila.pop(0)
            # ADICIONA O VÉRTICE ATUAL À LISTA DE PERCURSO.
            percurso.append(n + 1)
            while True:
                # ENCONTRA UM VÉRTICE ADJACENTE NÃO VISITADO.
                m = noAdjacente(n, visitados)
                if m == -1:
                    # SE NÃO HÁ MAIS VÉRTICES ADJACENTES NÃO VISITADOS, SAIA DO LOOP INTERNO.
                    break
                # ADICIONA O VÉRTICE ADJACENTE À FILA E MARCA COMO VISITADO.
                fila.append(m)
                visitados[m] = True

        # RETORNA A LISTA DE VÉRTICES NA ORDEM DO PERCURSO.
        return percurso


if __name__ == "__main__":
    # INSTANCIANDO O OBJETO
    grafo = TGrafo(4)

    # ADICIONA ARESTAS AO GRAFO
    grafo.add_aresta(1, 2)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(3, 4)
    grafo.add_aresta(4, 1)

    # VISUALIZA GRAFO RESULTANTE
    grafo.mostra_matriz()

    grafo.inDegree(6)

    grafo.ehFonte(5)
    grafo.remove_vertice(2)
    logger.info(1)
