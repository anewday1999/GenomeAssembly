import graphviz
def parse(s, k):
    s = s[1:-1]
    #nodes
    nodes = []
    i = 0
    while i < len(s):
        if (s[i] != '(' and s[i] != ')' and s[i] != ' '):
            add = ''
            for j in range(k):
                add += s[i + j * 2]
            if add not in nodes:
                nodes.append(add)
            i += k * 2 - 2
        i += 1
    '''#nodes
    nodes = []
    i = 0
    while i < len(s):
        if (s[i] != '(' and s[i] != ')' and s[i] != ' '):
            add = s[i] + s[i + 2]
            if add not in nodes:
                nodes.append(add)
            i += 3
        i += 1'''
    #edges
    edges = []
    i = 0
    while i < len(s):
        if (s[i] != '(' and s[i] != ')' and s[i] != ' '):
            add = ''
            for j in range(k):
                add += s[i + j * 2]
            edges.append(add)
            i += k * 2 - 2
        i += 1

    listedges = []
    i = 0
    while i < len(edges):
        if (i % 2) == 0:
            listedges.append( [nodes.index(edges[i]) + 1, nodes.index(edges[i + 1]) + 1] )
        i += 1
    '''edges = []
    i = 0
    while i < len(s):
        if (s[i] != '(' and s[i] != ')' and s[i] != ' '):
            add = s[i] + s[i + 2]
            edges.append(add)
            i += 3
        i += 1

    listedges = []
    i = 0
    while i < len(edges):
        if (i % 2) == 0:
            listedges.append( [nodes.index(edges[i]) + 1, nodes.index(edges[i + 1]) + 1] )
        i += 1'''

    return nodes, listedges

def tograph(s, k):
    nodes, edges = parse(s, k)
    dot = graphviz.Digraph()
    cnt = 0
    for node in nodes:
        cnt += 1
        dot.node(f'{cnt}', f'{node}')
    cnt = 0
    for edge in edges:
        cnt += 1
        dot.edge(f'{edge[0]}',f'{edge[1]}', label=f'{nodes[edge[0]-1][0:1]}{nodes[edge[1]-1]}')
    dot.render('genome.gv', view=True)  

#input = '(((A C) (C C)) ((C C) (C T)) ((C T) (T T)) ((T T) (T T)) ((T T) (T C)) ((T C) (C G)) ((C G) (G T)) ((G T) (T A)) ((T A) (A A)) ((A A) (A C)) ((A C) (C C)))'
input = '(((A C C) (C C T)) ((C C T) (C T T)) ((C T T) (T T T)) ((T T T) (T T C)) ((T T C) (T C G)) ((T C G) (C G T)) ((C G T) (G T A)) ((G T A) (T A A)) ((T A A) (A A C)) ((A A C) (A C C))) '
k = 3
node, listedge = parse(input, k)
print('node ',node)
print('edge ',listedge)
tograph(input, k)
