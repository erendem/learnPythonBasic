"""
Dictionary python 3.7'den önceki versiyonlarında unordered iken 3.7den sonra (şu an güncelde) ordered data tipi olarak karşımıza çıkmaktadır.

{key: value} yapısındadır. Tuttuğu elemanları belirli bir key yani anahtar ile değerlerini tutar.

key mutlaka immutable olmalı ve unique olmalı. Mesela list(mutable olduğu için) dictionary'e key olamaz. Fakat value olabilir.

"""

#
num_names = {"one": 1, "two": 2, "three": 3}
print(num_names)

# constructor
empty_dict = dict()
num_names = dict(one=1, two=2, three=3)
num_names_other_example = dict([("one", 1),("two", 1),("three", 1)])
print(num_names)
print(num_names_other_example)

# Value Access
capitals_dict = {'tr': "Ankara", "usa": "Washington", "al": "Belin", "fr": "Paris"}
print(capitals_dict.get("tr")) # --> "Ankara"
print(capitals_dict["tr"])

all_values = list(capitals_dict.values())
print(all_values)

# Key Access
all_keys = list(capitals_dict.keys()) # ['tr', 'usa', 'al', 'fr']
print(all_keys)

#items

all_items = list(capitals_dict.items())
print("All items : ", all_items)

#check if key exist
if 'tr' in capitals_dict:
    print("Türkiye dictionary'de mevcut")

# access element using loop
for k in capitals_dict:
    print(k) #--> keyleri döner
    print(capitals_dict.get(k)) # --> value'lar döner

""" Update Dictionary """

capitals_dict = {'tr': "Ankara", "usa": "Washington", "al": "Belin", "fr": "Paris"}

capitals_dict["usa"] = "New York" #usa adında key var dolayısıyla mevcut değeri günceller(yani washington -> New york)
capitals_dict["eng"] = "London"  # eng adında key yok fakat yoksa yenisini oluşturur.

print(capitals_dict)

# Dictionary update etmenin ikinci yolu da update methodu'dur.
capitals_dict.update({'ar': "Buenos Aires"})
print(capitals_dict)

""" Deletion Dictionary """

del capitals_dict["usa"] # usa key ve value karlığını uçurur
print(capitals_dict)

""" * ! """
# del capitals_dict # tamamen dictionary'i memory'den siler
# print(capitals_dict) bu kod çalışmaz hata verir çünkü tamamen dictionary'i silmiştir.

""" Dictionary Methods 
1. dict.clear() --> Dictionary'i tamamen memory'den silmez. Yalnızca içindeki elamanları boşaltarak tamamen boş bir dictionary yapar.
2. dict.copy() --> shallow copy'i çağırır, yani yüzeysel olarak birebir sırasıyla aynı dictionary'i kopyalar.
3. dict.pop(-key-) --> pop methodu listelerdeki gibi son elemanı silmez pop methoduna silinmek istenen key'in adı verilmelidir.
4. dict.update(), dict.keys(), dict.values(), dict.items() dictionary methodlarıdır. Bunların örnekleri yukarıdadır.

Detaylar ve tüm methodlar için print(dir(dict)), spesifik istenen methodun açıklamasını öğrenmek için print(help(dict.clear)) yazılabilir.

"""




