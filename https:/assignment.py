#Class1: Car
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        return f"The {self.color} {self.brand} {self.model} engine has started."

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), Color: {self.color}"


# Class 2: Student
class Student:
    def __init__(self, name, age, student_id, major):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.major} major."

    def is_adult(self):
        return self.age >= 18


# Class 3: Book
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def description(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}"

    def is_long(self):
        return self.pages > 300


# Sample usage (optional)
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2020, "Blue")
    print(car.start_engine())
    print(car.get_info())

    student = Student("Loteni", 24, "22118644", "Engineering")
    print(student.introduce())
    print("Adult:", student.is_adult())

    book = Book("1984", "George Orwell", 328, "Dystopian")
    print(book.description())
    print("Is long:", book.is_long())
