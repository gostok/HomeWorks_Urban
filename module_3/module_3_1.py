# Задача "Счётчик вызовов":

calls = 0

def count_calls():
    global calls
    
    calls += 1
    

def string_info(string):
    count_calls()
    
    
    if string == str:
        
        return len(string), str(string).upper(), str(string).lower()
    else:
        return len(string), str(string).upper(), str(string).lower()
    
    
    
  

def is_contains(string, list_to_search):
    count_calls()
    string == str
    list_to_search == [str]
    
    if str(string).lower() in str(list_to_search).lower():
        return True
    else: 
        return False
    
    
    

print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # True
print(is_contains('cycle', ['recycling', 'cyclic'])) # False

print(f'Количество вызовов функций: {calls}')

