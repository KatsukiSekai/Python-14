car = {"brand" : "Ford" , 
    "model" : "Mustang" ,
    "year" : 1964
}
print(car["brand"])
print(car)
x = car.keys()
print(x)
#เพิ่มค่าใน Dic
car["color"] = "white"
print(car)
#แก้ค่าใน Dic
car["color"] = "red"
print(car)
#การ Update Dic
car.update({"light" : "blue"})
print(car)
#การลบค่าใน Dic
car.pop("light")
print(car)
del car["color"]
print(car)
#เพิ่่มค่า Dic แบบ List
car.update ({"part" : ["body" , "wheel" , "light"]})
print(car)
#เพิ่มค่าdicแบบ  Nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child1']['year'])