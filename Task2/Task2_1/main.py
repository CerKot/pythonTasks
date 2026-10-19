import solution_comprehensions as s_c

import solution_loops as s_l
from data import library_archive,crew_members,ship_systems

from typing import Any


PRECISION = 2


def fmt(value: Any) -> str:
    """Форматирование значения: числа с фиксированной точностью, кортежи через запятую."""
    if isinstance(value, float):
        return f"{value:.{PRECISION}f}"
    if isinstance(value, tuple):
        return ", ".join(fmt(v) for v in value)
    return str(value)


def print_list(title: str, items: list[Any]) -> None:
    """Список: по одному элементу в строке."""
    print(title)
    for item in items:
        print(f"  {fmt(item)}")
    print()


def print_dict(title: str, mapping: dict[str, Any]) -> None:
    """Словарь построчно; если значение — список, его элементы идут по одному в строке."""
    print(title)
    for key, value in mapping.items():
        if isinstance(value, list):
            print(f"  {key}:")
            for item in value:
                print(f"    {fmt(item)}")
        else:
            print(f"  {key}: {fmt(value)}")
    print()


def print_records(title: str, records: list[dict[str, Any]]) -> None:
    """Список словарей: одна запись — одна строка."""
    print(title)
    for record in records:
        print("  " + ", ".join(f"{k}={fmt(v)}" for k, v in record.items()))
    print()


def main() -> None:
    lib, crew, systems = library_archive, crew_members, ship_systems

    print_list("A1. Научная фантастика:", s_l.get_sci_fi_books(lib))
    print_list("A2. Названия литературы:", s_l.get_book_titles(lib))
    print_list("A3. До 1950 года и короче 300 страниц:", s_l.get_short_book_titles(lib))
    print_dict("A4. Автор -> произведения:", s_l.get_books_by_author(lib))
    avg = s_l.get_avg_page_count_from_library(lib)
    print(f"A5. Среднее число страниц: {fmt(avg)}\n")

    print_dict("B1. Должность -> средний стаж:", s_l.get_avg_exp_by_job(crew))
    print_list("B2. Зарплата > 5000 и стаж < 10:", s_l.get_high_salary_members(crew))
    print_dict("B3. Фамилия -> число систем:", s_l.get_member_count_of_systems(crew, systems))
    print_dict("B4. Фамилия -> премия:", s_l.get_member_bonuses(crew))
    print_list("B5. Системы с менее чем двумя ответственными:",
               s_l.get_little_systems(systems))
    print_records("B6. Сводка по сотрудникам:", s_l.get_member_list(crew, systems))


if __name__ == "__main__":
    main()