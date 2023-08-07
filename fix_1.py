import re

def to_camel_case(text):
    words = re.split('_|-', text)
    return words[0] + ''.join(word.title() for word in words[1::])

# была ошибка в строке re.split('_|-', "text")[1::], где была использована строка "text" вместо переменной text
# Также ошибка в строке words[0] где использовали индекс 1 вместо 0.