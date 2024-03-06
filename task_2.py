from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо рядок у нижній регістр
    s = s.replace(" ", "").lower()
    
    # Створюємо чергу та додаємо символи рядка до неї
    char_queue = deque()
    for char in s:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))