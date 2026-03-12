class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

krug = Circle(10)
print("Сейчас радиус =", krug.get_radius())

print("Меняем...")
krug.set_radius(20)
print("Сейчас радиус =", krug.get_radius())


