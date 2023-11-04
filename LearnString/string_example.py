#### Raw strings
""" Tırnak işaretinin önüne 'r' ile başlanılarak yazılır.
    Amacı python'sal ifadeleri yok ederek içinde bulundurduğu tüm karakterleri metinsel olarak algılar. """

new_str = 'c://progrom_files\newgames\\riot'
print("Before Raw str", new_str)
new_str = r'c://progrom_files\newgames\\riot'
print("After Raw str", new_str)

""" (\) kaçış karakteridir. Kaçmak istenilen karakterden önce kullanılır. """

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------

"""Print function
print("printed value", end='', sep='')

end parametresi stringin sonu nasıl biteceğini belirtir,(default \n dir yani alt satıra atar. Bir şey yazılmazsa yan yana yazar)
sep parametresi seperator'dan gelir ve stringleri neyle ayıracağını söyler.

"""
# string definition types
new_str = """ calculates volume of cone"""
print(new_str)

# \n , \t, \b
""" '\n' -> new line demek, alt satıra atar. \t -> tab ile boşluk bırakır. \b kendinden önceki bir harfi siler.  """
new_str = "ajdnsakdajgn\badsad"
print(new_str)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------

# concatenated of string
x = 'eren'
y = x + 'demir'

# 'eren' 'demir' --> bu şekilde de concat eder çıktı 'erendemir' olarak yazar
# Fakat değişkenlerle (+ operatörü kullanmadan) concat işlemi yapılmaz
# x = 'eren'
# x 'demir' --> hata verir + operatörü kullanılması gerekmektedir. x + 'demir' --> çıktı verir

print(y)

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------

# string slicing
"""
stringleri köşeli parantezle keserek kullanılır örn: some_str[5:]

Kural : [ 'Başlangıç Index' : 'Gideceği Index' : 'yön/gidiş' ]
ilk iki parametre aralık belirtir.
son parametre + olursa pozitif artış - olursa negatif yöne doğru gideceğini belirtir.
"""

url = 'http://www.google.com.tr'
x = 'string kesmede ilk deneme'
sliced_str = x.split(" ")[0] + " " + x.split(" ")[1] + " " + x.split(" ")[2][0]
print(sliced_str)
print(url[7:])

# string reversing
reversing_str = 'stringkesmedeilkdeneme'
reversed_str = reversing_str[::-1]
print(reversed_str)


#len string
reversing_str = 'string'
reversing_str.__len__()
print(len(reversing_str))


#formatted string
age = 17
name = 'eren'

message = 'Merhaba {} yaşınız {}'.format(name, age)
second_message = "merhaba %s yaşınız %s" % (name, age)

# formatted_str = "{} {} {}".format('a', 'b', 'c') --> 'a b c'
# formatted_str = "{1} {2} {0}".format('a', 'b', 'c') --> 'b c a'

print(message)
print(second_message)
# print(formatted_str)

# converting string
x = 1792
print(type(x))
converted_str = str(x)
print(type(converted_str))
f" example  {converted_str} example" # -> 'example 1792 example'
print(type(f"{ x }"))

x = '54.53'
# print(float(x))

# string methods
""" help methoduyla string ve integer'ların methodlarını ve kullanımları hakkında bilgi edinilebilir. """
# print(help(str))
# print(help(str.capitalize))
# print(new_str_a.replace(" ", ""))

# find and count() method'ları
"""
find geçen kelimenin indexini döndürür.
count method'u ise istenilen kelimenin string içerisinde kaç defa geçtiğini söyler.

# print(help(str.find))
# print(help(str.count))
"""


ex_str = "python is the most is powerful language"
# print(ex_str.count("is"))
# print(ex_str.find("is"))

# input from user
# received_number = input("Doğum yılınızı giriniz : ")

# print(received_number)
# print(2023 - int(received_number))

"""partition methodu (str.partition) --> print(help(str.partition))
Toplam 3 parametre döndürür
1.parametresi aranan kelimeden önceki kısım
2.parametresi aranan kelime
3.parametresi aranan kelimeden sonraki kısım döndürür.
Örnek:

example_str = 'erendemir2023'
example_str.partition("demir") --> demir aranan kelime 

1.Kısım eren
2.Kısım demir
3.Kısım 2023 döndürür

"""

####

""" TC numarasını maskeleme örneği """
identification_number = input("TC nizi giriniz :")
# 1.Yöntem
first_char = identification_number[:2]
last_char = identification_number[-2:]
masked_part = len(identification_number) - len(first_char) - len(last_char)

print(first_char + '#' * masked_part + last_char)

# 2.Yöntem
first_char = identification_number[:2]
last_char = identification_number[-2:]
masked_to_be_part = identification_number[len(first_char): -len(last_char)]
masked_part = masked_to_be_part.replace(masked_to_be_part, "#" * len(masked_to_be_part))

print(first_char + masked_part + last_char)


