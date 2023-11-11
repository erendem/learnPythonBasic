numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# """"""
# 10 dan geriye 5'e kadar saymak, sondaki -1 eksi yönde gideceğini belirtir.
# for i in range(10, 5, -1):
#     print(i)

# //////////////////////////////////////////////////////////////////////////////////////////


# fruit_list = ["Muz", "elma", "Greyfurt", "Portakal"]

# "Listede baş harfi büyük olanları bulduk, baş harfi büyük olmayanları listeden çıkarıp büyük haliyle ekledik."

# uppered_fruit_list = []
# count = 0
# for fruit in fruit_list:
#     if fruit[0].isupper():
#         uppered_fruit_list.append(fruit)
#     else:
#         upper_fruit = fruit.replace(fruit[0], fruit[0].upper())
#
#         fruit_list.append(upper_fruit)
#         # fruit_list.remove(fruit) # remove methodu direkt ismiyle spesifik siler
#         fruit_list.pop(count) # indeksi ile sildik
#
#     count += 1
#
# # print(uppered_fruit_list)
# print(fruit_list)

# //////////////////////////////////////////////////////////////////////////////////////////

# loop_in_loop = [ [1, 2, 3], [4, 5, 6] ]
# even_numbers = []
# for inner_list in loop_in_loop:
#     for number in inner_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
# print(even_numbers)

# //////////////////////////////////////////////////////////////////////////////////////////

# some_list = [5,-3, 17, '75', 5, 99, 101, 'a', '+']
# integer olanları yazdırdık sadece
# for i in some_list:
#     if type(i) is not int:
#         continue
#     print(i, end=" ")

# //////////////////////////////////////////////////////////////////////////////////////////

# is_while_run = True
# while True:
#     for i in range(50):
#         print(i)
#         if i == 20:
#             is_while_run = False
#             break
#     if is_while_run is False:
#         break

# //////////////////////////////////////////////////////////////////////////////////////////

#aşağıdaki örnekte, boş bir string tanımladık ve 6'nın katlarını stringe ekleyerek arada tire işaretiyle yazdık.


# x = ""
# for i in range(100):
#     if i % 6 == 0:
#         x += "-{}".format(i)
#
# x = x[1:] #bu işlem başta eklenen tireyi siler 1nci elemandan sonuna kadar stringi al ve yeniden stringe eşitle dedik.(Yani ilk elemanı alma dedik)
# list_of_six_number = x.split("-")  #burada tireye göre split edip listeye dönüştürdük.
#
# Listeye dönüşen numaralar elbette string olduğu için aşağıda integera cast etme yaptık
# int_list = []
# for j in list_of_six_number:
#     int_list.append(int(j))
#
# print(int_list)

# //////////////////////////////////////////////////////////////////////////////////////////


# x = [1,17, 23, -1, 99, 'a', 'A', 154, 'asd', '$', 65, 129, 300 , 250]
# odd_number_list = []
# even_number_list = []
# arithmetic_list = []
#
# for i in x:
#     if type(i) is not int:
#         continue
#
#     if i % 2 == 0:
#         even_number_list.append(i)
#     else:
#         odd_number_list.append(i)
#
# even_number_list.sort()
# odd_number_list.sort(reverse=True)
#
# arithmetic_even = sum(even_number_list) / len(even_number_list)
# odd_number_list = sum(odd_number_list) / len(odd_number_list)
# arithmetic_list.extend([round(arithmetic_even, 2), round(odd_number_list, 2)])
#
# print(odd_number_list)
# print(even_number_list)
# print(arithmetic_list)

# import string
# print(string.ascii_lowercase)
#
# name = input("Bir isim giriniz : ")
# """eren --> 4"""
# x = []
# for letter in name:
#     indexing = string.ascii_lowercase.index(letter)
#     x.append(indexing)
# print(x)
"""List Comprehension"""

# some_list = [1,2,3,'a', 'B', 55, 'C', 'f']
# # even_number = []
# # for number in number_list:
# #     if number % 2 == 0:
# #         even_number.append(number)
#
# result_list = [i for i in some_list if type(i) is int or (type(i) is str and i.isupper())]
# print(result_list)

"""Enumerate (iterable'lara sayaç, counter ekler """

# x= enumerate(['a', 'b', 'c', 'd'], start=1)
# print(list(x))


"""For else
For else kavramında eğer break olursa else çalışmaz, break olmadığı her durumda -döngü bittikten sonra- else de çalışır.
Kısayoldur.
"""

for number in range(2, 100):
    # is_prime = True
    for p in range(2, number):
        if number % p == 0:
            break
    else:
        print(number, end="-")
    #if is_prime:
        #print(number, end="-")