import re


from my_class import AddtextsBook, Record, Name, Phone, Birthday, IncorrectDateFormat, IncorrectPhoneeFormat 

adress_book = AddtextsBook()
flag_exit = True

# Обробка помилок.
def input_error(func):
    def inner(*argsi,**kwargs): 
        #try:
        return func(*argsi,**kwargs)
        # except TypeError:
        #     print("Wrong command")
        #     return main()
        # except IndexError:
        #     print('Enter name and phone separated by a space!')
        #     return main()
        # except ValueError:
        #     print("Incorrect data") 
        #     return main()
        # except KeyError:
        #     print("Enter another name.")
        #     return main()
        # except AttributeError:
        #     print('Enter command.')
        #     return main()
        # except IncorrectDateFormat:
        #     print("Incorrect date format")
        #     return main()
        # except IncorrectPhoneeFormat:
        #     print("Incorrect phone format")
        #     return main()
    return inner

# Асистент вітається у відповідь.
@input_error
def hello(_):
    return "How can I help you?"

# Асистент додає ім'я та номер телефону якщо є до книги контактів.
@input_error
def add(uzer_input: str):
    text = uzer_input.split()
    if len(text) > 2:
        rec = Record(Name(text[1].capitalize()), [Phone(text[2])])
        flag = adress_book.add_record(rec)
        if flag:
            return f"Контакт {text[1].capitalize()} з номером {[phone.value for phone in rec.phones]} створений" 
    else:
        rec = Record(Name(text[1].capitalize())) # , [Phone(None)]
        flag = adress_book.add_record(rec)
        if flag:
            return f"Контакт {text[1].capitalize()} без номера телефону створений" 
    
    return f" "

# Додавання телефону до контакту 
def add_phone(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[2].capitalize()]
    rec.add_phone(Phone(text[3]))
    return f"До контакту {text[2].capitalize()} доданий новий телефон"

# Заміна телефону A на телефон B 
@input_error
def change(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[1].capitalize()]
    ret = f"{rec.name.value} : {[phone.value for phone in adress_book[rec.name.value].phones]}\n" + "Змінено на\n"
    rec.edit_phone(Phone(text[2]), Phone(text[3]))
    ret += f"{rec.name.value} : {[phone.value for phone in rec.phones]}"
    return ret
    
# Ассистент за ім'ям знаходить в контактах номер.
@input_error
def phone(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[1].capitalize()]
    try:
        return f"Номер телефону {text[1].capitalize()} це : {[phone.value for phone in rec.phones]}"
    except AttributeError:
        return f"Номер телефону {text[1].capitalize()} це :"
    

# Видаляє мобільний телефон
@input_error
def remove_phones(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[2].capitalize()]
    rec.remove_phone(Phone(text[3]))
    return f"Номер телефону {text[2].capitalize()} : {text[3]}\nВидалений"

# Ассистент показує всі контактні дані.
@input_error
def show_all(_):
    text = ''
    for key, record in adress_book.items():
        text += f"{key} : {[phone.value for phone in record.phones]}\n"
    return text if text else "Addtexts book is empty."

# Зупиняє роботу асистента.
@input_error
def exit_uzer(_):
    global flag_exit
    flag_exit = False
    return "Good bye!"

# Додає день народження 
@input_error
def add_birthday(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[2].capitalize()]
    rec.add_to_birthday(Birthday([text[3]]))
    return f"Birthday для {text[2].capitalize()} записаний"

# Показує скільки днів лишилося до дня народження
@input_error
def days_to_birthday(uzer_input: str):
    text = uzer_input.split()
    rec = adress_book[text[1].capitalize()]
    time = rec.days_to_birthday()
    return f"До дня народження {text[1].capitalize()} залишолося {time}"


# Список команд.
COMMANDS = {"add" : add, # Додає контакт в книгу контактів *
            "add phone" : add_phone, # Додає номер телефону до контакту *
            "add birthday" : add_birthday, # Додає день народження *
            "birthday" : days_to_birthday, # Показує скільки днів лишилося до дня народження *
            "change": change, # Заміна телефону A на телефон B *
            "close" : exit_uzer, # Виходить з асистента *
            "exit" : exit_uzer, # Виходить з асистента *
            "good bye" : exit_uzer, # Виходить з асистента *
            "hello": hello, # Виводить привітання *
            "phone" : phone, # Виводить номер телефону за ім'ям *
            "remove phone" : remove_phones, # Видаляє телефон *
            "show all" : show_all, # Показує книгу контактів *    
            }

# Знаходить команду.
@input_error    
def handler(uzer_input: str):
    text = uzer_input.lower()
    for keys in COMMANDS.keys():
        if re.findall(text, keys):
            return COMMANDS[keys]
        
# Знаходить команду.
@input_error    
def handler(uzer_input: str):
    text = uzer_input.lower()
    found_keywords = []
    for keyword in COMMANDS.keys():
        if text.find(keyword) != -1:
            found_keywords.append(keyword)
    comannds = list(filter(lambda x: len(x) == max(len(com) for com in found_keywords), found_keywords))
    print(comannds)
    return COMMANDS[comannds[0]]



@input_error
def main():
    while flag_exit: 
        uzer_input = input("-->")
        com = handler(uzer_input)
        print(com(uzer_input.lower()))
    

if __name__ == "__main__":
    main()