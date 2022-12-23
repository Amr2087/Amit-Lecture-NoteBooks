class Rectangle:
    height = 0
    width = 0

    def area(self):
        area_calc = self.height * self.width
        return area_calc

    def perimeter(self):
        perimeter_calc = 2 * (self.height + self.width)
        return perimeter_calc

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width


height_usr = int(input("Enter Height : "))
width_usr = int(input("Enter Width : "))

rec = Rectangle()
rec.set_width(width_usr)
rec.set_height(height_usr)

if height_usr == width_usr:
    print("That's a Square ")

else:
    area1 = rec.area()
    print(f"Area = {area1}")
    perimeter1 = rec.perimeter()
    print(f"Perimeter = {perimeter1}")
