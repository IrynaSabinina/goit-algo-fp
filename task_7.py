import random
import matplotlib.pyplot as plt
import numpy as np

# Функція для симуляції кидка двох кубиків
def roll_dice(num_rolls):
    # Массив для підрахунку кількості випадань кожної суми
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симулюємо кидки кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Перший кубик
        die2 = random.randint(1, 6)  # Другий кубик
        total_sum = die1 + die2  # Сума
        sums_count[total_sum] += 1
    
    # Обчислюємо ймовірності
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    return probabilities

# Теоретичні ймовірності для сум 2-12 при киданні двох кубиків
def theoretical_probabilities():
    # Визначаємо кількість можливих випадків для кожної суми
    possible_sums = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    
    total_outcomes = 6 * 6  # Всього можливих варіантів (6 x 6)
    probabilities = {k: v / total_outcomes for k, v in possible_sums.items()}
    return probabilities

# Симуляція кидків кубиків (наприклад, 1 мільйон кидків)
num_rolls = 1000000
simulated_probabilities = roll_dice(num_rolls)

# Теоретичні ймовірності
theoretical_prob = theoretical_probabilities()

# Виведемо ймовірності та порівняємо їх
print(f"Симульовані ймовірності (метод Монте-Карло):")
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {simulated_probabilities[sum_value]:.4f}")

print("\nТеоретичні ймовірності:")
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {theoretical_prob[sum_value]:.4f}")

# Графічне відображення ймовірностей
sums = list(range(2, 13))
simulated_values = [simulated_probabilities[sum_value] for sum_value in sums]
theoretical_values = [theoretical_prob[sum_value] for sum_value in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, simulated_values, alpha=0.7, label='Симульовані ймовірності', color='blue')
plt.plot(sums, theoretical_values, marker='o', color='red', label='Теоретичні ймовірності', linestyle='--')
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність")
plt.title("Порівняння симульованих і теоретичних ймовірностей (метод Монте-Карло)")
plt.legend()
plt.grid(True)
plt.show()
