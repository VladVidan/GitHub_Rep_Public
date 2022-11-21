# Ознайомтеся за допомогою документації з класами OrderedDict, defaultdict та ChainMap модуля collections.

# OrderedDict
# 1.Упорядоченная последовательность ключей в отличии от обычного dict
# 2.Потребляет больше памяти чем обычный dict
# 3.Является не подклассом словарей , а спец.контейнером модуля collections

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)
od['newkey'] = 'newvalue'
print(od)
print('-' * 50)

# defaultdict
# 1. Выдает значение заданное в виде функции в первом аргументе при обращении к несуществующему ключу как
# в случае со стандартным dict
# 2. Можно использовать как фабрику словарей , вставляя в первый аргумент класс list или int
# Syntax: defaultdict(default_factory)
# Parameters:
# default_factory: A function returning the default value for the dictionary defined.
# If this argument is absent then the dictionary raises a KeyError.

from collections import defaultdict

dd = defaultdict(lambda: 'Not present')
dd['a'] = 1
dd['b'] = 2
print(dd)
print(dd["a"])
print(dd["b"])
print(dd["c"])

print('-' * 50)

# Использование списка как default_factory :

def_dict = defaultdict(list)
for i in range(5):
    def_dict[i].append(i)
print(def_dict)

print('-' * 50)

# ChainMap
# Предоставляет почти такой же интерфейс, как и словарь , но с некоторыми дополнительными функциями
# Что-то типа списка словарей с методами словарей. Создает удобство работы в определенных ситуациях
from collections import ChainMap

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
d_in_d = ChainMap(numbers, letters)
print(d_in_d)