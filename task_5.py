import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, key, color="#000000"):  # Початковий колір чорний
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання рядів та позицій для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол до графа з кольором та міткою
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додаємо рямок до лівого нащадка
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо ліве піддерево
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додаємо рямок до правого нащадка
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо праве піддерево
    return graph

# Функція для генерації кольору залежно від кроку обхід
def generate_color(step, total_steps):
    r = int(255 * step / total_steps)  # Червоний колір збільшується з кожним кроком
    g = int(255 * (1 - step / total_steps))  # Зелений зменшується з кожним кроком
    b = random.randint(100, 255)  # Випадковий синій для додаткової варіативності
    return f"#{r:02X}{g:02X}{b:02X}"  # Повертаємо RGB у форматі hex

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створюємо орієнтований граф
    pos = {tree_root.id: (0, 0)}  # Позиція кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додаємо ряди та позиції до графа

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Отримуємо кольори для вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Отримуємо значення для міток

    plt.figure(figsize=(8, 5))  # Встановлюємо розмір фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Малюємо граф
    plt.show()

# Обхід в глибину (DFS) з використанням стека
def dfs(tree_root):
    stack = [tree_root]  # Використовуємо стек для DFS
    visited = set()
    step = 0
    total_steps = 0
    nodes = []  # Список для відстеження вузлів для оновлення кольорів

    # Підраховуємо загальну кількість вузлів для варіації кольорів
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    total_steps = count_nodes(tree_root)  # Отримуємо загальну кількість вузлів для обчислення кольору

    # Обхід в глибину
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color = generate_color(step, total_steps)  # Присвоюємо колір залежно від кроку
            nodes.append(node)  # Додаємо вузол до списку для пізнішого оновлення кольору
            step += 1

            # Додаємо правого та лівого нащадка до стека
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return nodes  # Повертаємо відвідані вузли для оновлення кольорів

# Обхід в ширину (BFS) з використанням черги
def bfs(tree_root):
    queue = [tree_root]  # Використовуємо чергу для BFS
    visited = set()
    step = 0
    total_steps = 0
    nodes = []  # Список для відстеження вузлів для оновлення кольорів

    # Підраховуємо загальну кількість вузлів для варіації кольорів
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    total_steps = count_nodes(tree_root)  # Отримуємо загальну кількість вузлів для обчислення кольору

    # Обхід в ширину
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            node.color = generate_color(step, total_steps)  # Присвоюємо колір залежно від кроку
            nodes.append(node)  # Додаємо вузол до списку для пізнішого оновлення кольору
            step += 1

            # Додаємо лівого та правого нащадка до черги
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return nodes  # Повертаємо відвідані вузли для оновлення кольорів

# Перетворення масиву (бінарної купи) на бінарне дерево
def array_to_heap_tree(arr, index=0):
    if index >= len(arr):
        return None
    
    root = Node(arr[index])
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    
    root.left = array_to_heap_tree(arr, left_child)
    root.right = array_to_heap_tree(arr, right_child)
    
    return root

# Приклад використання
heap = [0, 4, 1, 5, 10, 3]  # Проста бінарна купа

# Перетворення масиву на бінарне дерево
heap_tree_root = array_to_heap_tree(heap)

# Виконуємо DFS та візуалізуємо обхід
dfs(heap_tree_root)
draw_tree(heap_tree_root)

# Виконуємо BFS та візуалізуємо обхід
bfs(heap_tree_root)
draw_tree(heap_tree_root)
