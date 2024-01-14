
from collections import deque

def check_if_palindrom (string:str):
    string = string.lower().replace(" ", "") #Забираємо пробіли і переводимо в нижній регістр
    characters = deque(string)

    while len(characters)>1:
        first_character = characters.popleft()
        last_character = characters.pop()

        if first_character != last_character:
            return False

    return True

string = "A man a plan a canal Panama"
result = check_if_palindrom (string)
print (f"Чи є рядок паліндромом: {result}")