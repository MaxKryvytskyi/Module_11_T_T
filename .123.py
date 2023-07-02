# from collections import UserDict


# class AddtextsBook(UserDict):

#     def add_record(self, record):
#         if record.name.value not in self.keys():
#             self.data[record.name.value] = record
#             return True
#         else:
#             print("Name already exists. Try adding the phone command to add an extra phone.")
#             return False

#     class Iterable:
#         d = {
#             "1": "value1", "2": "value2", "3": "value3", "4": "value4", "5": "value5",
#             "6": "value6", "7": "value7", "8": "value8", "9": "value9", "10": "value10",
#             "11": "value11", "12": "value12", "13": "value13", "14": "value14", "15": "value15",
#             "16": "value16", "17": "value17", "18": "value18", "19": "value19", "20": "value20"
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
#                         self.count += 1
#                 except KeyError:
#                     return self.current_value.strip()

#                 self.current_page += 1
#                 return self.current_value.strip()
#             raise StopIteration

#     def __iter__(self):
#         return self.Iterable(3, 20)


# book = AddtextsBook()
# # Додайте записи до AddtextsBook

# for i in book:
#     _ = input("--->>> Enter")
#     print(i)



# Приклад

# def main(num, max_num):
#     nums = 0
#     nums += num
#     result = ""
#     count = 0
#     for i in range(max_num+1):
#         result += str(i)
#         count += 1
#         if count == nums:
#             nums += num
#             yield result
#             result = ""

#         elif i > max_num:
#             return result

        
# num = 10
# max_num = 100

# m = main(num, max_num)
# for _ in range(int(max_num/num)):
#     print(next(m))





# print(" {:^30}".format("_"*32))
# print("|{:<10}|{:^10}|{:>10}|".format(15,15,15))
# print("{:<30}".format("|" + "_"*10 + "|" + "_"*10 + "|"+ "_"*10 + "|"))


# print(" {:^100}".format("_"*101))
# print("|{:^101}|".format(15,15,15))
# print("{:<100}".format("|" + "_"*101 +"|"))









        # cache_list.append({k : v})
        # count += 1
        # if count == num:
        #     count = 0
        #     yield cache_list
        #     cache_list.clear()
        # else:
        #     return cache_list
        
        
        

    

# num = 3
# c = main(num)
# print(c) 

# for i in range(4):
#     print(next(c))












from collections import UserDict

class AddtextsBook(UserDict):
    d = {"Max":   [{"Phone":"+380991111111"}, {"Birthday": "2000-12-12"}], 
        "Bill":   [{"Phone":"+380991111121"}, {"Birthday": "1999-12-12"}], 
        "Shasha": [{"Phone":"+380991411121"}, {"Birthday": "1989-12-12"}], 
        "Devid":  [{"Phone":"+380991116251"}, {"Birthday": "1991-12-11"}], 
        "Richard":[{"Phone":"+380991111441"}, {"Birthday": "1993-12-12"}], 
        "Marco":  [{"Phone":"+380991111166"}, {"Birthday": "1990-12-11"}], 
        "Boris":  [{"Phone":"+380991111546"}, {"Birthday": "1991-11-12"}], 
        "Greg":   [{"Phone":"+380991111177"}, {"Birthday": "1960-12-12"}], 
        "Oleg":   [{"Phone":"+380991119966"}, {"Birthday": "1997-12-12"}], 
        "Andre":  [{"Phone":"+380991551166"}, {"Birthday": "1960-12-12"}],
        "Max1":    [{"Phone":"+380991111111"}, {"Birthday": "2000-12-12"}], 
        "Bill1":   [{"Phone":"+380991111121"}, {"Birthday": "1999-12-12"}], 
        "Shasha1": [{"Phone":"+380991411121"}, {"Birthday": "1989-12-12"}], 
        "Devid1":  [{"Phone":"+380991116251"}, {"Birthday": "1991-12-11"}], 
        "Richard1":[{"Phone":"+380991111441"}, {"Birthday": "1993-12-12"}], 
        "Marco1":  [{"Phone":"+380991111166"}, {"Birthday": "1990-12-11"}], 
        "Boris1":  [{"Phone":"+380991111546"}, {"Birthday": "1991-11-12"}], 
        "Greg1":   [{"Phone":"+380991111177"}, {"Birthday": "1960-12-12"}], 
        "Oleg1":   [{"Phone":"+380991119966"}, {"Birthday": "1997-12-12"}],
        "Oleg11":   [{"Phone":"+380991119966"}, {"Birthday": "1997-12-12"}],
        "Andre1":  [{"Phone":"+380991551166"}, {"Birthday": "1960-12-12"}]
            }
    print(len(d))
    def add_record(self, record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record
            return True
        else:
            print("Name already exist. Try add phone command for add extra phone.")
            return False



    def create_page(self, num):
        result = ""
        result_list = {}
        count = 1
        page = 1
        n = 12

        result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
        result += " {:^92}".format("|" + " "*12 +f"Page {page}" + " "*12 + "|") + "\n"
        result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"
        for _, name in enumerate(self.d.items()):
            for birthday, data in name[1][1].items():
                for phone, numders in name[1][0].items():
                    name_value = f"Name {name[0]}: "
                    phone_value = f"{phone} {numders}, "
                    birthday_value = f"{birthday} {data}"
                    
                    if count == 1:
                        result += " {:^90}".format("_"*92) + "\n"
                    else:
                        result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"

                    result += "| {:<29}| {:<29}| {:<29}|".format(name_value, phone_value, birthday_value) + "\n"
                    
                    if num == count:
                        result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"
                        count = 0
                        result_list[page] = result
                        result = ""
                        page += 1
                        if len(self.d) / num == page-1:
                            return result
                        if page > 9:
                            n = 11
                        elif page > 99:
                            n = 10
                   
                        result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
                        result += " {:^92}".format("|" + " "*n +f"Page {page}" + " "*12 + "|") + "\n"
                        result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"
                    count += 1
                
        result += "{:^90}".format("|" + "_"*30 +"|"+ "_"*30 +"|"+ "_"*30 +"|") + "\n"
        result_list[page] = result
        return result_list
    
    def iterator(self, num):
        result = self.create_page(num)
        len(result)
        for _, value in result.items():
            yield value
            


num = 5
n = 1
addtextsBook = AddtextsBook()
c = addtextsBook.iterator(num)
for _ in range(1000):
    
    _ = input(f"Page : {n}")
    try:
        print(next(c))
    except StopIteration:
        break
    n += 1



