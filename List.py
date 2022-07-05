from audioop import reverse


fruits = ["apple" , "banana" , "cherry" , "watermelon" , "blueberry"]
print(fruits[1])

fruits[1] = "blackcurrants"
fruits[1:3] = ["blackcurrants","watermelon"]

fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical = ["mango" , "pineapple" , "papaya"]
fruits.extend(tropical)
print(fruits)

fruits.remove("watermelon")
print(fruits)
fruits.pop(1)
print(fruits)
#del fruits
fruits.sort(reverse = True)
print(fruits)
#ชนะชัย สังข์ศิริ 6/14 8