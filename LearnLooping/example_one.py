"""
a = input("username ")
username =
1- En fazla 15 karakter en az da 5 karakter girebilsin
2- En az 1 tane büyük harf olsun
3- Yalnızca harf içersin(numara sembol içermesin)

Password =
1. En az 2 tane özel karakter
2. özel karakter dışında ve numara dışında bir parola belirlenemesin
3. 5-10 arasında uzunluğu olsun

merhaba {username} kaydınız başarılı
parolanız {1*****9}

"""

import string
while True:
    username = input("Kullanıcı ismi giriniz : ")
    if len(username) > 15:
        print("Girdiğiniz username çok uzun lütfen tekrar giriniz")
        continue
    elif len(username) < 5:
        print("Girdiğiniz username çok kısa lütfen tekrar giriniz")
        continue

    upper_list = []
    for letter in username:
        if letter.isupper():
            upper_list.append(letter)
    if len(upper_list) == 0:
        print("Büyük harf içermedi kullanıcız tekrar belirleyiniz")
        continue

    if not username.isalpha():
        continue
    break

special_char = string.punctuation
while True:
    password = input("Parola giriniz : ")
    special_list = ''
    is_char_or_special_char = False
    for p in password:
        if p in special_char:
            special_list += p
        if p not in special_char and not p.isdigit():
            is_char_or_special_char = True

    if len(special_list) < 2:
        print("Özel karakter içermeli en az 2 tane")
        continue
    if is_char_or_special_char:
        print("özel karakter ve numara dışında bir karakter girilemez")
        continue

    if not 5 < len(password) < 10:
        print("5 ile 10 arasında parola belirleyiniz")
        continue
    break


print("Merhaba {} adında kullanıcınız oluşuturulmuştur\n parolanız {}".format(username, password))