from collections import defaultdict 

class Grafo:

    def __init__(self): 
        self.graph = defaultdict(list) 

    def adiciona_aresta(self,u,v): 
        self.graph[u].append(v) 
        #self.graph[v-1].append(u) 

    def mostra_grafo(self):
        for i in range(len(self.graph)):
            print(f'{i}:', end='  ')
            for j in self.graph[i]:
                print(f'{j}  ||', end='  ')
            print('\n')
    
    def BFS(self, posInicio): 
        print("-----BFS-----")
    
        visited = [False] * (len(self.graph)) 
        lista = [] 
        lista.append(posInicio) 
        visited[posInicio] = True

        while lista: 

            posInicio = lista.pop(0) 
            print(f'{posInicio}  ->', end='  ') 

            for i in self.graph[posInicio]: 
                if visited[i] == False: 
                    lista.append(i) 
                    visited[i] = True
        print("Done!")

# g = Grafo()

# g.adiciona_aresta(0, 2) 
# g.adiciona_aresta(0, 3) 
# g.adiciona_aresta(0, 4) 
# g.adiciona_aresta(1, 2) 
# g.adiciona_aresta(1, 4) 
# g.adiciona_aresta(2, 4) 
# g.adiciona_aresta(3, 4) 
# g.adiciona_aresta(3, 5)
# g.adiciona_aresta(4, 5)
# g.adiciona_aresta(5, 1)

# g.mostra_grafo()

# g.BFS(0)