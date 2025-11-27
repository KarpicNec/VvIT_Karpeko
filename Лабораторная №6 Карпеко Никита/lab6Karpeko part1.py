class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # "__что-то" = приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль был изменен!")

    def check_password(self, password):
        return password == self.__password


user = UserAccount("Nikita_Karp", "some@mail.ru", "qwerty123")

#Проверка пароля
print(user.check_password("qwerty123"))  
print(user.check_password("wrong_pass"))  

#Изменим пароль
user.set_password("123qwErty")
    
#Проверка нового пароля
print(user.check_password("123qwErty"))  
print(user.check_password("qwerty123"))  
