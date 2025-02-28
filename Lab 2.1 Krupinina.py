class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

# Пример использования
if __name__ == "__main__":
    book = Book(1223477896, "Класс Book", 200)
    print(str(book))  # Вывод: Книга "Класс Book"
    print(repr(book))  # Вывод: Book(id_=1223477896, name='Класс Book', pages=200)
