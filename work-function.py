from cmath import pi

def square(width,height):
    return  width * height
def triangle(base,height):
    return  0.5 * base * height
def circle(radius):
    return  pi * radius * radius
sq = square(width = int(input("กรอกค่าความกว้าง : ")),height = int(input("กรอกค่าความสูง : ")))
print (sq)
tr = triangle(base = int(input("กรอกค่าความยาวฐาน : ")),height = int(input("กรอกค่าความสูง : ")))
print (tr)
cr = circle(radius = int(input("กรอกค่ารัศมี : ")))
print (cr)
#นายชนะชัย สังข์ศิริ 6/14 8