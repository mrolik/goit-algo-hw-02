import uuid
from queue import Queue


#Створити чергу заявок
queue = Queue()
counterID = 0.00

def generate_request():
    request_id = str(uuid.uuid4())
    new_request = {'id': request_id, 'data': 'Request information'}
    queue.put(new_request)
    print (f"Створено нову заявку: {new_request}")
        
#Обробити заявку    
def process_request():
    if not queue.empty():
        appl = queue.get()
        print (f"Обробка заявки: {new_request}")
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




