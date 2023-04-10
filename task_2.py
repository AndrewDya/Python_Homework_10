"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов (не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words_bytes = [b'class', b'function', b'method']


def byte():
    for i in range(len(words_bytes)):
        print(
            f"Тип {type(words_bytes[i])}, содержимое {words_bytes[i]}, длина {len(words_bytes[i])}")


byte()
