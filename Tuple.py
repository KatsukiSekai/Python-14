fruit = ("apple" , "banana" , "cherry")
print(fruit[0])
fruit = ("apple" , "banana" , "cherry" , "orange" , "kiwi" , "melon" , "mango")
print (fruit[2:5])
print (fruit[:5])
print (fruit[2:])
#เพิ่มค่าใน tuple
x = ("apple" , "banana" , "cherry")
y = list(x) #แปลงค่าเป็น List แล้วเก็บค่าเข้า y
y[1] = "kiwi"
x = tuple(y) #แปลงค่า List เป็น tuple แล้วกลับมาเก็บค่าที่ x
print = (x)
#ลบค่าใน Tuple
x = ("apple" , "banana" , "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#join
tuple1 = ("a" , "b" , "c")
tuple2 = (1 , 2 , 3)
tuple3 = tuple1 + tuple2
print(tuple3)
x = range(3 , 6)
for n in x:
    print(n)
x = range(3 , 20 , 5)
for n in x:
    print("rangeแบบstep2:" , n)
#นายชนะชัย สังข์ศิริ 6/14 8