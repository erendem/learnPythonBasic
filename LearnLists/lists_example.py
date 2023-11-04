"""Lists
  Compound and sequences data types --> farklı türde elemanların tutulduğu ve sıralanabilen/döngülenebilen data tipleridir.

"""

#  List Indices

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = example_list[9: 7: -2]
# print(sliced_list)
# print(dir(list))

# copy types in list

""" there are two types of lists

    import copy

    1: Shallow copy 'copy.copy(list)'  ->  yüzeysel olarak kopyalar içerisinde bulunan listelerin id'lerini kopyalamaz
    2: Deep Copy  'copy.deepcopy(list)'  -> her şeyiyle kopyalama yapar içerisinde liste varsa onların id'lerini de kopyalar farklı yere kaydeder.
"""
import copy

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

shallow_copy = copy.copy(original_list)
original_list.append(56)
original_list[0][1] = 'eren'
# print(original_list)
# print(shallow_copy)

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_copied = copy.deepcopy(original_list)
original_list.append(56)
original_list[0][1] = 'eren'
# print(original_list)
# print(deep_copied)


# sorted list

x = [5, 6, 13, 27, 32, 1, 99]
""" sort metodu listeyi sıralar, ve bundan sonra liste nerede kullanılırsa orjinal liste bozularak sıralı olarak gelir."""
x.sort()
# print(x)
"""sorted ise, orjinal listeyi bozmadan sıralar ve başka değişkene atılarak orjinal listenin sıralanmış hali kullanılır"""
sorted_of_x = sorted(x)
# print(sorted_of_x)

"""
List methodları:

örnek liste = [1,2,3,4]

1. Append (listenin sonuna eleman ekler -> örnek_list.append(55) = [1,2,3,4, 55]
2. Remove Listeden spesifik eleman siler -> örnek_liste.remove(3) = [1,2,4]
3. insert istenilen spesifik index'e eleman ekler(index 0'dan başlar) örneğin 2nci sıraya eleman eklemek için = örnek_liste.inster(1, 63) = [1,63, 2,3,4]
4. clear listeyi temizler boş listeye çevirir.
5. extend listeye bir seferde bir listeyle birleştirerek yeni liste yapar ör: [1,2,3,4] liste olsun ['a','b'] başka liste olsun.
list1.extend(list2) dersek yeni listede birleştirir --> [1,2,3,4,'a','b'] olur.

6. pop  listedeki son elemanı siler.
7. len listede kaç eleman varsa onun sayısını döndürür --> len(örnek_list) :4
8. sum numeric listeki elemanların hepsini toplar sum(örnek_list) = 1+2+3+4 == 10;

 tüm methodları görmek için 'dir' ve 'help' komutlarına bakılarak yardım alınabilir

"""

# List concat
some_list = [1, 2, 3, 4]
new_list = [0] + some_list
append_list = some_list + [98, 87]
# print(new_list)
# print(append_list)

""" Mutable vs Immutable

Mutable = program akışı boyunca iç değerlerini değiştirebildiğimiz data türlerine mutable denir. Başlıca örnek list, set ve dictionary'dir.
Immutable = bunun tam tersidir, tanımlandıktan sonra iç değerlerini değiştiremiyorsak bunlara da immutable objeler deriz. Örnek: String, int, float, Tuples..

"""

""" Join ve Split fonksiyonları
Join fonksiyonu stringlerin iterable bir list parametresi alarak o listeyi stringe çevirdiğimiz metotlardır.
split ise bir stringdeki belirli bir spesifik karektere göre bölerek listeye dönüştüren metottur. Örnekler
"""

string_example = 'python is the most powerful language'
str_to_list = string_example.split(" ")
print(str_to_list)

list_example = ["a", "b", "c", "d", "e"]
list_to_str = "-".join(list_example)
print(list_to_str)

""" List filtreleme 
 filter(filtre tanımı/kuralı, listenin kendisi)
"""

list_to_be_filtered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = list(filter(lambda l: l % 2 == 0, list_to_be_filtered))
# sadece çift sayıları filtreledik
print(filtered_list)