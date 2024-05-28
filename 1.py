# Не ориентированный граф - Обход в глубину и в ширину

class Graph:
    def __init__(self):
        self.graph = {}

    # Функция для добавления ребра в граф
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        # Добавляем обратное ребро для не ориентированного графа
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

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
            print(queue, end=' ')
            v = queue.pop(0)
            print(v, end=' ')

            if v in self.graph:  # Проверяем наличие вершины в графе
                for neighbor in self.graph[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)


# Создаем граф
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
# graph.add_edge(3, 6)
graph.add_edge(5, 4)
graph.add_edge(5, 6)

print("Обход в глубину:")
graph.dfs(0, 6, set(), [])

print("\nОбход в ширину:")
graph.bfs(0)
