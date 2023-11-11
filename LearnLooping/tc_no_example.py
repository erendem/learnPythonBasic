"""
1.Kural: 11 Haneli olacak
2.Kural : 0 ile başlayamaz
3.Kural : 1,3,5,7,9 hanelerinin toplamının 7 katı 2,4,6,8 hanelerinin
    toplamından çıkarılınca mod10'u 10'ncu haneyi vercek

4.Kural : ilk on hanesinin toplamının mod10'u 11nci haneyi verir.


"""

while True:
    tc_no_from_user = input("Geçerli TC Giriniz : ")
    if len(tc_no_from_user) > 0 and tc_no_from_user[0] == '0':
        print("İlk hanesi 0 ile başlayamaz")
        continue

    if not len(tc_no_from_user) == 11:
        print("Lütfen 11 haneli bir numara giriniz")
        continue

    if not tc_no_from_user.isdigit():
        print("Yalnızca Numeric değerler giriniz")
        continue

    odd_str = tc_no_from_user[:10:2]
    even_str = tc_no_from_user[1:9:2]

    # for o in odd_str:
    #     odd_number.append(int(o))
    odd_number = [int(o) for o in odd_str]
    sum_of_odd = sum(odd_number)

    # for e in even_str:
    #     even_number.append(int(e))
    even_number = [int(e) for e in even_str]
    sum_of_even = sum(even_number)

    if ((sum_of_odd * 7) - sum_of_even) % 10 != int(tc_no_from_user[-2]):
        print("10ncu hanen yanlış !")
        continue
    first_ten_digit = tc_no_from_user[:-1]

    # for f in first_ten_digit:
    #     first_ten_digit_list.append(int(f))
    first_ten_digit_list = [int(f) for f in first_ten_digit]
    sum_of_ten_digit = sum(first_ten_digit_list)

    if sum_of_ten_digit % 10 != int(tc_no_from_user[-1]):
        print("Son hane hatalı")
        continue
    break

print("TC No oluşturuldu : {}".format(tc_no_from_user))