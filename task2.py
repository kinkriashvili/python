# excercise 1


# class Book:
#     def __init__(self, name, author, makeyear, numberpage):
#         self.name = name
#         self.author = author
#         self.makeyear = makeyear
#         self.numberpage = numberpage
#
#     def info(self):
#         print(f'წიგნის სახელია {self.name}, მისი ავტორია {self.author}, გამოშვებულია {self.makeyear} წელს, '
#               f'წიგნის გვერდების რაოდენობაა - {self.numberpage}')
#
#     def get_name(self):
#         return self.name
#
#     def set_author(self, value):
#         self.author = value
#
#     def get_makeyear(self):
#         return self.makeyear
#
#     def set_numberpage(self, text):
#         self.numberpage = text
#
#
# name = input('Enter the name of book: ')
# author = input('Enter the author of this book: ')
# makeyear = int(input('Enter the year of publication of this book: '))
# numberpage = int(input('Enter the number of pages: '))
#
# obj1 = Book(name, author, makeyear, numberpage)
# obj1.info()
#
# obj1.get_name()
# obj1.set_author('J.K Rowling')

# excercise 2


# excercise 3


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'ცხოველის სახელია {self.name}, ხოლო მისი ასაკი არის - {self.age}')
#
#
# class Dog(Animal):
#     def __init__(self, breed, color, name, age):
#         super().__init__(name, age)
#         self.breed = breed
#         self.color = color
#
#     def info(self):
#         print(f'ცხოველის სახელია {self.name}, მისი ასაკია - {self.age}, '
#               f'ჯიშია - {self.breed}, ხოლო ფერი - {self.color}')
#
#     def get_breed(self):
#         return self.breed
#
#     def set_color(self, value):
#         self.color = value
#
#
# dog1 = Dog("პუდელი", 'ვარდისფერი', 'ნენე', 2)
# dog1.info()
#
# dog2 =Dog('დალმანტინელი', 'შავ-თეთრი', 'ნეკა', 3)
# dog2.info()



# excercise 4

# class CallMixin:
#     def call(self):
#
#
# class Person(CallMixin):
#     def __init__(self):
#         self.fname = fname
#         self.lname = lname
#         self.phone = phone
#
#     def info(self):
#         print(f'პიროვნების სახელია {self.fname}, გვარია - {self.lname}, ტელეფონის ნომერია - {self.phone}')


