import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Рекурсивна функція для додавання ребер і позицій для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додавання вузла в граф з кольором та міткою
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додавання ребра до лівого дочірнього вузла
            l = x - 1 / 2 ** layer  # Обчислення x-позиції для лівого дочірнього вузла
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо лівий піддерево
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додавання ребра до правого дочірнього вузла
            r = x + 1 / 2 ** layer  # Обчислення x-позиції для правого дочірнього вузла
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо правий піддерево
    return graph

# Функція для відображення дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створення орієнтованого графа
    pos = {tree_root.id: (0, 0)}  # Позиція кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додаємо ребра та позиції для візуалізації

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Отримуємо кольори для вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Отримуємо значення вузлів для міток

    plt.figure(figsize=(8, 5))  # Встановлення розміру фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Малюємо граф
    plt.show()

# Функція для перетворення масиву (бінарної купи) в дерево
def array_to_heap_tree(arr, index=0):
    if index >= len(arr):  # Базовий випадок: відсутній вузол, якщо індекс перевищує довжину масиву
        return None
    
    root = Node(arr[index])  # Створюємо новий вузол для поточного значення
    left_child = 2 * index + 1  # Індекс лівого дочірнього вузла
    right_child = 2 * index + 2  # Індекс правого дочірнього вузла
    
    root.left = array_to_heap_tree(arr, left_child)  # Рекурсивно будуємо ліве піддерево
    root.right = array_to_heap_tree(arr, right_child)  # Рекурсивно будуємо праве піддерево
    
    return root

# Приклад використання
heap = [0, 4, 1, 5, 10, 3]  # Простіший масив бінарної купи

# Перетворюємо масив на бінарне дерево
heap_tree_root = array_to_heap_tree(heap)

# Відображаємо дерево
draw_tree(heap_tree_root)
