# Ориентированный граф - Обход в глубину и в ширину

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    # Функция для добавления ребра в граф
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Обход в глубину
    def dfs(self, current, target, visited, path):
        visited.add(current)
        path.append(current)

        if current == target:
            print(' '.join(map(str, path)) + "!")
        else:
            if current in self.graph:  # Проверяем наличие вершины в графе
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        self.dfs(neighbor, target, visited, path)

        path.pop()
        visited.remove(current)

    # Обход в ширину
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            if v in self.graph:  # Проверяем наличие вершины в графе
                for neighbor in self.graph[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)


# Создаем ориентированный граф
directed_graph = DirectedGraph()
directed_graph.add_edge(0, 1)
directed_graph.add_edge(0, 2)
directed_graph.add_edge(1, 3)
directed_graph.add_edge(2, 3)
directed_graph.add_edge(2, 4)
directed_graph.add_edge(2, 5)
# directed_graph.add_edge(3, 6)
directed_graph.add_edge(5, 4)
directed_graph.add_edge(5, 6)

print("Обход в глубину:")
directed_graph.dfs(0, 6, set(), [])

print("\nОбход в ширину:")
directed_graph.bfs(0)
