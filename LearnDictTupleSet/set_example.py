"""
Set mutable data türleridir. "{}"
Unordered yani sıralanmamış data tipidir. Bulundurduğu elemanların index ve yerlerini tutmaz.Dolayısıyla indexlenerek elemanlarına erişelemez.
Yalnızca distinct/tekil eleman tutar. {1,2,3,4} --> add(3) ---> {1,2,3,4} 3'den iki tane tutmaz.

Sadece immutable objeler set'in bir partı olabilir.

"""

some_set_example = {1, 6, 3, 'eren', 'True'}
print(some_set_example)

""" tüm elemanalara erişmek için for ile dönülebilir çünkü set'ler index'lenemez. """

for i in some_set_example:
    print(i)

""" set methods """

#Add/Update/remove
added_set = {'a', 'b', 'c'}

some_set_example.add(5.76)
print(some_set_example)

some_set_example.update(added_set)
print(some_set_example)

some_set_example.remove('a')
print(some_set_example)

#Kesişimi bulur (intersection)
a = [1, 2, 6]
inters = some_set_example.intersection(a)
print(inters)

#union birleştirir (matematikteki gibi)
another_set_elements = {7,8,15,'b', 3}
union_ex = some_set_example.union(another_set_elements)
print(union_ex)

#difference farkı bulur

diff_set = some_set_example.difference(another_set_elements)
print(diff_set)

# iki liste arasındaki fark için listeler set objelere cast edilerek işlem yapılabilir.

a_list = [1,2,3,4]
b_list = [3,4,5,6,7,8]

# fark için 1.yol
diff_list_result = set(a_list) - set(b_list) #a listesinde olup b listesinde olmayanlar tam tersi için set(b) - set(a)
print(list(diff_list_result))
#fark için 2.yol difference methodudur.
diff_list_result = set(a_list).difference(set(b_list))


