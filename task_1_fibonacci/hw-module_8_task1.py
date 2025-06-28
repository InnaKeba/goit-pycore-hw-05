"""Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш
для зберігання і повторного використання вже обчислених значень чисел Фібоначчі"""

def caching_fibonacci():
    cache = {}  # Порожній словник для кешування обчислених значень
# Функція для обчислення чисел Фібоначчі
    def fibonacci(n): 
        if n in cache:
            return cache[n]
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result
    return fibonacci
# Приклад використання:
fib = caching_fibonacci()
for i in range(10):
    print(f"F({i}) = {fib(i)}") 