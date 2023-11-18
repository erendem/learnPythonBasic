"""
Tuple immutable data tipleridir. "()" Yani program akışı boyunca elemanları değiştirilemez.
Ordered data koleksiyonlarıdır. Tuttuğu elemanların index ve yerleri kaydedilir ve sıralanır.
Listelerdeki gibi farklı data türlerini barındırabilir.
"Tuple olabilmesi için en az bir tane virgül olması gerekmektedir.
('eren') --> tuple object değil
('eren',) --> Tuple object

Tuple ve List arasındaki en önemli fark List'lerin mutable olması, tuple'ların ise immutable olmasıdır.
onun dışında tuple'lar doğrudan memory erişimleri listelere göre çok daha hızlı olduğundan hızlı çalışır.

"""

empty_tuple = ()

print(type(empty_tuple))

numbers = (1, 2, 3, 4, 'eren', True)
print(numbers)

names = 'eren', 'ahmet', 'mehmet', 'osman'
print(names)

print(names[0])

a, b, c, d = names
print(a,b,c,d)


indexing_tuple_same_as_list = (1,2,3,4,5,6,7)
print(indexing_tuple_same_as_list[1:4])
print(indexing_tuple_same_as_list[-1])
print(indexing_tuple_same_as_list[::-1])