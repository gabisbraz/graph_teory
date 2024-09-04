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
        Adiciona uma aresta direcionada ao grafo entre os vértices
        `linha` e `coluna`.

        Args:
            linha (int): Índice da linha (vértice de partida).
            coluna (int): Índice da coluna (vértice de chegada).
        """
        # Adiciona a aresta, definindo o valor 1 na posição específica da matriz
        self.grafo[linha][coluna] = 1

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
        grau = sum(self.grafo[vertice])
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

    def ehSimetrico(self) -> int:
        """
        Verifica se a matriz de adjacência do grafo é simétrica. Um grafo
        é considerado simétrico se, para todas as arestas, o vértice `i`
        estiver conectado ao vértice `j`, então o vértice `j` também deve
        estar conectado ao vértice `i`.

        Returns:
            int: Retorna 1 se a matriz é simétrica (grafo não direcionado),
            caso contrário retorna 0 (grafo direcionado).
        """
        for i in range(self.vertices):
            for j in range(i, self.vertices):
                if self.grafo[i][j] != self.grafo[j][i]:
                    return 0
        return 1

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
    
    def eh_completo_direcionado(self) -> int:
        """
        Verifica se o grafo direcionado é completo. Um grafo direcionado
        é considerado completo se, para todos os pares de vértices distintos `(i, j)`,
        existir uma aresta de `i` para `j` e uma aresta de `j` para `i`.

        Returns:
            int: Retorna 1 se o grafo é completo, caso contrário retorna 0.
        """
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and (self.grafo[i][j] == 0 or self.grafo[j][i] == 0):
                    return 0
        return 1

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
            if not bfs(i, self.grafo):  # Verifica se todos os vértices são acessíveis a partir de `i`
                break
        else:
            return 3  # Se todos os vértices são fortemente conectados

        # Cria o grafo inverso (transposto)
        grafo_transposto = [[self.grafo[j][i] for j in range(self.vertices)] for i in range(self.vertices)]
        
        # Verifica a conectividade fraca (C1)
        for i in range(self.vertices):
            if not bfs(i, [[1 if self.grafo[j][i] or grafo_transposto[j][i] else 0 for i in range(self.vertices)] for j in range(self.vertices)]):
                break
        else:
            return 1  # Se o grafo é fracamente conexo

        # Verifica se o grafo é unicamente conexo (C2)
        for i in range(self.vertices):
            if not bfs(i, self.grafo) or not bfs(i, grafo_transposto):
                return 0  # Desconexo
        
        return 2  # Unicamente conexo (C2)

    
class TGrafoND:
    def __init__(self, vertices: int):
        """
        Inicializa o grafo não direcionado com uma matriz de adjacência
        de tamanho `vertices` x `vertices`, permitindo rótulos (valores float)
        nas arestas.

        Args:
            vertices (int): Número de vértices do grafo.
        """
        self.vertices = vertices
        self.grafo = [[0.0] * self.vertices for _ in range(self.vertices)]

    def add_aresta(self, linha: int, coluna: int, peso: float):
        """
        Adiciona uma aresta não direcionada ao grafo entre os
        vértices `linha` e `coluna`, com um rótulo `peso`.

        Args:
            linha (int): Índice da linha (um dos vértices).
            coluna (int): Índice da coluna (o outro vértice).
            peso (float): Valor associado à aresta (rótulo).
        """
        self.grafo[linha][coluna] = peso
        self.grafo[coluna][linha] = peso

    def mostra_matriz(self):
        """
        Exibe a matriz de adjacência do grafo não direcionado.
        """
        print("A MATRIZ DE ADJACÊNCIA É: ")
        for i in range(self.vertices):
            print(self.grafo[i])

    def eh_completo_n_direcionado(self) -> int:
        """
        Verifica se o grafo não direcionado é completo. Um grafo não direcionado
        é considerado completo se, para todos os pares de vértices distintos `(i, j)`,
        existir uma aresta entre `i` e `j`.

        Returns:
            int: Retorna 1 se o grafo é completo, caso contrário retorna 0.
        """
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.grafo[i][j] == 0:
                    return 0
        return 1

    def complemento(self) -> list:
        """
        Calcula o grafo complementar não direcionado, ou seja, um grafo que possui as
        arestas invertidas em relação ao grafo original.

        Returns:
            list: A matriz de adjacência do grafo complementar não direcionado.
        """
        complemento_grafo = [[0.0 if i != j and self.grafo[i][j] != 0 else 1.0 for j in range(self.vertices)] for i in range(self.vertices)]
        return complemento_grafo


# TESTES

# INSTANCIANDO O OBJETO
grafo = TGrafo(4)
grafo.add_aresta(0, 1)
grafo.add_aresta(1, 2)
grafo.add_aresta(2, 3)
grafo.add_aresta(3, 0)
grafo.mostra_matriz()
print(grafo.inDegree(2))  # Exemplo de uso
print(grafo.ehFonte(0))  # Exemplo de uso
print(grafo.remove_vertice(2))  # Exemplo de uso
print(grafo.eh_completo_direcionado())

# INSTANCIANDO O OBJETO DO GRAFO NÃO DIRECIONADO
grafo_nd = TGrafoND(4)
grafo_nd.add_aresta(0, 1, 1.5)
grafo_nd.add_aresta(1, 2, 2.5)
grafo_nd.add_aresta(2, 3, 3.5)
grafo_nd.add_aresta(3, 0, 4.5)
grafo_nd.mostra_matriz()
print(grafo_nd.eh_completo_n_direcionado())  # Esperado: 0

# Exemplo de uso
grafo = TGrafo(4)
grafo.add_aresta(0, 1)
grafo.add_aresta(1, 0)
grafo.add_aresta(1, 2)
grafo.add_aresta(2, 1)
grafo.add_aresta(2, 3)
grafo.add_aresta(3, 2)
grafo.add_aresta(3, 0)
grafo.add_aresta(0, 3)

print(grafo.categoria_conexidade())  # Deve retornar 3 (C3) - fortemente conexo
