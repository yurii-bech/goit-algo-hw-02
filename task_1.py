import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації заявок
def generate_request():
    # Генеруємо унікальний номер для заявки (можна використати поточний час)
    request_id = int(time.time())
    # Додаємо заявку до черги
    request_queue.put(request_id)
    print(f"Заявка {request_id} створена")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється")
        # Імітуємо обробку заявки
        time.sleep(random.uniform(0.5, 2))
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга порожня")

# Головний цикл програми
if __name__ == "__main__":
    try:
        while True:
            # Генеруємо нову заявку
            generate_request()
            # Обробляємо заявки
            process_request()
            # Затримка між ітераціями
            time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершила роботу")