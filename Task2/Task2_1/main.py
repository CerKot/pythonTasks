import Task2.Task2_1.solution_loops as s_p
import Task2.Task2_1.solution_comprehensions as s_c

from data import library_archive,crew_members,ship_systems

from collections.abc import Iterable


def print_collection(collection: Iterable, description: str):
    print(description)
    for el in collection:
        print(*el)
    print()

def print_sci_fi_books(library_archive):
    sci_fi_books = s_c.get_sci_fi_books(library_archive)
    print_collection(sci_fi_books,
                     "Книги -- научная фантастика:")

def print_short_book_titles(library_archive):
    short_book_titles = s_c.get_short_book_titles(library_archive)
    print_collection(short_book_titles,
                     "Книги короче 300 страниц и старше 1950 года:")

def print_books_by_author(library_archive):
    books_by_author = s_c.get_books_by_author(library_archive)
    print_collection(books_by_author,
                     "Список книг каждого автора:")

def