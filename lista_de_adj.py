class Grafo:
    def __init__(self):
        """
        INICIALIZA O GRAFO COMO UM DICIONÁRIO VAZIO.
        """
        self.grafo = {}
    
    def add_vertice(self, vertice):
        """
        ADICIONA UM VÉRTICE AO GRAFO.

        Args:
            vertice (str): O IDENTIFICADOR DO VÉRTICE.
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def add_aresta(self, u, v):
        """
        ADICIONA UMA ARESTA DIRECIONADA DO VÉRTICE U PARA O VÉRTICE V.

        Args:
            u (str): O IDENTIFICADOR DO VÉRTICE DE ORIGEM.
            v (str): O IDENTIFICADOR DO VÉRTICE DE DESTINO.
        """
        if u in self.grafo and v in self.grafo:
            self.grafo[u].append(v)
        else:
            print(f"Vértices {u} ou {v} não encontrados no grafo.")
    
    def mostra_lista(self):
        """
        EXIBE A LISTA DE ADJACÊNCIA DO GRAFO NO FORMATO DESEJADO.
        """
        print("LISTA ORIGINAL:")
        for vertice, vizinhos in self.grafo.items():
            print(f'{vertice} -> ', end='')
            if vizinhos:
                print(' -> '.join(vizinhos), end=' ->')
            print()

    def inverter_vizinhos(self):
        """
        #19) Escreva um método que receba um grafo armazenado em lista de adjacência e inverta a lista de adjacência de todos os vértices do grafo.  Por exemplo, se os 4 vizinhos de um certo vértice u aparecem na lista adj[u] na ordem v, w, x, y, então depois da aplicação do método a lista deve conter os mesmos vértices na ordem y, x, w, v. Obs.: Vizinhos são todos os vértices ligados ao vértice u.
        ---
        INVERTE A LISTA DE VIZINHOS DE TODOS OS VÉRTICES NO GRAFO E EXIBE ESSA LISTA.
        """
        print("\nLISTA COM VIZINHOS INVERTIDOS:")
        for vertice, vizinhos in self.grafo.items():
            print(f'{vertice} -> ', end='')
            if vizinhos:
                vizinhos_invertidos = list(reversed(vizinhos))
                print(' -> '.join(vizinhos_invertidos), end=' ->')
            print()

    def eh_simetrico(self) -> int:
        """
        #22) Escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico e 0 caso contrário. O método deve ser implementado  para a classe TGrafo que utiliza lista de adjacência.
        ---
        VERIFICA SE O GRAFO É SIMÉTRICO.

        PARA SER CONSIDERADO SIMÉTRICO, TODAS AS ARESTAS (U, V) DEVEM TER UMA ARESTA 
        CORRESPONDENTE (V, U).

        RETURNS:
            INT: 1 SE O GRAFO FOR SIMÉTRICO, 0 CASO CONTRÁRIO.
        """
        for u, vizinhos in self.grafo.items():
            for v in vizinhos:
                if u not in self.grafo.get(v, []):
                    return 0
        return 1

    def remove_vertice(self, vertice):
        """
        #25) Fazer um método que permita remover um vértice do Grafo (dirigido). Não se esqueça de remover as arestas associadas.
        ---
        REMOVE UM VÉRTICE DO GRAFO E TODAS AS ARESTAS ASSOCIADAS.

        Args:
            vertice (str): O IDENTIFICADOR DO VÉRTICE A SER REMOVIDO.
        """
        if vertice not in self.grafo:
            raise ValueError(f"O vértice {vertice} não está no grafo.")
        
        # REMOVE TODAS AS REFERÊNCIAS AO VÉRTICE NAS LISTAS DE ADJACÊNCIA
        for v in list(self.grafo.keys()):  # Cria uma lista para evitar modificação durante iteração
            if vertice in self.grafo[v]:
                self.grafo[v].remove(vertice)
        
        # REMOVE O VÉRTICE E SUA LISTA DE ADJACÊNCIA
        del self.grafo[vertice]
        print(f"Vértice {vertice} removido com sucesso!")

# EXEMPLO DE USO
g = Grafo()

# ADICIONA VÉRTICES AO GRAFO
g.add_vertice('1')
g.add_vertice('2')
g.add_vertice('3')
g.add_vertice('4')
g.add_vertice('5')

# ADICIONA AS ARESTAS AO GRAFO
g.add_aresta('1', '2')
g.add_aresta('1', '3')
g.add_aresta('2', '4')
g.add_aresta('3', '2')
g.add_aresta('3', '4')
g.add_aresta('4', '5')
g.add_aresta('5', '1')

# EXIBE A LISTA DE ADJACÊNCIA E SUA VERSÃO INVERTIDA
g.mostra_lista()
g.inverter_vizinhos()

# VERIFICAR SE O GRAFO É SIMÉTRICO
if g.eh_simetrico():
    print("\nO grafo é simétrico.")
else:
    print("\nO grafo não é simétrico.")

# REMOVER O VÉRTICE '3'
print("\nRemovendo o vértice '3':")
g.remove_vertice('3')

# EXIBIR NOVAMENTE A LISTA APÓS REMOÇÃO
print("\nLista de adjacência após remoção do vértice:")
g.mostra_lista()








