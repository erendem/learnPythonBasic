"""
Modüller kısa tanımıyla hazır fonksiyon paketleridir.
Sıklıkla kullanılan fonksiyonları, projeye dahil ederek kendimiz yazmadan hazır kullanarak zamandan tasarruf etmemizi sağlar.


"""

def calc_factorial(n):
    # total = 1
    # while n>1:
    #     total *= n
    #     n -= 1
    # print(total)

    multiplier = 1
    for i in range(n,1,-1):
        multiplier *= i
    print(multiplier)

# calc_factorial(5)

"""Math Modulü"""
import math
factorial_result = math.factorial(5)
# print(factorial_result)
# print(math.e)
# print(math.pi)
# print(math.log(10))
# print(math.log10(10))
# print(math.sin(0.5))
# print(math.ceil(5.12))
# print(math.floor(5.12))

"""Time/Datetime Modülü"""

import time
import pytz
from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta


""" çalıştırdığınız kodun zamanını ölçebilirsiniz """
# start_date = time.time()
# number_list = []
# for i in range(1000000):
#     number_list.append(i)
# end_date = time.time()
# print(end_date - start_date)



a = time.ctime()
b = time.strftime('%d.%m.%Y - %H:%M:%S') #time'ı stringe/yazıya çevirerek format vermenizi sağlar

current_time = datetime.now()
current_date = current_time.date()

# Zamanlara gün eklemek veya çıkarmak timedelta iledir.
five_days_later = current_date + timedelta(days=5)
five_days_ago = current_date - timedelta(days=5)
twenty_min_ago = current_date - timedelta(minutes=20)

#spesifik hafta veya ay eklenecekse relative delta kullanılabilir time delta sadece gün ve dakika eklenebilir
three_week_later = current_date + relativedelta(weeks=3)

# print(pytz.common_timezones)
#spesifik bir yerdeki zamanı almak için time zone parametresi gönderilmelidir örnek Americayı gönderirsek
print(datetime.now(pytz.timezone('America/Dawson')))

#tarihleri stringe istediğiniz şekliyle formatlamak için strftime
x = datetime.strftime(datetime.now(pytz.timezone('America/Dawson')), "%d.%m.%Y - %H:%M:%S")
#string olan bir değişkeni tekrar date objesine cast etmek için : strptime
cgg = datetime.strptime(x, "%d.%m.%Y - %H:%M:%S")
# print(type(cgg))
# print(type(x))
# print(cgg.hour)
# print(datetime.now(pytz.timezone('Europe/Istanbul')))
str_date = '2023-08-12'
date_obj = datetime.strptime(str_date, '%Y-%m-%d')
# print(datetime.strftime(date_obj, '%d/%m/%Y'))
# print(datetime.now())
# print(type(date_obj))

# Bir önceki ayın son gününü bulur replace methodu ile günü ayı ve yılı değiştirebilirsiniz.
aaa = datetime.now().replace(day=1) - timedelta(days=1)
# print(aaa)

#calendar modülüyle ile de spesifik ayın son günü bulunabilir.
""" calendar.monthrage methodu 2 parametre alır ilk parametresi current yıl'dır ikincisi ise aydır.
    yıl ve ay gönderilen değişkenleri method tuple şekliyle başladığı günü(yani o ayın ilk günü hangi gün başlıyorsa indexini döndürür
     mesela salı başlıyorsa 1 çarşamba başlıyorsa 2yi döndürür) ve ayın son gününü döndürür(28 mi 30 mu çektiğini).
"""
f = calendar.monthrange(datetime.now().year, datetime.now().month)
print(f) #ayın son günü için >> f[1]


""" Random modülü """

import random
randoming_str = 'abcdefg'
random_two_string = random.choices(randoming_str, k=2)
#random.sample ve random.choice, random.choices benzer methodlardır random modülünün çokça metodu vardır internetten açıklamalarıyla okunabilir.
print(random_two_string)

some_random_int = random.randint(1,100) # 1 ile 100 arasında rastgele sayı üretir