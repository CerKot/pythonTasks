import Task2.Task2_1.solution_loops as s_p
import Task2.Task2_1.solution_comprehensions as s_c
from Task2.Task2_1.data import library_archive, crew_members, ship_systems

def test_self_get_sci_fi_books():
    sci_fi_books = [("Марсианин", "Энди Вейер", 2011, 384, "Научная фантастика"),
                    ("Дюна", "Фрэнк Герберт", 1965, 412, "Научная фантастика"),
                    ("Левая рука тьмы", "Урсула Ле Гуин", 1969, 304, "Научная фантастика"),
                    ("Проект 'Феникс'", "Энди Вейер", 2021, 476, "Научная фантастика"),
                    ]
    assert (s_p.get_sci_fi_books(library_archive) == sci_fi_books)

def test_get_sci_fi_books():
    assert s_p.get_sci_fi_books(library_archive) == s_c.get_sci_fi_books(library_archive)

def test_get_short_book_titles():
    assert s_p.get_short_book_titles(library_archive) == s_c.get_short_book_titles(library_archive)

def test_get_books_by_author():
    assert s_p.get_books_by_author(library_archive) == s_c.get_books_by_author(library_archive)

def test_get_avg_page_count_from_library():
    assert s_p.get_avg_page_count_from_library(library_archive) == s_c.get_avg_page_count_from_library(library_archive)

def test_get_avg_exp_by_job():
    assert s_p.get_avg_exp_by_job(crew_members) == s_c.get_avg_exp_by_job(crew_members)

def test_get_high_salary_members():
    assert s_p.get_high_salary_members(crew_members) == s_c.get_high_salary_members(crew_members)

def test_get_member_count_of_systems():
    assert s_p.get_member_count_of_systems(crew_members,ship_systems) == s_c.get_member_count_of_systems(crew_members,ship_systems)

def test_get_member_bonuses():
    assert s_p.get_member_bonuses(crew_members) == s_c.get_member_bonuses(crew_members)

def test_get_little_system():
    assert s_p.get_little_systems(ship_systems) == s_c.get_little_systems(ship_systems)

def test_get_member_list():
    assert (s_p.get_member_list(crew_members,
                                ship_systems,
                               )
            == s_c.get_member_list(crew_members,
                                   ship_systems,
                                    )
            )




