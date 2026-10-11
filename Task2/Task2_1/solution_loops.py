from typing import Callable

from Task2.Task2_1.data import ship_systems


#Part A

def get_sci_fi_books(library_archive: tuple[str,str,int,int,str]) -> list[tuple]:
    sci_fi_books = []
    for title,name,year,pages,genre in library_archive:
        if genre == "Научная фантастика":
            sci_fi_books.append((title,name,year,pages,genre))
    return sci_fi_books

def get_short_book_titles(library_archive: tuple[str,str,int,int,str]) -> list[str]:
    book_titles = []
    for title, *_ in library_archive:
        book_titles.append(title)
    short_books_before_1950 = []
    for title,_,year,pages,_ in library_archive:
        if year <= 1950 and pages < 300:
            short_books_before_1950.append(title)

    return short_books_before_1950

def get_books_by_author(library_archive: tuple[str,str,int,int,str]) -> dict:

    books_by_author = {}
    for _, author, *_ in library_archive:
        answer = []
        for title, a, *_ in library_archive:
            if a == author:
                answer.append(title)
        books_by_author[author] = tuple(answer)

    return books_by_author

def get_avg_page_count_from_library(library_archive: tuple[str,str,int,int,str]) -> float | None:
    page_count = 0
    for *_,pages,_ in library_archive:
        page_count += pages
    avg_page_count = None if not library_archive else page_count / len(library_archive)
    return avg_page_count

#Part B
#1
def get_avg_exp_by_job(crew_members:list[tuple]) -> dict:
    jobs = set()
    for _, job, *_ in crew_members:
        jobs.add(job)

    avg_exp_by_job = {}
    for job in jobs:
        avg_exp = 0
        worker_count = 0
        for _, j, year, _ in crew_members:
            if j == job:
                avg_exp += year
                worker_count += 1
        avg_exp_by_job[job] = avg_exp / worker_count if worker_count else None
    return avg_exp_by_job

#2
def get_high_salary_members(crew_members:list[tuple])->list:
    high_salary_members = []
    for name,_,exp,salary in crew_members:
        if salary > 5000 and exp < 10:
            high_salary_members.append(f'{name}:{salary}')
    return high_salary_members

#3
def get_member_count_of_systems(crew_members:list[tuple],
                                ship_systems:dict) -> dict:
    member_names = []
    for name, *_ in crew_members:
        member_names.append(name)

    member_count_of_systems = {}
    for member in member_names:
        for system in ship_systems:
            if member in ship_systems[system]:
                member_count_of_systems[member] = member_count_of_systems.get(member,0) + 1
    return member_count_of_systems

#4
def get_member_bonuses(crew_members: list[tuple]) -> dict:
    member_bonuses = {}
    for name,_,exp,salary in crew_members:

        if exp <= 5:
            member_bonuses[name] = salary * 0.1
        else:
            member_bonuses[name] = salary * 0.15
    return member_bonuses

#5
def get_little_systems(ship_systems: dict) -> list:
    little_systems = []
    for system in ship_systems:
        if len(ship_systems[system]) < 2:
            little_systems.append(system)
    return little_systems

#6
def get_member_list(crew_members: list[tuple],
                    ship_systems: dict,
                    get_member_count_of_systems: Callable,
                    get_member_bonuses: Callable) -> list:

    member_list = []
    for name, job, age, salary in crew_members:
        member_list.append(
            {name : (
                     job, age, salary,
                     get_member_count_of_systems(crew_members,ship_systems),
                     get_member_bonuses(crew_members)
                     )
             }
        )
    return member_list




