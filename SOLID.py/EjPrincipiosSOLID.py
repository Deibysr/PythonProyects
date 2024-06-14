# Principio de Responsabilidad Única (SRP)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

# Principio Abierto/Cerrado (OCP)
class LibraryInventory:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

# Principio de Sustitución de Liskov (LSP) & Principio de Inversión de Dependencia (DIP)
class Loanable:
    def check_out(self, member):
        pass

    def check_in(self):
        pass

class LoanableBook(Book, Loanable):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.is_checked_out = False
        self.current_member = None

    def check_out(self, member):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.current_member = member
            return True
        return False

    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.current_member = None
            return True
        return False

# El Principio de Segregación de Interfaces (ISP) es implícito en este diseño, ya que Python no requiere la implementación
# de interfaces explícitas y podemos diseñar nuestras clases para cumplir solo con las responsabilidades que necesitan.
