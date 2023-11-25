""" kullanıcıdan alınan iki tarih arasındaki yalnızca haftaiçlerini bulan algoritma """

from datetime import datetime, timedelta

first_date_from_user = input("Başlangıç tarihi giriniz : (d.m.Y) formatında ")
end_date_from_user = input("Bitiş tarihi giriniz : (d.m.Y) formatında ")

#kullanıcınn girdiği tarihler string onları date'e cast etmeliyiz.
first_date = datetime.strptime(first_date_from_user, "%d.%m.%Y")
end_date = datetime.strptime(end_date_from_user, "%d.%m.%Y")

#arasında kaç gün varsa o kadar dönmeliyiz ki tarihleri bulalım
between_days = (end_date - first_date).days

between_dates_except_weekend = []
for d in range(between_days+1):
    date = first_date + timedelta(days=d)
    if date.weekday() not in (5,6): # weekday methodu günün indeksini döndürür cumartesi ve pazar indeksi 5ve6'dır
        between_dates_except_weekend.append(date)

print(between_dates_except_weekend)
