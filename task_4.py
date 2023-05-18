"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
bytes_list = [word.encode('utf-8') for word in words]
decoded_list = [bytes_word.decode('utf-8') for bytes_word in bytes_list]
print(bytes_list)
print(decoded_list)
