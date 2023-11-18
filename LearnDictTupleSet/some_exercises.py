

""" exercise 1 (harflerin sayısına göre grupladık)"""

# input_from_user = input("Bir isim giriniz : ")
# # 'eren' >  {'e': 2, 'r': 1, 'n': 1} .
# input_from_user = input_from_user.replace(" ", "") # eğer boşluk girerse boşluğu silmek için
# empty_dict = {}
# for i in input_from_user:
#     if i in empty_dict:
#         empty_dict[i] = empty_dict.get(i) + 1
#     else:
#         empty_dict[i] = 1
# print(empty_dict)

""" exercise 2 (key ve value yerlerini değiştiren algoritma yazdık) """

# {1: 'one' , 2 : 'two', 'three': 3, 'four': 4}

# empty_dict = {}

# for i in s_dict:
#     empty_dict[s_dict.get(i)] = i
# s_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# empty_dict = {s_dict.get(i): i for i in s_dict}
# print(empty_dict)

"""Exercise 3 (iki dictionaryi birleştirdik aynı keyleri topladık (2 yol ile yaptık) )"""

# dict_x = {'a': 5, 'b': 17, 'c': 25}
# dict_y = {'d' : 51, 'e': 30, 'a': 40}

# Way 1 (kısa yol)
# copied_x = dict_x.copy()
# copied_x.update(dict_y)
# print(copied_x)
# for i in copied_x:
#     if i in dict_x and i in dict_y:
#         copied_x[i] = copied_x.get(i) + dict_x.get(i)
# print(copied_x)

# Way 2 (uzun yol)

dict_x = {'a': 5, 'b': 17, 'c': 25}
dict_y = {'d' : 51, 'e': 30, 'a': 40}

x_keys = set(dict_x.keys()) # {'a', 'b', 'c'}
y_keys = set(dict_y.keys()) # {'d', 'e', 'a'}
intersection_keys = x_keys.intersection(y_keys) # {'a'}
unique_keys = x_keys.union(y_keys)
for x in intersection_keys:
    unique_keys.remove(x)
empty_dict = {}
for i in intersection_keys.union(unique_keys): #bütün key'leri dönüyoruz ortak olsansa iki dictionarydeki değerleri topluyoruz.
    if i in intersection_keys:
        empty_dict[i] = dict_x.get(i) + dict_y.get(i)
    elif i in unique_keys: # ortak değilse ya x'dedir ya y'dedir. x'teyse xdeki değeri alıyoruz y'deyse y'deki değeri alıyoruz.
        if i in dict_x:
            empty_dict[i] = dict_x.get(i)
        else:
            empty_dict[i] = dict_y.get(i)

print(empty_dict)
