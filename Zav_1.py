from queue import Queue

#Створити чергу заявок
queue = Queue()

def generate_request():
    for id in range (1, 6):
        new_appl = f"Заявка {id}"
        queue.put(new_appl)
        print (f"Створено нову заявку: {new_appl}")

#Обробити заявку    
def process_request():
    if not queue.empty():
        appl = queue.get()
        print (f"Обробка заявки: {appl}")
    else:
        print("Черга порожня. Очікуємо на нові заявки.")  

#Головний цикл програми:          
while True:
    choice = input("Хочете створити нову заявку? (так/ні):")
    if choice.lower() == 'так':
        generate_request()

    process_request()
    print(f"Оброблення заявки {id}")

    exit = input ("Вийти з програми? (так/ні): ")
    if exit.lower() == 'так':
        break




