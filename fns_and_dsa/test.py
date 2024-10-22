# class student:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age

#     def student_information(self):
#         print (f"sudent name is {self.name} while the age is {self.age}")
    
# my_guy = student("joseph", 25)
# my_guy.student_information()

# class product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value_product(self):
#         return self.price * self.quantity
    
#     def desplay_info(self):
#         print(f"name of the product = {self.name}")
#         print(f"price of product = {self.price}")
#         print(f"qualtity of product = {self.quantity}")
#         print(f"the total product value = {self.total_value_product()}")

# product1 = product("tomatoes", 25, 40)

# product1.desplay_info()
# import gc

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # def speak(self):
#     def __str__(self):
#         return f"my name is {self.name}, i am {self.age} years old"


# result = Person("joseph", 23)
# print(result)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         return f"My name is {self.name}, I am {self.age} years old."
    
#     def __del__(self):
#         print(f"I am sorry, you have been deleted {self.name}")

# # Create an object of Person
# result = Person("Joseph", 23)
# print(result.speak())

# # Explicitly delete the object to trigger the __del__ method
# del result

# class Book:
#     total_books = 0

#     def __init__(self, name):
#         self.name = name
#         Book.total_books +=1   

#     @classmethod
#     def display_total_books(cls):
#         print (f"the total number of books is {cls.total_books}")

# book1 = Book("daramola")
# book2 = Book("joseph")
# book3 = Book("doyin")

# print(Book.display_total_books())

class calculator:
    @staticmethod
    def add(x, y):
       result = x + y
       return result

    @staticmethod
    def multiply(x, y):
        result = x * y
        return result

print(calculator.add(3, 4))
print(calculator.multiply(3, 4))
        