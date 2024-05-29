class Graph:
    def __init__(self):
        self.graph = {}

    # Функция для добавления ребра в граф с указанием веса
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

        # Добавляем обратное ребро для неориентированного графа
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))

    # Поиск минимального остовного дерева методом Прима
    def prim_mst(self):
        mst = []
        # Берем начальную вершину
        start = list(self.graph.keys())[0]
        visited = set([start])  # Множество посещенных вершин
        edges = []  # Список для хранения ребер

        # Заполняем список ребрами, связанными с начальной вершиной
        for neighbor, weight in self.graph[start]:
            edges.append((weight, start, neighbor))

        while edges:
            # Сортируем список ребер и берем ребро с минимальным весом
            edges.sort()
            weight, u, v = edges.pop(0)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for neighbor, weight in self.graph[v]:
                    if neighbor not in visited:
                        edges.append((weight, v, neighbor))

        # Формируем строку с выводом минимального остовного дерева
        result = "Минимальное остовное дерево (метод Прима):\n"
        current_parent = None
        for u, v, weight in mst:
            if u != current_parent:
                if current_parent is not None:
                    result += "\n"
                current_parent = u
            result += f"({u}, {v}, {weight}) "
        return result

    # Поиск кратчайшего пути методом Дейкстры
    def dijkstra_shortest_path(self, start):
        # Объявляем расстояния до всех вершин бесконечностью
        distances = {top: float('infinity') for top in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            # Выбираем не посещенную вершину с минимальным расстоянием
            current_top = min(
                (top for top in self.graph if top not in visited), key=lambda top: distances[top])
            # Генератор, который перебирает вершины графа, но только те, которые еще не были посещены
            visited.add(current_top)

            for neighbour, weight in self.graph[current_top]:
                if neighbour not in visited:
                    new_distance = distances[current_top] + weight
                    if new_distance < distances[neighbour]:
                        distances[neighbour] = new_distance

        return distances


# Создаем граф
graph = Graph()
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(2, 4, 5)
graph.add_edge(2, 5, 6)
# graph.add_edge(3, 6, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 6, 9)

print(graph.prim_mst())

print("\nКратчайший путь (метод Дейкстры):")
start_top = int(input("Введите начальную вершину: "))
shortest_paths = graph.dijkstra_shortest_path(start_top)
for top, distance in shortest_paths.items():
    print(f"Кратчайший путь от вершины {start_top} до {top}: {distance}")
