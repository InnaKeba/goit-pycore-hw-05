"""Створити дві функції:
Перша- generator_numbers(text: str), буде шукати всі дійсні числа у заданому тексті та повертати їх як генератор. 
Друга- sum_profit(text: str, func: Callable), для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику."""

import re
from collections.abc import Callable
def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел.
    pattern = r'\b\d+\.\d*\b'
    for match in re.finditer(pattern, text):
        yield float(match.group(0))
def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total      
# Приклад використання:
if __name__ == "__main__":  
    text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\n
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
    total_income = sum_profit(text, generator_numbers)
print(f"Загальний прибуток: {total_income} доларів")

  