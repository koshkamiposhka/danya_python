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

adas