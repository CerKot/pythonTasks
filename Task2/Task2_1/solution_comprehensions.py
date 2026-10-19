#Part A


def get_sci_fi_books(library_archive: list[tuple[str,str,int,int,str]]) -> list[tuple]:
    """A1: произведения жанра «Научная фантастика» (полные кортежи)."""
    return [(title,name,year,pages,genre)
                    for title,name,year,pages,genre in library_archive
                    if genre == "Научная фантастика"]


def get_book_titles(library_archive: list[tuple[str,str,int,int,str]]) -> list[str]:
    """A2: названия научно-фантастических произведений."""
    return [title for title,name,year,pages,genre in library_archive]



def get_short_book_titles(library_archive: list[tuple[str,str,int,int,str]]) -> list[str]:
    """A3: названия книг, изданных до 1950 года и короче 300 страниц."""
    short_books_before_1950 = [title
               for title,_,year,pages,_ in library_archive if year <= 1950 and pages < 300]
    return short_books_before_1950



def get_books_by_author(library_archive: list[tuple[str,str,int,int,str]]) -> dict:
    """A4: автор -> список его произведений."""
    return {author: [(title,name,year,pages,genre) for (title,name,year,pages,genre) in library_archive if name == author]
            for author in dict.fromkeys(name for (title,name,year,pages,genre) in library_archive)}


def get_avg_page_count_from_library(library_archive: list[tuple[str,str,int,int,str]]) -> float | None:
    """A5: среднее число страниц; для пустой коллекции — None."""
    avg_page_count = (
                      sum((pages for _,_,_,pages,_ in library_archive)) / len(library_archive)
                      if library_archive else None
                      )
    return avg_page_count


#Part B


def get_avg_exp_by_job(crew_members:list[tuple]) -> dict:
    """B1: должность -> средний стаж."""
    avg_exp_by_job = {targ_job:
                     sum(exp for _,job,exp, _ in crew_members if job == targ_job) /
                     len([_ for _,job,*_ in crew_members if job == targ_job])
                 for _,targ_job,*_ in crew_members}
    return avg_exp_by_job

#2

def get_high_salary_members(crew_members:list[tuple])->list:
    """B2: строки «Фамилия: Зарплата» для зарплаты > 5000 и стажа < 10 лет."""
    high_salary_members = [f'{name}:{salary}' for name,_,exp,salary in crew_members
                  if salary > 5000 and exp < 10]
    return high_salary_members


#3

def get_member_count_of_systems(crew_members: list[tuple],
                                ship_systems: dict) -> dict:
    """B3: фамилия -> число систем."""
    member_names = [name for name, *_ in crew_members]
    member_count_of_systems = {member: len([syst_name for syst_name in ship_systems
                                            if member in ship_systems[syst_name]])
                               for member in member_names
                               }
    return member_count_of_systems


#4

def get_member_bonuses(crew_members: list[tuple]) -> dict:
    """B4: фамилия -> премия (10 %, при стаже более 5 лет — 15 %)."""
    member_bonuses = {name:(salary * 0.1 if age <=  5 else salary * 0.15)
                      for name,_,age,salary in crew_members
                      }
    return member_bonuses


#5

def get_little_systems(ship_systems: dict) -> list:
    """B5: системы, за которые отвечает меньше двух сотрудников."""
    little_systems = [system for system in ship_systems if len(ship_systems[system]) < 2]
    return little_systems


#6

def get_member_list(crew_members: list[tuple],
                    ship_systems: dict,
                    ) -> list:
    """B6: список словарей по сотрудникам."""
    counts = get_member_count_of_systems(crew_members, ship_systems)
    bonuses = get_member_bonuses(crew_members)
    return [
        {"фамилия": name, "должность": job, "стаж": exp, "зарплата": salary,
         "число_систем": counts[name], "премия": bonuses[name]}
        for name, job, exp, salary in crew_members
    ]
