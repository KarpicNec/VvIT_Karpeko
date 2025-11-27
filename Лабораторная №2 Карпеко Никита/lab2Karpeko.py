def greet(name):
    print("Здравствуйте,", name)

greet("Марина Сергеевна")

def square(number):
    return number * number

print(square(25))

def max_of_two(x, y):  # return max(x, y)
    if x > y:
        return x
    return y

print(max_of_two(15, 2501))

def describe_person(name, age=30):
    print ("Имя данного человека:", str(name + ';'), "Возраст:", age)

describe_person("Никита Кологривый")
describe_person("Владимир Владимирович", 72)

def is_prime(number):
   i = 2
   while i * i <= number:
       if number % i == 0:
           return False
       i += 1
   return True
   
print(is_prime(29))
print(is_prime(190))