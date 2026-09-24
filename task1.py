import random
import timeit
import matplotlib.pyplot as plt
import sys

# Збільшуємо ліміт рекурсії для масивів великого розміру (напр., 500_000 елементів)
sys.setrecursionlimit(10_000)

def deterministic_quick_sort(arr):
    """
    Детермінований QuickSort, де опорним елементом завжди обирається середній.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    """
    Рандомізований QuickSort, де опорний елемент обирається випадковим чином.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_function, arr, runs=5):
    """
    Вимірює середній час виконання функції сортування за задану кількість прогонів.
    """
    # Функція-обгортка для timeit
    def run_sort():
        sort_function(arr.copy()) # Передаємо копію, щоб масив залишався невідсортованим для тесту

    total_time = timeit.timeit(run_sort, number=runs)
    return total_time / runs

if __name__ == '__main__':
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []

    print("Починаємо вимірювання часу виконання (це може зайняти хвилину-дві)...\n")

    for size in sizes:
        # Генерація масиву випадкових чисел
        arr = [random.randint(0, 1_000_000) for _ in range(size)]
        
        # Вимірювання для рандомізованого
        rand_time = measure_time(randomized_quick_sort, arr)
        rand_times.append(rand_time)
        
        # Вимірювання для детермінованого
        det_time = measure_time(deterministic_quick_sort, arr)
        det_times.append(det_time)
        
        # Вивід у термінал
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, marker='o', color='blue', label='Рандомізований QuickSort')
    plt.plot(sizes, det_times, marker='s', color='orange', label='Детермінований QuickSort')
    
    plt.title('Порівняння продуктивності: Рандомізований vs Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Середній час виконання (секунди)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()