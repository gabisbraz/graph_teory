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
