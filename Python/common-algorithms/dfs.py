def dfs(graph, v, visited):
    neighbors = graph[v]
    for n in neighbors:
        if n not in visited:
            visited.append(n)
            dfs(graph, n, visited)

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

    visited = ['A']
    dfs(graph, 'A', visited)

    for v in visited:
        print(v)