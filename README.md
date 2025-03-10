Цей репозиторій містить рішення для різних завдань, що стосуються структур даних, алгоритмів пошуку та сортування, а також візуалізації та ймовірностей за допомогою методу Монте-Карло. Усі програми реалізовано на мові Python. Нижче наведено опис завдань та відповідні реалізації.

## Завдання 1: Структури даних. Сортування. Робота з однозв'язним списком
Опис:
Для реалізації однозв'язного списку необхідно:

Написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами.
Розробити алгоритм сортування для однозв'язного списку (наприклад, сортування вставками або злиттям).
Написати функцію, яка об'єднує два відсортовані однозв'язні списки в один відсортований список.
Кроки реалізації:
Реалізовано базову структуру для однозв'язного списку.
Створено функцію для реверсування списку.
Реалізовано алгоритм сортування вставками та злиттям.
Додано функцію для об'єднання двох відсортованих списків.
## Завдання 2: Бінарне дерево. Візуалізація обхідних операцій
Опис:
Це завдання передбачає побудову бінарного дерева та візуалізацію його обходів за допомогою методів:

Обхід у глибину.
Обхід у ширину.
Кожен крок обробки дерева має супроводжуватися зміною кольору вузлів, які змінюються від темних до світлих відтінків у залежності від порядку обходу.

Кроки реалізації:
Створено клас Node для представлення вузлів бінарного дерева.
Використовуються стек та черга для реалізації обходів в глибину (DFS) та в ширину (BFS) без використання рекурсії.
Реалізовано функцію для візуалізації дерева з кольоровими змінами вузлів на кожному кроці обходу.
## Завдання 3: Жадібні алгоритми та динамічне програмування
Опис:
Необхідно створити програму для вирішення задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету. Для цього реалізовано два підходи:

Жадібний алгоритм.
Алгоритм динамічного програмування.
Кроки реалізації:
Для кожного підходу розроблено відповідні функції:
greedy_algorithm: вибір страв, максимізуючи співвідношення калорій до вартості.
dynamic_programming: оптимальний набір страв для максимізації калорій при заданому бюджеті.
## Завдання 4: Кидки кубиків. Метод Монте-Карло
Опис:
Необхідно написати програму для імітації великої кількості кидків двох кубиків, обчислення сум чисел, що випали на кубиках, та визначення ймовірності кожної можливої суми (від 2 до 12). Використовувати метод Монте-Карло для підрахунку ймовірностей.

Кроки реалізації:
Створена симуляція, де два кубики кидаються велику кількість разів, і для кожного кидка визначається сума чисел.
Підраховані ймовірності для кожної можливої суми.
Побудовано графік порівняння симульованих ймовірностей та теоретичних розрахунків для різних сум.
## Завдання 5: Структури даних для бінарних дерев та візуалізація
Опис:
Створення та візуалізація бінарного дерева, включаючи різні обхідні стратегії, без використання рекурсії. Використовується бібліотека NetworkX для візуалізації дерева.

Кроки реалізації:
Побудова дерева за допомогою класу Node.
Реалізація алгоритмів обходу дерева в глибину (DFS) та в ширину (BFS).
Зміна кольору вузлів на кожному кроці обходу залежно від порядку відвідування.
## Завдання 6: Жадібні алгоритми та динамічне програмування для вибору страв
Опис:
Реалізація двох підходів для вибору їжі з найбільшою калорійністю в межах обмеженого бюджету:

Жадібний алгоритм для вибору страв на основі їх калорій та вартості.
Алгоритм динамічного програмування для пошуку оптимального набору страв.
Кроки реалізації:
Реалізація обох підходів для максимізації калорійності.
Для кожного підходу створено функції, що працюють з вхідними даними (цінами та калоріями їжі).
## Завдання 7: Імітація кидків кубиків та обчислення ймовірностей
Опис:
Написати програму, яка імітує кидки двох кубиків та визначає ймовірності для кожної можливої суми, що випала на кубиках. Використовується метод Монте-Карло для підрахунку ймовірностей різних сум (від 2 до 12).

## Кроки реалізації:
Симуляція кидків кубиків з підрахунком кількості кожної суми.
Побудова таблиці ймовірностей.
Порівняння результатів з теоретичними значеннями ймовірностей.
Побудова графіка для візуалізації результатів.
Для запуску кожного з розв'язків:
Склонуйте репозиторій.
Встановіть необхідні залежності
Запустіть відповідний Python файл для кожного завдання.
Використовувані бібліотеки:
random
matplotlib
networkx
numpy
Ці бібліотеки можуть бути встановлені за допомогою pip, якщо вони не присутні у вашій системі.
