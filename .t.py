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



# # Работает
# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step):
#         self.step = step

#     def __iter__(self):
#         return self.Iterable(self.step)
    
#     class Iterable:
#         d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
#         "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
#         "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#         "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
#         }
#         current_page = 1
#         def __init__(self, step):
#             self.step = step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
#             # for i, key in enumerate(self.d.keys()):
#             #     print(f"{i}: {key}")
#             # for i, key in enumerate(self.d.items()):
#             #     print(f"{key[0]}: {key[1]}")
#             if self.count <= len(self.d):
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for i, key in enumerate(self.d.items()):
#                         for _ in range(self.step):
#                             self.current_value += f"{key[0]}: {key[1]}" + "\n"
#                             self.count +=1
                            
#                         self.current_page += 1
#                         return self.current_value.strip()
#                 except KeyError:
#                     return self.current_value.strip()
                
                
#             raise StopIteration


# c = CustomIterator(3)
# for i in c:
#     _ = input("--->>> Enter")
#     print(i)





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






# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step, max_step):
#         self.step = step
#         self.max_step = max_step

#     def __iter__(self):
#         return self.Iterable(self.step, self.max_step)
    
#     class Iterable:
#         d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
#         "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
#         "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#         "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
#         }
#         current_page = 1
#         def __init__(self, step, max_step):
#             self.step = step
#             self.max_step = max_step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
#             if self.count <= self.max_step:
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for _ in range(self.step):
                        
#                         self.current_value += f"{self.d[str(self.count)]}" + "\n"
#                         self.count +=1
#                 except KeyError:
#                     return self.current_value.strip()
                
#                 self.current_page += 1
#                 return self.current_value.strip()
#             raise StopIteration


# c = CustomIterator(3, 20)
# for i in c:
#     _ = input("--->>> Enter")
#     print(i)













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



    # def iterator(self, n, page=1):
    #     count = 0
    #     start = (page - 1) * n
    #     end = page * n
        
    #     for i, key in enumerate(self.keys()):
    #         if i >= start and i < end:
    #             yield key, self[key]
    #             count += 1
    #         elif i >= end:
    #             break
    
    # def show_page(self, page_number=1, count=5):
    #     out = '|{:^98}|\n'.format(f" Page #{page_number}   |  Max {count} contacts per page.")
    #     out += '-'*100 + '\n'
    #     out += '| {:^20} | {:^50} | {:^20} |\n'.format('Name', 'Phones', 'Birthday date')
    #     out += '-'*100 + '\n'
    #     if self.keys():
    #         for key, value in self.iterator(int(count), page=int(page_number)):
    #             out += value.print_record()
    #     else:
    #         out += '| {:^96} |\n'.format('Adress book is empty.')
    #     out += '-'*100 + '\n'
    #     return out


    # def print_all(self):
    #     out = '-'*100 + '\n'
    #     out += '| {:^20} | {:^50} | {:^20} |\n'.format('Name', 'Phones', 'Birthday date')
    #     out += '-'*100 + '\n'
    #     if self.keys():
    #         for key in self.keys():
    #             out += self[key].print_record()
    #     else:
    #         out += '| {:^96} |\n'.format('Adress book is empty.')
    #     out += '-'*100 + '\n'
    #     return out



# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step):
#         self.step = step

#     def __iter__(self):
#         return self.Iterable(self.step)
    
#     class Iterable:
#         d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
#         "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
#         "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#         "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
#         }
#         current_page = 1
#         def __init__(self, step):
#             self.step = step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
        
#             if self.count <= len(self.d):
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for _ in range(self.step):
#                         i, key = next(iter(self.d.items()))
#                         self.current_value += f"{i}: {key}" + "\n"
#                         self.count += 1
#                     yield self.current_value.strip()
                            
#                     self.current_page += 1
#                     return self.current_value.strip()
#                 except StopIteration:
#                     return self.current_value.strip()
                
#             raise StopIteration


# c = CustomIterator(3)
# for i in c:
#     _ = input("--->>> Enter")
#     print(i)




# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step):
#         self.step = step

#     def __iter__(self):
#         return self.Iterable(self.step)
    
#     class Iterable:
#         d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
#         "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
#         "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#         "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
#         }
#         current_page = 1
#         def __init__(self, step):
#             self.step = step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
        
#             if self.count <= len(self.d):
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for _ in range(self.step):
#                         i, key = next(iter(self.d.items()))
#                         self.current_value += f"{i}: {key}" + "\n"
#                         self.count += 1
#                         del self.d[i]
                            
#                     self.current_page += 1
#                     return self.current_value.strip()
#                 except StopIteration:
#                     return self.current_value.strip()
                
#             raise StopIteration


# def print_paged_dictionary(iterator):
#     for page in iterator:
#         _ = input("--->>> Enter")
#         print(page)


# c = CustomIterator(3)
# print_paged_dictionary(c)





# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step, max_step):
#         self.step = step
#         self.max_step = max_step

#     def __iter__(self):
#         return self.Iterable(self.step, self.max_step)
    
#     class Iterable:
#         d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
#         "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
#         "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#         "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
#         }
#         current_page = 1
#         def __init__(self, step, max_step):
#             self.step = step
#             self.max_step = max_step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
#             if self.count <= self.max_step:
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for _ in range(self.step):
                        
#                         self.current_value += f"{self.d[str(self.count)]}" + "\n"
#                         self.count +=1
#                 except KeyError:
#                     return self.current_value.strip()
                
#                 self.current_page += 1
#                 return self.current_value.strip()
#             raise StopIteration


# c = CustomIterator(3, 20)
# for i in c:
#     _ = input("--->>> Enter")
#     print(i)



# from collections import UserDict

# class CustomIterator(UserDict):

#     def __init__(self, step, max_step):
#         self.step = step
#         self.max_step = max_step

#     def __iter__(self):
#         return self.Iterable(self.step, self.max_step)
    
#     class Iterable:
#         d = {"Max":   [{"Phone":"+380991111111"}, {"Birthday": "2000-12-12"}], 
#             "Bill":   [{"Phone":"+380991111121"}, {"Birthday": "1999-12-12"}], 
#             "Shasha": [{"Phone":"+380991411121"}, {"Birthday": "1989-12-12"}], 
#             "Devid":  [{"Phone":"+380991116251"}, {"Birthday": "1991-12-11"}], 
#             "Richard":[{"Phone":"+380991111441"}, {"Birthday": "1993-12-12"}], 
#             "Marco":  [{"Phone":"+380991111166"}, {"Birthday": "1990-12-11"}], 
#             "Boris":  [{"Phone":"+380991111546"}, {"Birthday": "1991-11-12"}], 
#             "Greg":   [{"Phone":"+380991111177"}, {"Birthday": "1960-12-12"}], 
#             "Oleg":   [{"Phone":"+380991119966"}, {"Birthday": "1997-12-12"}], 
#             "Andre":  [{"Phone":"+380991551166"}, {"Birthday": "1960-12-12"}]
#             }
#         current_page = 1
#         def __init__(self, step, max_step):
#             self.step = step
#             self.max_step = max_step
#             self.current_value = ""
#             self.count = 1

#         def __next__(self):
#             if self.count <= self.max_step:
#                 self.current_value = f'page : {self.current_page}\n'
#                 try:
#                     for _ in range(self.step):
#                         key = str(self.count)
#                         value = self.d.get(key)
#                         if value is not None:
#                             self.current_value += f"{key}: {value}" + "\n"
#                             self.count += 1
#                         else:
#                             break
#                 except KeyError:
#                     return self.current_value.strip()
                
#                 self.current_page += 1
#                 return self.current_value.strip()
#             raise StopIteration



from collections import UserDict

class CustomIterator(UserDict):

    def __init__(self, step):
        self.step = step

    def __iter__(self):
        return self.Iterable(self.step)
    
    class Iterable:
        d = {"1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5", 
        "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10", 
        "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
        "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
        }

        # d = {"Max":   [{"Phone":"+380991111111"}, {"Birthday": "2000-12-12"}], 
        #     "Bill":   [{"Phone":"+380991111121"}, {"Birthday": "1999-12-12"}], 
        #     "Shasha": [{"Phone":"+380991411121"}, {"Birthday": "1989-12-12"}], 
        #     "Devid":  [{"Phone":"+380991116251"}, {"Birthday": "1991-12-11"}], 
        #     "Richard":[{"Phone":"+380991111441"}, {"Birthday": "1993-12-12"}], 
        #     "Marco":  [{"Phone":"+380991111166"}, {"Birthday": "1990-12-11"}], 
        #     "Boris":  [{"Phone":"+380991111546"}, {"Birthday": "1991-11-12"}], 
        #     "Greg":   [{"Phone":"+380991111177"}, {"Birthday": "1960-12-12"}], 
        #     "Oleg":   [{"Phone":"+380991119966"}, {"Birthday": "1997-12-12"}], 
        #     "Andre":  [{"Phone":"+380991551166"}, {"Birthday": "1960-12-12"}]
        #         }


        current_page = 1
        def __init__(self, step):
            self.step = step
            self.current_value = ""
            self.count = 1

        def __next__(self):
            if self.count <= len(self.d):
                self.current_value = f'page : {self.current_page}\n'
                try:
                    for _ in range(self.step):
                        
                        self.current_value += f"{self.d[str(self.count)]}" + "\n"
                        self.count +=1
                except KeyError:
                    return self.current_value.strip()
                
                self.current_page += 1
                return self.current_value.strip()
            raise StopIteration


c = CustomIterator(3)
for i in c:
    _ = input("--->>> Enter")
    print(i)




    
# Все работает, дурак зачем трогал то что работает? теперь разбирайся 

    # def create_page(self, num):
    #     if len(self.data) == 0:
    #         return None
    #     result = ""
    #     result_list = {}
    #     count = 1
    #     page = 1
    #     n = 12

    #     result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
    #     result += " {:^92}".format("|" + " "*n +f"Page {page}" + " "*12 + "|") + "\n"
    #     result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"

    #     for i in self.data.values():
    #         value_birthday = "No birthday date"
    #         name_value = f"Name {i.name.value}: "
    #         phone_value = f"Phone {[ii.value for ii in i.phones]} "
    #         birthday_value = f"Birthday {i.birthday.value if i.birthday else value_birthday}"
            
    #         if count == 1:
    #             result += " {:^90}".format("_"*92) + "\n"
    #         else:
    #             result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"

    #         result += "| {:<29}| {:<29}| {:<29}|".format(name_value, phone_value, birthday_value) + "\n"
            
    #         if int(num) == count:
    #             result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"
    #             count = 0
    #             result_list[page] = result
    #             result = ""
    #             page += 1
    #             if len(self.data) / int(num) == page-1:
    #                 return result_list
    #             if page > 9:
    #                 n = 11
    #             elif page > 99:
    #                 n = 10
            
    #             result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
    #             result += " {:^92}".format("|" + " "*n +f"Page {page}" + " "*12 + "|") + "\n"
    #             result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"
    #         count += 1
    #     result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"
    #     result_list[page] = result
    #     return result_list
    



# @input_error
# def main():
#     while flag_exit: 
#         lsdc = ['add max +38099-111-2222 2000-12-12','add chacha +38019-101-2212 2001-12-12', 'add bill +38099-311-2922 2002-12-12',
#                 'add devid +38019-171-2222 2000-11-11','add greg +38099-111-5512 2000-12-11','add richard +38099-111-1112 2011-12-12', 
#                 'add max1 +38099-111-2212 2000-11-12','add chacha1 +38019-111-2212 2011-12-12', 'add bill1 +38099-311-2122 2012-12-12',
#                 'add devid1 +38019-111-2222 2001-11-11','add greg1 +38099-111-5112 2000-11-11','add richard1 +38099-111-1111 2011-11-12', 
#                 "show page 4","close"]
#         # lsdc = ['add max +38099-111-2222 2000-12-12','add chacha +38019-101-2212 2001-12-12', "show page 3",
#         #         "close"]
#         for i in lsdc:
#             uzer_input = i 
#             com = handler(uzer_input)
#             print(com(uzer_input.lower()))









