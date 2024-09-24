from collections import deque


def dfs(adj, source, visited):
    visited[source] = True
    print(source, end=" ")

    for i in adj[source]:
        if not visited[i]:
            dfs(adj, i, visited)


def bfs(adj, source, visited):
    q = deque()

    visited[source] = True
    q.append(source)
    while q:
        curr = q.popleft()
        print(curr, end=" ")
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


def add_edge(adj, u, v):
    adj[u].append(v)


if __name__ == "__main__":
    V = 7
    adj = [[] for _ in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 0, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 1, 3)
    add_edge(adj, 2, 5)
    add_edge(adj, 3, 2)
    add_edge(adj, 3, 5)
    add_edge(adj, 3, 6)
    add_edge(adj, 4, 3)
    add_edge(adj, 4, 6)
    add_edge(adj, 6, 5)

    print("BFS: ")
    visited = [False] * V
    bfs(adj, 0, visited)

    print("\nDFS: ")
    visited = [False] * V
    dfs(adj, 0, visited)
