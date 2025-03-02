import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        # Використання піраміди (бінарної купи) для пошуку найкоротших шляхів
        heap = []
        heapq.heappush(heap, (0, start))  # (відстань, вершина)

        shortest_paths = {start: (0, None)}  # Відстань до початкової вершини дорівнює 0
        visited = set()

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight

                if neighbor not in shortest_paths or distance < shortest_paths[neighbor][0]:
                    shortest_paths[neighbor] = (distance, current_vertex)
                    heapq.heappush(heap, (distance, neighbor))

        return shortest_paths

    def print_shortest_paths(self, shortest_paths, start):
        print(f"Найкоротші шляхи від вершини {start}:")
        for vertex, (distance, _) in shortest_paths.items():
            print(f"До вершини {vertex}: відстань = {distance}")

    def get_path(self, shortest_paths, start, target):
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = shortest_paths.get(current, (None, None))[1]
        path.reverse()  # Шлях будується від кінця до початку, тож потрібно перевернути
        return path

# Демонстрація роботи алгоритму

graph = Graph()

# Додавання ребер графа (зваженого графа)
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Початкова вершина
start_vertex = 'A'

# Обчислення найкоротших шляхів
shortest_paths = graph.dijkstra(start_vertex)

# Виведення результатів
graph.print_shortest_paths(shortest_paths, start_vertex)

# Приклад відновлення шляху
target_vertex = 'D'
path = graph.get_path(shortest_paths, start_vertex, target_vertex)
print(f"Шлях до вершини {target_vertex}: {' -> '.join(path)}")
