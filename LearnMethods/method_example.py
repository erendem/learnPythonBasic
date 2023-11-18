"""
syntax : def method_name(params):
            "docstring"
            ...

"""

def print_hello():

    print("Hello World")

print_hello()

""" params 
   :str bu parametreye string gelmesi gerektiğine yazılımcıya verilen ipucudur.
   ancak integer da yollanmış olsa hata vermez sadece ipucu örnek verilmesi için parametrelerin type'ları belli edilebilir.
"""
def print_hello(message:str):
    """ This methods displays parametric message on screen """
    print(message)

#print_hello() # -->  err > parametre gönderilmedi
print_hello("Hello World !")
print_hello(123) # Ide sarı çizer ama method çalışır hata döndürmez


def print_some_values(x, y):
    print(x, y)

print_some_values(1, 2) # --> positional arguments sırayla yazar
print_some_values(x= 2, y= 1) # --> keyword arguments değerleri yazar sıralama önemli değil


returning_value_of_method = print_some_values(1, 2)
print(returning_value_of_method) # içinde bir şey return etmeyen her method None döndürür.


def calculate_numbers(x, y):
    return x + y


total_numbers = calculate_numbers(3,6)
print(total_numbers)

"""*args and **kwargs

args: argument list, bir demet elemanı parametre olarak karşılar.(Tuple olarak alır)
kwargs : keyword argument list, bir demet elemanları keywords şeklinde parametre karşılar.

"""

def args_example(*args):
    print(args)


args_example(1,23,4,345,46,423,432,1) # hepsi args a gider
args_example([1,2,34,5,6,7,8,89], 66)
args_example(*[1,2,34,5,6,7,8,89], 66) # * işareti listeyi açarak gönderir yani içindeki elemanların herbirini tek tek paramsa gönderir.
                                        # * gönderilmezse tüm liste tek bir ayrı elamanmış gibi parametreyi karşılar.

def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(a=5, b=3, c=4)
kwargs_example(**{'a': 5, 'b': 3, 'c': 4}) #kwargs her zaman dictionary key:value yapısı bekler eğer '**' ile dictionary gönderirseniz hata verir.
                                        # Çünkü normal positional parametre gibi algılar


def args_and_kwargs_example(*args, **kwargs):
    """args and keywords args example"""
    print("args :", args, "Kwargs : ", kwargs)


print(help(args_and_kwargs_example))
args_and_kwargs_example(1,23,53,5,3,2, *[9,8,7], a=5, b=3, **{'c': 7, 'd': 16})


""" Lambda Fonksiyonları 
Tek satırda yazılan fonksiyon görevi gören, isimsiz methodlardır.
"""

x = lambda l: l + 10

x(10) # 20 döner 'l' oradaki parametresidir ve 10 gönderilirse l+10 dan 20 döner.

y = lambda : print("Argüman almadan çıktı verir")
y() # çağırırken değişken göndermedik çünkü herhangi bir aldığı parametre yok doğrudan ekrana yazı yazar.



"""
Hata yakalama

try:
 "Hataya sunduğumuz kod alanı"
except:
  "Eğer try kısmında bir hata ile karşılaşılırsa burası çalışır"
else:
    "Except çalışmıyorsa burası çalışır"
finally:
    "Her zaman çalışır"

"""
def calculate_division_num(x,y):
    try:
        result = x / y
    except:
        print("Division cannot be zero")
        return
    else:
        print("Else Düştü")
    finally:
        print("Çalışır")
    return result

# print(calculate_division_num(5,3))
# print(calculate_division_num(5,0))
