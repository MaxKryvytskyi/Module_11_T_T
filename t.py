# from datetime import datetime


# date = "2020-3-25"
# name = "Oleg"



# def days_to_birthday(date):
#     if type(date) == str:
#         new_date = datetime.strptime(date, r'%Y-%m-%d')
#         current_datetime = datetime.now()
#         new_date = new_date.replace(year=current_datetime.year)
#         days_birthday = new_date - current_datetime 

#     else:
#         days_birthday = date - datetime.now() 

#     if days_birthday.days >= 0:
#         hours = int(days_birthday.seconds // 3600)
#         minutes = int((days_birthday.seconds % 3600) // 60)
#         seconds = int(days_birthday.seconds % 60)
#         print(f"До дня народження {name} : {days_birthday.days} days, {hours} hours, {minutes} minutes, {seconds} seconds ")
#     else:
#         correct_date = new_date.replace(year=current_datetime.year+1)
#         days_to_birthday(correct_date)

# days_to_birthday(date)




# phone =  "+380123456789" #  "0123456789" "123456789" 

# def phones(phone: str):
#     correct_phone = ""
#     for i in phone: 
#         if i in "+0123456789":
#             correct_phone += i

#     if len(correct_phone) == 13 or len(correct_phone) == 10 or len(correct_phone) == 9: # "+380123456789" "0123456789" "123456789" 
#         print(correct_phone)
#         print(len(correct_phone))

# phones(phone)


# birthday = "2000-03-30"

# s = datetime.strptime(birthday, r'%Y-%m-%d')

# def days_to_birthday(s):
#     current_datetime = datetime.now()
#     new_date = s.replace(year=current_datetime.year)
#     days_birthday = new_date - current_datetime
#     if days_birthday.days >= 0:
#         hours = int(days_birthday.seconds // 3600)
#         minutes = int((days_birthday.seconds % 3600) // 60)
#         seconds = int(days_birthday.seconds % 60)
#         return f"{days_birthday.days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
#     else:
#         date = s.replace(year=current_datetime.year+1)
#         days_birthday = date - current_datetime
#         hours = int(days_birthday.seconds // 3600)
#         minutes = int((days_birthday.seconds % 3600) // 60)
#         seconds = int(days_birthday.seconds % 60)
#         return f"{days_birthday.days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# print(days_to_birthday(s))





class Iterable:

    current_page = 1
    def __init__(self, step, max_step):
        self.step = step
        self.max_step = max_step
        self.current_value = ""
        self.count = 0

    def __next__(self):
        if self.count < self.max_step:
            self.current_value = f'page : {self.current_page}\n'
            
            for _ in range(self.step):
                self.current_value += str(self.count) + "\n"
                self.count +=1
            self.current_page += 1
            return self.current_value.strip()
        raise StopIteration


class CustomIterator:

    def __init__(self, step, max_step):
        self.step = step
        self.max_step = max_step

    def __iter__(self):
        return Iterable(self.step, self.max_step)


c = CustomIterator(3, 20)
for i in c:
    print(i)



# >>> show all 3
# page 1
# contact1
# contact2
# contact3
# page 2
# contact4
# contact5
# contact6
# page 3
# contact 7




# class Iterable:
#     current_page = 1

#     def __init__(self, step, max_step):
#         self.step = step
#         self.max_step = max_step
#         self.current_value = ""
#         self.count = 0

#     def __next__(self):

#         if self.count < self.max_step:
#             self.current_value = f'page: {self.current_page}\n'
#             for _ in range(self.step):
#                 self.current_value += str(self.count) + "\n"
#                 self.count += 1
#             self.current_page += 1
#             return self.current_value.strip()
#         raise StopIteration


# class CustomIterator:

#     def __init__(self, step, max_step):
#         self.step = step
#         self.max_step = max_step

#     def __iter__(self):
#         return Iterable(self.step, self.max_step)


# c = CustomIterator(3, 20)
# for i in c:
#     print(i)














# from collections import UserDict

# class RecordDict(UserDict):
#     def __iter__(self):
#         self._keys = iter(self.data.keys())
#         return self

#     def __next__(self):
#         key = next(self._keys)
#         return self.data[key]



# d = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5", 
#      "key6": "value6", "key7": "value7", "key8": "value8", "key9": "value9", "key10": "value10", 
#      "key11": "value11", "key12": "value12", "key13": "value13", "key14": "value14", "key15": "value15"
#      }
# record_dict = RecordDict(d)

# for value in record_dict:
#     print(value)

# def iterate_dict_in_chunks(dictionary, chunk_size):
#     keys = list(dictionary.keys())  # Отримуємо список ключів словника
#     values = list(dictionary.values())  # Отримуємо список значень словника

#     for i in range(0, len(keys), chunk_size):
#         chunk_keys = keys[i:i+chunk_size]  # Зріз ключів
#         chunk_values = values[i:i+chunk_size]  # Зріз значень

#         chunk_dict = {v for _, v in zip(chunk_keys, chunk_values)}  # Створюємо словник зі зрізу ключів та значень
#         print(chunk_dict)  # Виводимо частину словника


# # my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}

# iterate_dict_in_chunks(d, 3)

# def get_formatted_commands(commands_list):
#     output = ""
#     count = 0

#     for _, v in commands_list.items():
#         if count == 0:
#             output += "{:^100}\n".format(" " + "_"*100 + " ")
#         else:
#             output += "{:^100}\n".format("|" + "_"*100 + "|")
#         output += "|{:^100}|\n".format(f" COMMANDS - {_}")
#         output += "{:^100}\n".format("|" + "_"*100 + "|")
#         output += "|{:^100}|\n".format(v[0])
#         output += "|{:^100}|\n".format(v[1])
#         output += "{:^100}\n".format("|" + "_"*100 + "|")
#         count += 1

#     return output

# my_commands = {
#     "command1": ["Description 1", "Details 1"],
#     "command2": ["Description 2", "Details 2"],
#     "command3": ["Description 3", "Details 3"]
# }

# result = get_formatted_commands(my_commands)
# print(result)
