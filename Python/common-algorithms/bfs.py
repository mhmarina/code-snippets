def bfs(graph, v):
    q = [v]
    visited = []
    visited.append(v)

    while len(q) > 0:
        curr = q.pop(0)
        neighbors = graph[curr]

        for n in neighbors:
            if n not in visited:
                visited.append(n)
                q.append(n)
        
    for node in visited:
        print(node)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F', 'G'],
        'C': ['G', 'H'],
        'D': [],
        'E': [],
        'F': ['E', 'D'],
        'G': ['A'],
        'H': []
    }

    bfs(graph, 'A')