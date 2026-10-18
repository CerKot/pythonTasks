import Task2.Task2_1.solution_loops as s_p
import Task2.Task2_1.solution_comprehensions as s_c


def test_get_sci_fi_books():
    assert s_p.get_sci_fi_books([]) == s_c.get_sci_fi_books([])

def test_get_short_book_titles():
    assert s_p.get_short_book_titles([]) == s_c.get_short_book_titles([])

def test_get_books_by_author():
    assert s_p.get_books_by_author([]) == s_c.get_books_by_author([])

def test_get_avg_page_count_from_library():
    assert s_p.get_avg_page_count_from_library([]) == s_c.get_avg_page_count_from_library([])

def test_get_avg_exp_by_job():
    assert s_p.get_avg_exp_by_job([]) == s_c.get_avg_exp_by_job([])

def test_get_high_salary_members():
    assert s_p.get_high_salary_members([]) == s_c.get_high_salary_members([])

def test_get_member_count_of_systems():
    assert s_p.get_member_count_of_systems([],{}) == s_c.get_member_count_of_systems([],{})

def test_get_member_bonuses():
    assert s_p.get_member_bonuses([]) == s_c.get_member_bonuses([])

def test_get_little_system():
    assert s_p.get_little_systems({}) == s_c.get_little_systems({})

def test_get_member_list():
    assert (s_p.get_member_list([],
                                {},
                                s_p.get_member_count_of_systems,
                                s_p.get_member_bonuses
                               )
            == s_c.get_member_list([],
                                   {},
                                   s_c.get_member_count_of_systems,
                                   s_c.get_member_bonuses)
            )
