"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

urls = ["yandex.ru", "youtube.com"]

for url in urls:
    result = subprocess.run(["ping", url], stdout=subprocess.PIPE)
    encoding = chardet.detect(result.stdout)['encoding']
    print(result.stdout.decode(encoding))
