# створити функцію generator_numbers, яка буде аналізувати текст,
# ідентифікувати всі дійсні числа, що вважаються частинами доходів,
# і повертати їх як генератор. 
# Дійсні числа у тексті записані без помилок, відокремлені пробілами з обох боків.
# реалізувати функцію sum_profit, яка буде використовувати generator_numbers
# для підсумовування цих чисел і обчислення загального прибутку.

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")