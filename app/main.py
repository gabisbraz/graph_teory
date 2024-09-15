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

# MOSTRA MATRIZ
grafo_direcionado.mostra_matriz()

# 1) GRAU DE ENTRADA DO VÉRTICE
grau_entrada_1 = grafo_direcionado.inDegree(vertice=1)
logger.info(f"GRAU DE ENTRADA DO VÉRTICE 1: {grau_entrada_1}")

# 2) GRAU DE SAÍDA DO VÉRTICE
grau_entrada_1 = grafo_direcionado.outDegree(vertice=1)
logger.info(f"GRAU DE SAÍDA DO VÉRTICE 1: {grau_entrada_1}")

# 3) VERIFICA SE UM VÉRTICE É FONTE
vertice_eh_fonte = grafo_direcionado.ehFonte(vertice=3)
logger.info(f"VÉRTICE 3 É FONTE? {vertice_eh_fonte}")

# 4) VERIFICA SE UM VÉRTICE É SORVEDOURO
vertice_eh_sorvedouro = grafo_direcionado.sorvedouro(vertice=3)
logger.info(f"VÉRTICE 3 É SORVEDOURO? {vertice_eh_sorvedouro}")

# 5) VERIFICA SE UM VÉRTICE É SORVEDOURO
grafo_eh_simetrico = grafo_direcionado.ehSimetrico()
logger.info(f"GRAFO É SIMÉTRICO? {grafo_eh_simetrico}")

# 6) LEITURA DO GRAFO A PARTIR DE UM ARQUIVO
grafo_direcionado_arquivo = TGrafo(vertices=0)
grafo_direcionado_arquivo.leArquivoGrafo(
    file_name="app/utils/graph_files/grafo_exemplo.txt"
)

# 9) REMOVENDO VÉRTICE DO GRAFO
grafo_direcionado.remove_vertice_direcionado(vertice=3)

# 11) VERIFICA SE UMA GRAFO É COMPLETO
eh_completo = grafo_direcionado.ehCompleto()
logger.info(f"GRAFO É COMPLETO? {eh_completo}")

# 12) COMPLEMENTO DO GRAFO
grafo_direcionado.complemento_dirigido()

# 14) CONEXIDADE DO GRAFO
conexidade = grafo_direcionado.categoria_conexidade()
logger.info(f"CONEXIDADE DO GRAFO: {conexidade}")

# 15) OBTEM GRAFO REDUZIDO
grafo_reduzido = grafo_direcionado.reduzido()
logger.info(f"GRAFO REDUZIDO: {grafo_reduzido}")

# 18) CONVERTE MATRIZ EM LISTA DE ADJACÊNCIA
matriz_para_lista = grafo_direcionado.matriz_para_lista_adjacencia()
logger.info(f"LISTA DE ADJACÊNCIA: {matriz_para_lista}")

# 21) VERIFICA SORVEDOURO --> LISTA DE ADJACÊNCIA
verifica_sorvedouro = grafo_direcionado.verifica_sorvedor(vertice=1)
logger.info(f"VÉRTICE 4 É SORVEDOURO? {verifica_sorvedouro}")

#############################################################################

# """
#     [0, 1, 1, 0]
#     [1, 0, 0, 1]
#     [1, 0, 0, 1]
#     [0, 1, 1, 0]
# """

# INICIALIZA A MATRIZ DE TAMANHO 4
grafo_nao_direcionado = TGrafoND(vertices=4)

# ADICIONA ARESTAS AO GRAFO
grafo_nao_direcionado.insereA(u=1, v=2)
grafo_nao_direcionado.insereA(u=1, v=3)
grafo_nao_direcionado.insereA(u=2, v=1)
grafo_nao_direcionado.insereA(u=2, v=4)
grafo_nao_direcionado.insereA(u=3, v=1)
grafo_nao_direcionado.insereA(u=3, v=4)
grafo_nao_direcionado.insereA(u=4, v=2)
grafo_nao_direcionado.insereA(u=4, v=3)

# IMPRIME A MATRIZ DE ADJACÊNCIA DO GRAFO CRIADO
grafo_nao_direcionado.show()

# REMOVE UM VÉRTICE DA LISTA DE ADJACÊNCIA
lista_adjacencia = grafo_nao_direcionado.remove_vertice(vertice=2)
logger.info(f"LISTA DE ADJACÊNCIA APÓS REMOÇÃO DO VÉRICE 2: {lista_adjacencia}")

# CALCULA O DFS - PERCURSO EM PROFUNDIDADE DA MATRIZ
percurso_profundidade_1 = grafo_nao_direcionado.percurso_profundidade(1)
logger.info(f"O PERCURSO PROFUNDIDADE DO GRAFO 1 É: {percurso_profundidade_1}")

# CALCULA O BFS - PERCURSO EM LARGURA DA MATRIZ
percurso_largura_1 = grafo_nao_direcionado.percurso_largura(1)
logger.info(f"O PERCURSO LARGURA DO GRAFO 1 É: {percurso_largura_1}")

############################################################################################
