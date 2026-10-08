from data import library_archive, crew_members, ship_systems

#Part A

GENRE_FILTER = "Научная фантастика"

sci_fi_books = []
for title,name,year,pages,genre in library_archive:
    if genre == GENRE_FILTER:
        sci_fi_books.append((title,name,year,pages,genre))

book_titles = []
for title, *_ in library_archive:
    book_titles.append(title)
short_books_before_1950 = []
for title,_,year,pages,_ in library_archive:
    if year <= 1950 and pages < 300:
        short_books_before_1950.append(title)
books_by_author = {author: tuple(title for title,a,*_ in library_archive if a == author)
                   for _, author, *_ in library_archive}

avg_page_count = sum((pages for _,_,_,pages,_ in library_archive)) / len(library_archive)

#Part B
#1
avg_exp_by_job = {targ_job:
                 sum(exp for _,job,exp, _ in crew_members if job == targ_job) /
                 len([_ for _,job,*_ in crew_members if job == targ_job])
             for _,targ_job,*_ in crew_members}
print(avg_exp_by_job)

#2
high_salary_members = [f'{name}:{salary}' for name,_,exp,salary in crew_members
                  if salary > 5000 and exp < 10]

#3
member_names = [name for name, *_ in crew_members]
member_count_of_systems = {member: len([syst_name for syst_name in ship_systems
                                        if member in ship_systems[syst_name]])
                           for member in member_names
                           }

#4
member_bonuses = {name:(salary * 0.1 if age <=  5 else salary * 0.15)
                  for name,_,age,salary in crew_members
                  }

#5
little_systems = [system for system in ship_systems if len(ship_systems[system]) < 2]

#6
member_list = [
    {name : (job, age, salary,member_count_of_systems[name],member_bonuses[name])}
    for name,job,age,salary in crew_members
]

print(member_list)




