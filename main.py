##################################
# s1 = 2
# s2 = 1

# def zadacha_1(s1, s2):
#     return s1 + s2

# print(zadacha_1(s1, s2))
##################################

# s1 = 'hello'

# def zadacha_2(s1):
#     count = 0
#     for a in  s1:
#         count += 1
#     return count

# print(zadacha_2(s1))
##################################

# s1 = 'ss'
# n = 3
# def zadacha_3(s1, n):
#     return s1 * n

# print(zadacha_3(s1, 3))
##################################

# s1 = 'adadad'
# def zadacha_4(s1):
#     return (s1[0], s1[-1])

# print(zadacha_4(s1))
##################################

# s1 = 'asdfgh'
# def zadacha_5(s1):
#     return (s1[2:5])

# print(zadacha_5(s1))
##################################

# s1 = 'asasasa'
# def zadacha_6(s1):
#     count = 0
#     for s in s1:
#         if s == 'a':
#             count += 1
#     return count
# print(zadacha_6(s1))
##################################

# s1 = 'sa sa sa'
# def zadacha_7(s1):
#     rezult = ''
#     for a in s1:
#         if a == " ":
#             rezult += "_"
#         else:
#             rezult += a

#     return rezult
    
# print(zadacha_7(s1))
##################################

# s1 = 'asdfg'
# def zadacha_8(s1):
#     return (s1[::-1])

# print(zadacha_8(s1))
##################################

# s1 = 'asd'
# def zadacha_9(s1):
#     rezult = ""
#     for c in s1:
#         if 'a' <= c <= 'z':
#             rezult += chr(ord(c) - 32)
#         elif 'а' <= c <= 'я':
#             rezult += chr(ord(c) - 32)
#         else:
#             rezult += c
#     return rezult

# print(zadacha_9(s1))
##################################

# s1 = 'hello danya'
# def zadacha_10(s1):
#     return s1.title()

# print(zadacha_10(s1))
##################################

# s1 = 'asasasa'
# def zadacha_11(s1):
#     new_st = ''
#     world_count = 0 
#     for a in s1:
#         world_count += 1
#         if world_count %2 == 0:
#             new_st += a.upper()
#         else:
#             new_st += a

#     return new_st

# print(zadacha_11(s1))
##################################

# s1 = '           as as as as '
# def zadacha_12(s1):
#     new_strok = list(s1)
#     while new_strok and new_strok[0] == ' ':
#         new_strok.pop(0)
#     while new_strok and new_strok[-1] == ' ':
#         new_strok.pop(-1)
#     return ''.join(new_strok)


# print(zadacha_12(s1))
##################################

# s1 = 'asasa'
# def zadacha_13(s1):
#     return s1 == s1[::-1]

# print(zadacha_13(s1))
################################## 

# s1 = 'asas12'
# def zadacha_14(s1):
#     for char in s1:
#         if char.isdigit():
#             return f'Здесь есть буквы'
#     return f'Здесь нет букв'
# print(zadacha_14(s1))
##################################

# def zadacha_15(s):
#     for c in s:
#         if not c.isalpha():
#             return f'Здесь есть цифры'
#     return f'Здесь нет цифр'

# print (zadacha_15('asasa'))
##################################

# s1 = 'hello world'
# def zadacha_16(s):
#     stroka = 'Hello'  
#     if s1[0:5] == stroka:
#         return f'Строка начинается с {stroka}'
#     else:
#         return f'Строка не начинается с {stroka}'
# print(zadacha_16(s1))
##################################

# s1 = 'hello world'
# def zadacha_17(s1):
#     return s1.split()

# print(zadacha_17(s1))
##################################

# s1 = ('hello', 'world')
# def zadacha_18(s1):
#     return ','.join(s1)
    
    
# print(zadacha_18(s1))
##################################

# name = 'Danya'
# age = 22
# def zadacha_19(name, age):
#     return f'Меня зовут {name}, мне {age} лет'

# print(zadacha_19(name, age))
##################################

# s1 = 'hello world 1 1 1 1'
# def zadacha_20(s1):
#     count = 0
#     for char in s1:
#         if char == ' ':
#             count += 1
#     return count + 1  

# print(zadacha_20(s1))
###################################

# s1 = 'hello world'
# def zadacha_21(s1):
#     book = {}
#     for char in s1:
#         if char in book:
#             book[char] += 1
#         else:
#             book[char] = 1
#     return book

# print(zadacha_21(s1))
##################################

# s1 = 'helloo world'
# def zadacha_22(s1):
#     words = s1.split()
#     if not words:
#         return f'Строка пустая'
#     return max(words, key=len)

# print(zadacha_22(s1))
##################################



# s1 = 'halo'
# def zadacha_23(s1):
#     stroka = set()
#     for char in s1:
#         stroka.add(char)
#     if len(stroka) == len(s1):
#         return f'Строка уникальная'
#     else:
#         return f'Строка не уникальная'

# print(zadacha_23(s1))

# def zadacha_23(s1:)
#     return 'Уникальная' if len(set(s1)) == len(s1) else 'Не уникальная'
   
##################################


# import random 
# import string

# def zadacha_24(pass_lenght: int):
#     if pass_lenght < 6:
#         raise ValueError('Пароль должен быть не менее 6 символов')
    
#     chars_pass = string.ascii_letters + string.digits + string.punctuation
    
#     password = ''.join(random.choice(chars_pass) for _ in range(pass_lenght))
#     return password
    

# print(zadacha_24(12))  # Пример вызова функции для генерации пароля длиной 8 символов
##################################


###################################################################################################
                                    #Работа со списками#

# s1 = [1, 2, 3, 4, 5]
# def zadacha_1(s1):
#     return sum(s1)

# print(zadacha_1(s1))
##################################

# s1 = [1, 2, 3, 4, -1]
# def zadacha_2(s1):
#     if not s1:
#         return None
#     max_num = s1[0]
#     min_num = s1[0]
#     for num in s1:
#         if num > max_num:
#             max_num = num
#         if num < min_num:
#             min_num = num
#     return max_num, min_num

# print(zadacha_2(s1))
##################################

# s1 = [1, 2, 3, 4, 5]
# def zadacha_3(s1):
#     return sum(s1) / len(s1)

# print(zadacha_3(s1))
##################################

# s1 = [1, 2, 3, 4, 5]
# def zadacha_4(s1):
#     count = 0
#     for char in s1:
#         count += 1
#     return count

# print(zadacha_4(s1))
##################################

# s1 = [1, 2, 3, 4, 5]
# def zadacha_5(s1):
#     stroka = ''
#     for char in s1:
#         stroka += str(char)
#     return list(stroka[::-1])
        
# print(zadacha_5(s1))
##################################

# s1 = [1, 1 ,2, 3, 3, 4, 5]
# def zadacha_6(s1):
#     mno = set()
#     for char in s1:
#         mno.add(char)
#     return list(mno)

# print(zadacha_6(s1))
###################################

# s1 = [1, 2, 3, 4, 5]
# s2 = [6, 7, 8, 9, 10]
# s3 = []
# def zadacha_7(s1, s2):
#     for char in s1:
#         s3.append(char)
#     for char in s2:
#         s3.append(char)
#     return s3

# print(zadacha_7(s1, s2))
###################################

# s1  = [1, 2, 3, 4, 5]
# def zadacha_8(s1):
#     if len(s1) > 3:
#         s1[3] = 42
#     return s1    
    
# print(zadacha_8(s1))
###################################

# s1 = [1, 2, 3, 4, 5]
# def zadacha_9(s1):
#     s1.remove(5)
#     return s1
    
# print(zadacha_9(s1))
###################################

# s1 = [1, 2, 3, 4, 5]
# def zadacha_10(s1):
#     for char in s1:
#         if char % 2 != 0:
#             s1.remove(char)
#     return s1

# print(zadacha_10(s1))
###################################

# s1 = ['apple', 'apple', 'banana', 'orange']
# def zadacha_11(s1):
#     count = s1.count('apple')
#     return count

# print(zadacha_11(s1))
###################################

# s1 = ['api', 'banana', 'orange']
# def zadacha_12(s1):
#     lenght = 3
#     for char in s1:
#         if len(char) <= lenght:
#             s1.remove(char)
#     return s1

# print(zadacha_12(s1))
###################################

# s1 = [1, 2, 3, 4, 5, 5]
# def zadacha_13(s1):
#     mno = set()
#     for char in s1:
#         mno.add(char)
#         if len(mno) == len(s1):
#             return f'Все элементы уникальны'
#     return f'Есть повторяющиеся элементы'

# print(zadacha_13(s1))
###################################

# s1 = [1, 2, 3, 4, 5]
# s2 = []
# def zadacha_14(s1, s2):
#     for char in s1:
#         s2.append(char ** 2)
#     return s2

# print(zadacha_14(s1, s2))
###################################

# s1 = [-1, 2, 3, -4, -5]
# s2 = []
# def zadacha_15(s1):
#     for char in s1: 
#         if char < 0:
#             char = 0
#             s2.append(char)
#         else:
#             s2.append(char)
#     return s2

# print(zadacha_15(s1))
###################################

# s1 = ['apple', 'bananaa', 'orange']
# s2 =[]
# def zadacha_16(s1):
#     s2 = sorted(s1, key=len)
#     return s2


# print(zadacha_16(s1))
###################################