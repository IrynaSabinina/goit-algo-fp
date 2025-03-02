# Продукти з їх вартостями та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм для максимізації співвідношення калорій до вартості
def greedy_algorithm(budget):
    # Обчислюємо співвідношення калорій до вартості для кожного елементу
    ratios = [(item, details["calories"] / details["cost"]) for item, details in items.items()]
    # Сортуємо елементи за співвідношенням калорій до вартості в порядку спадання
    ratios.sort(key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    # Вибираємо страви, поки не вийдемо за межі бюджету
    for item, ratio in ratios:
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        
        if total_cost + cost <= budget:  # Якщо можемо дозволити собі цей продукт
            total_cost += cost
            total_calories += calories
            selected_items.append(item)
    
    return selected_items, total_cost, total_calories

# Алгоритм динамічного програмування (за типом задачі "Задача рюкзака")
def dynamic_programming(budget):
    # Ініціалізація масиву dp, де dp[i] зберігає максимальні калорії, які можна отримати з бюджетом i
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]  # Список вибраних страв для кожного бюджету

    # Перебір кожної страви
    for item, details in items.items():
        cost = details["cost"]
        calories = details["calories"]
        
        # Перебираємо бюджети від більшого до меншого, щоб уникнути перезапису результатів поточної ітерації
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[current_budget - cost] + [item]

    return selected_items[budget], dp[budget]

# Приклад використання
budget = 100  # Встановлюємо бюджет на 100 одиниць

# Використовуємо Жадібний алгоритм
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_items}")
print(f"Загальна вартість: {greedy_cost}")
print(f"Загальна калорійність: {greedy_calories}\n")

# Використовуємо Алгоритм динамічного програмування
dp_items, dp_calories = dynamic_programming(budget)
print("Алгоритм динамічного програмування:")
print(f"Вибрані страви: {dp_items}")
print(f"Загальна калорійність: {dp_calories}")
