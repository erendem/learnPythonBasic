""" Exercise 1

gelen sayıları toplayıp döndüren method yazılacak ancak;

method çağrılırken liste gönderilirse içindeki elemanlar toplanacak ayrı eğer tek tek sayılar gönderililirse sayıların kendileri toplanacak.

"""

def sum_of_numbers(*args):
    result_sum = 0
    for i in args:
        if type(i) in [tuple,list]:
            result_sum += sum(i)
        elif type(i) is int:
            #sum methodu çalışmaz çünkü sum methodu yalnızca list, tuple gibi iterable'ların içindeki elemanlarını toplar.
            result_sum += i
        else: #yani methoda gönderilen değer int veya liste değildir o halde toplama işlemi yapılamaz.
            pass

    return result_sum

print(sum_of_numbers(1,2,3,4)) # 10 dönmeli toplamı.
print(sum_of_numbers([5,10])) # 15 dönmeli toplamı.
print(sum_of_numbers([5,10], [50,65])) # 130 dönmeli toplamı.
print(sum_of_numbers('a', 'b')) # 0


""" Exercise 2

"""

def student_information():
    student_info = [
                {'name':'eren', 'student_no': 10, 'note': 85},
                {'name':'ahmet', 'student_no': 15, 'note': 75},
                {'name':'elif', 'student_no': 20, 'note': 87},
                {'name':'aylin', 'student_no': 37, 'note': 27},
                {'name':'cengiz', 'student_no': 43, 'note': 27},
                {'name':'eren', 'student_no': 63, 'note': 36},
                {'name':'ayşe', 'student_no': 55, 'note': 79},]


    return student_info


def view_student_name(student_list):
    result = ""
    for i in student_list:
        result += i.get('name') + " " + str(i.get("student_no")) + "\n"
    return result


def some_operation_for_note(student_list, operation_type):
    note_list = [i.get('note') for i in student_list]

    if operation_type == 'max':
        max_note = max(note_list)
        max_note_students = list(filter(lambda l: l.get('note') == max_note, student_list))
        max_note_students_name = [name.get('name') for name in max_note_students]
        result = "{} - {}".format(max_note, max_note_students_name)
        return result
    elif operation_type == 'min':
        min_note = min(note_list)
        max_note_students = list(filter(lambda l: l.get('note') == min_note, student_list))
        max_note_students_name = [name.get('name') for name in max_note_students]
        result = "{} - {}".format(min_note, max_note_students_name)
        return result
    else:
        return round(sum(note_list) / len(note_list), 3)


student_info_list = student_information()
while True:
    input_from_user = input("Yapmak istediğiniz işlemi seçiniz :" "\n"
                            "Öğrenci listesi için lütfen 'v' basınız. " "\n"
                            "Not ortalamasını görmek için 'a' basınız ""\n"
                            "En yüksek alan öğrenci için 'max' yazınız" "\n"
                            "En düşük alan öğrenci için 'min' yazınız" "\n"
                            "Öğrenci eklemek için 'add' yazınız" "\n"
                            "Çıkış için 'q' ya basınız."
                            "\n"
                            "\n"
                            "")

    if input_from_user == 'q':
        break

    elif input_from_user == 'v':
        s_list_return = view_student_name(student_info_list)
        print(s_list_return)

    elif input_from_user == 'a':
        average = some_operation_for_note(student_info_list, 'a')
        print("Sınıf ortalaması : ", average )

    elif input_from_user == 'max':
        max_note = some_operation_for_note(student_info_list, 'max')
        print("En yüksek alan : ", max_note)

    elif input_from_user == 'min':
        min_note = some_operation_for_note(student_info_list, 'min')
        print("En düşük alan : ", min_note)

    elif input_from_user == 'add':
        name = input("Öğrenci ismi giriniz")
        student_no = input("Öğrenci numarasını giriniz")
        student_note = input("Note giriniz")
        student_info_list.append({'name': name, 'student_no':student_no,'note':student_note })
