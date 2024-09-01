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

    def mostra_matriz(self):
        """
        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """
        print("A MATRIZ DE ADJACÊNCIA É: ")
        for i in range(self.vertices):
            print(self.grafo[i])

    def inDegree(self, vertice: int) -> int:
        """
        CALCULA O GRAU DE ENTRADA DO VÉRTICE, OU SEJA, O NÚMERO DE
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
            if len(self.grafo[i]) < vertice:
                return None
            grau += self.grafo[i][vertice - 1]
        return grau

    def outDegree(self, vertice: int) -> int:
        """
        CALCULA O GRAU DE SAÍDA DO VÉRTICE, OU SEJA, O NÚMERO DE ARESTAS
        QUE SAEM DO VÉRTICE ESPECIFICADO.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE PARA O QUAL O GRAU DE
                SAÍDA SERÁ CALCULADO.

        Returns:
            int: O GRAU DE SAÍDA DO VÉRTICE.
        """
        grau = 0
        if len(self.grafo) < vertice:
            return None
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
        if vertice is not None:
            try:
                # VERIFICA AS CONDIÇÕES PARA O VÉRTICE SER FONTE
                if (self.outDegree(vertice) > 0) and (self.inDegree(vertice) == 0):
                    return 1
            except TypeError as ex:
                return 0
        return None

    def sorvedouro(self, vertice: int) -> int:
        """
        VERIFICA SE UM VÉRTICE É UM SORVEDOURO, OU SEJA, SE
        POSSUI GRAU DE ENTRADA > 0 E GRAU DE SAÍDA = 0.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER VERIFICADO.

        Returns:
            int: RETORNA 1 SE O VÉRTICE É SORVEDOURO, CASO CONTRÁRIO RETORNA 0.
        """
        if vertice is not None:
            try:
                # VERIFICA AS CONDIÇÕES PARA O VÉRTICE SER SORVEDOURO
                if (self.inDegree(vertice) > 0) and (self.outDegree(vertice) == 0):
                    return 1
            except TypeError as ex:
                return 0
        return None

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

        LÊ UM ARQUIVO QUE CONTÉM A REPRESENTAÇÃO DO GRAFO E
        CARREGA ESSA REPRESENTAÇÃO NO OBJETO `TGRAFO`.

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

    def remove_vertice(self, vertice: int) -> bool:
        """
        9) Fazer um método que permita remover um vértice do Grafo (não dirigido e dirigido).
        Não se esqueça de remover as arestas associadas.

        ---

        REMOVE UM VÉRTICE ESPECÍFICO DO GRAFO E ATUALIZA A MATRIZ DE ADJACÊNCIA.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO.

        Returns:
            bool: RETORNA `TRUE` SE A REMOÇÃO FOR BEM-SUCEDIDA, CASO CONTRÁRIO `FALSE`.
        """
        if vertice < 0 or vertice >= self.vertices:
            logger.info(f"VÉRTICE {vertice} INVÁLIDO.")
            return False

        # REMOVE O VÉRTICE DA MATRIZ DE ADJACÊNCIA
        self.grafo.pop(vertice)

        # REMOVE TODAS AS ARESTAS ASSOCIADAS AO VÉRTICE
        for i in range(len(self.grafo)):
            self.grafo[i].pop(vertice)

        # DECREMENTA O NÚMERO DE VÉRTICES
        self.vertices -= 1

        return True

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

    def reduzido(self) -> list:
        """
        15) Fazer um método que retorne o grafo reduzido de um grafo direcionado no
        formato de uma matriz de adjacência.

        """
        pass


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
print(1)
