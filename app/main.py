import sys
from pathlib import Path

from loguru import logger

from utils.graph_classes.grafo_direcionado import TGrafo
from utils.graph_classes.grafo_nao_direcionado import TGrafoND

"""
   1  2  3  4  5
1  0  1  1  0  0
2  1  0  0  1  0
3  1  0  0  0  1
4  0  0  0  1  0
5  0  1  1  1  0
"""

# INICIALIZA A MATRIZ DE TAMANHO 5
grafo_direcionado = TGrafo(vertices=5)

# ADICIONA ARESTAS AO GRAFO
grafo_direcionado.add_aresta(linha=1, coluna=2)
grafo_direcionado.add_aresta(linha=1, coluna=3)
grafo_direcionado.add_aresta(linha=2, coluna=1)
grafo_direcionado.add_aresta(linha=2, coluna=4)
grafo_direcionado.add_aresta(linha=3, coluna=1)
grafo_direcionado.add_aresta(linha=3, coluna=5)
grafo_direcionado.add_aresta(linha=4, coluna=4)
grafo_direcionado.add_aresta(linha=5, coluna=2)
grafo_direcionado.add_aresta(linha=5, coluna=3)
grafo_direcionado.add_aresta(linha=5, coluna=4)


# GRAU DE ENTRADA DO VÉRTICE
grau_entrada_1 = grafo_direcionado.inDegree(vertice=1)
logger.info(f"GRAU DE ENTRADA DO VÉRTICE 1: {grau_entrada_1}")

grau_entrada_4 = grafo_direcionado.inDegree(vertice=4)
logger.info(f"GRAU DE ENTRADA DO VÉRTICE 4: {grau_entrada_4}")

# GRAU DE SAÍDA DO VÉRTICE
grau_entrada_1 = grafo_direcionado.outDegree(vertice=1)
logger.info(f"GRAU DE SAÍDA DO VÉRTICE 1: {grau_entrada_1}")

grau_entrada_4 = grafo_direcionado.outDegree(vertice=4)
logger.info(f"GRAU DE SAÍDA DO VÉRTICE 4: {grau_entrada_4}")

# VERIFICA SE UM VÉRTICE É FONTE
vertice_eh_fonte = grafo_direcionado.ehFonte(vertice=3)
logger.info(f"VÉRTICE 3 É FONTE? {vertice_eh_fonte}")

# VERIFICA SE O GRAFO É SIMÉTRICO
grafo_eh_simetrico = grafo_direcionado.ehSimetrico()
logger.info(f"GRAFO É SIMÉTRICO? {grafo_eh_simetrico}")

# VERIFICA SE UM VÉRTICE É SORVEDOURO
vertice_eh_sorvedouro = grafo_direcionado.sorvedouro(vertice=3)
logger.info(f"VÉRTICE 3 É SORVEDOURO? {vertice_eh_sorvedouro}")

# VERIFICA SE UM VÉRTICE É SORVEDOURO
grafo_eh_simetrico = grafo_direcionado.ehSimetrico()
logger.info(f"GRAFO É SIMÉTRICO? {grafo_eh_simetrico}")

# LEITURA DO GRAFO A PARTIR DE UM ARQUIVO
grafo_direcionado_arquivo = TGrafo(vertices=0)
grafo_direcionado_arquivo.leArquivoGrafo(
    file_name="app/utils/graph_files/grafo_exemplo.txt"
)

#############################################################################

grafo_nao_direcionado = TGrafoND(vertices=4)

# INICIALIZA A MATRIZ DE TAMANHO 4
grafo_1 = TGrafo(vertices=4)

"""
    [0, 1, 1, 0]
    [1, 0, 0, 1]
    [1, 0, 0, 1]
    [0, 1, 1, 0]
"""

# ADICIONA ARESTAS AO GRAFO
grafo_1.add_aresta(linha=1, coluna=2)
grafo_1.add_aresta(linha=1, coluna=3)
grafo_1.add_aresta(linha=2, coluna=1)
grafo_1.add_aresta(linha=2, coluna=4)
grafo_1.add_aresta(linha=3, coluna=1)
grafo_1.add_aresta(linha=3, coluna=4)
grafo_1.add_aresta(linha=4, coluna=2)
grafo_1.add_aresta(linha=4, coluna=3)

# IMPRIME A MATRIZ DE ADJACÊNCIA DO GRAFO CRIADO
grafo_1.mostra_matriz()

# CALCULA O DFS - PERCURSO EM PROFUNDIDADE DA MATRIZ
percurso_profundidade_1 = grafo_1.percurso_profundidade(1)
logger.info(f"O PERCURSO PROFUNDIDADE DO GRAFO 1 É: {percurso_profundidade_1}")

# CALCULA O BFS - PERCURSO EM LARGURA DA MATRIZ
percurso_largura_1 = grafo_1.percurso_largura(1)
logger.info(f"O PERCURSO LARGURA DO GRAFO 1 É: {percurso_largura_1}")

############################################################################################

# INICIALIZA A MATRIZ DE TAMANHO 4
grafo_2 = TGrafo(vertices=8)

"""
    [0, 1, 1, 0, 1, 0, 0, 0]
    [0, 0, 0, 1, 1, 0, 0, 0]
    [0, 0, 0, 0, 0, 1, 1, 0]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 1, 0, 1, 0]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0, 0, 0, 0]
"""

# ADICIONA ARESTAS AO GRAFO
grafo_2.add_aresta(linha=1, coluna=2)
grafo_2.add_aresta(linha=1, coluna=3)
grafo_2.add_aresta(linha=1, coluna=5)
grafo_2.add_aresta(linha=2, coluna=4)
grafo_2.add_aresta(linha=2, coluna=5)
grafo_2.add_aresta(linha=3, coluna=6)
grafo_2.add_aresta(linha=3, coluna=7)
grafo_2.add_aresta(linha=4, coluna=8)
grafo_2.add_aresta(linha=5, coluna=8)
grafo_2.add_aresta(linha=6, coluna=5)
grafo_2.add_aresta(linha=6, coluna=7)
grafo_2.add_aresta(linha=7, coluna=8)

# IMPRIME A MATRIZ DE ADJACÊNCIA DO GRAFO CRIADO
grafo_2.mostra_matriz()

# CALCULA O DFS - PERCURSO EM PROFUNDIDADE DA MATRIZ
percurso_profundidade_2 = grafo_2.percurso_profundidade(1)
logger.info(f"O PERCURSO PROFUNDIDADE DO GRAFO 2 É: {percurso_profundidade_2}")

# CALCULA O BFS - PERCURSO EM LARGURA DA MATRIZ
percurso_largura_2 = grafo_2.percurso_largura(1)
logger.info(f"O PERCURSO LARGURA DO GRAFO 2 É: {percurso_largura_2}")

############################################################################################

# VERIFICA SE UM VÉRTICE É FONTE
vertice_eh_fonte = grafo_direcionado.ehFonte(vertice=3)
logger.info(f"O VÉRTICE 3 É FONTE? {vertice_eh_fonte}")

# LEITURA DO GRAFO A PARTIR DE UM ARQUIVO E CONSTRUÇÃO DA MATRIZ DE ADJACÊNCIA
grafo_direcionado_arquivo = TGrafo(vertices=0)
grafo_direcionado_arquivo.leArquivoGrafo(file_name="app/utils/graph_files/grafo_exemplo.txt")
grafo_direcionado_arquivo.mostra_matriz()

# VERIFICA SE O GRAFO É COMPLETO
grafo_eh_completo = grafo_direcionado.ehCompleto()
logger.info(f"O GRAFO É COMPLETO? {grafo_eh_completo}")

# VERIFICA SE DOIS GRAFOS SÃO IGUAIS
grafo1 = TGrafo(vertices=4)
grafo1.add_aresta(1, 2)
grafo1.add_aresta(2, 3)

grafo2 = TGrafo(vertices=4)
grafo2.add_aresta(1, 2)
grafo2.add_aresta(2, 3)

sao_iguais = grafo1.saoIguais(grafo2)
logger.info(f"OS GRAFOS SÃO IGUAIS? {sao_iguais}")

