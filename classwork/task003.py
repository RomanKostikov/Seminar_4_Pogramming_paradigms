# ● Контекст:
# Важнейшая задача в анализе данных - поиск дубликатов. Дубликат - это наблюдение, встречающееся в
# данных больше одного раза. Такие наблюдения не просто не улучшают результат анализа или
# полученных моделей, но и замедляют весь процесс в целом, поэтому аналитики и разработчики
# предпочитают избавляться от них перед тем как приступить к анализу.
# ● Ваша задача:
# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход
# подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к
# массиву, дубликаты должны быть выведены на экран в виде списка.

# def find_duplicates(lst: list[int]) -> set[int]:
#     return set(filter(lambda x: lst.count(x) > 1, lst))  # )))
#
#
# # return filter(lambda x: lst.count(x) > 1, lst)
#
# lst_in = [1, 2, 5, 3, 2, 4, 5, 6, 7]
#
# print(lst_in)
# print(list(find_duplicates(lst_in)))

# оптимальное решение
def search_duplicates(arr):
    count_items = {}
    for item in arr:
        count_items.setdefault(item, 0)
        count_items[item] += 1
    return list(set(filter(lambda x: count_items[x] > 1, arr)))

arr = [8, 4, 7, 0, 4, 0, 10, 4, 7, 4]

duplicates = search_duplicates(arr)
print(duplicates)