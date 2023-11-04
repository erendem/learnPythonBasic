"""
for loop;

numbers = [1,2,3,4,5,6,7,8]

syntax : for number in numbers:

numbers dizisi bitene kadar tek tek gezer "number" denilen değişken numbers dizisindeki her bir elamana karşılık gelir ve sırayla bakar.

while loop;

syntax : while (condition):
            ....

        condition geçerli(true) olduğu süre boyunca sonsuza kadar döner. Döngüyü bitirmek için ya break ya da condition'ın False olması koşulun geçersiz olması gerekir.


break ve continue keywords;

break : en içteki ilk döngüyü kıran/bitiren/sonlandıran keyworddür.
continue ise döngünün bir sonraki elemanına geçer.

ister break ister continue olsun bunları gördüğü zaman döngünün altında çalışan hiçbir kod çalışmaz break'de tamamen döngü kırılır ve döngüden çıkar.
continue'da ise döngünün alt kısmındaki kod çalışmadan bir sonraki döngünün elemanına geçer.(Yani döngü bir artırılır)

"""

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for number in numbers:
#     print(number)


some_list = [[1, 2, 3], ['a', 'b', 'c']]

for value in some_list:
    """ value değeri [1, 2, 3], ['a', 'b', 'c'] elemanlarına karşılık gelir. bu elemanların da içteki elemanlarını gezmek istersek
     bir daha for ile dönmemiz gerekir.
    """
    print(value) # --> [1,2,3], ['a', 'b', 'c']
    for inner_value in value:
        print(inner_value) # -->  1,2,3,'a','b','c'


list_values = []
while True:
    """sonsuza kadar 1 elemanını değere ekler eğer ben eleman sayısı 10 olunca bu döngüyü bitir dersem o zaman döngüden çıkar"""
    list_values.append(1)

    if len(list_values) == 10:
        break # döngüden çıkar 10 tane 1 eklemiştir.

