class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# Пример использования
if __name__ == "__main__":
    library = Library()
    print(library.get_next_book_id())  # Вывод: 1

    # Добавим книгу для примера
    book1 = Book(1, "Первая книга", 100)
    library.books.append(book1)

    print(library.get_next_book_id())  # Вывод: 2
    print(library.get_index_by_book_id(1))  # Вывод: 0
    # print(library.get_index_by_book_id(2))  # Вызывает ValueError
