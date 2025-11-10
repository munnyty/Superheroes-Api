from typing import Any


def hero_finding(gender: str,
                 employment: bool,
                 superheroes_json: list) -> dict[str, Any] | str:
    """
    По выбранному полу и наличию работы функция выдает самого высокого супергероя из списка(если имеется несколько героев с максимальным ростом, то выдает первого).

    Аргументы:
        gender (str): Гендер нашего героя
        employment (bool): Наличие у нашего героя работы

    Возвращает:
        dict | str: возвращает нам словарь с данными о герое в формате json, либо выдает ошибку ValueError
    """

    if gender not in ["Male","Female"] or employment not in [False, True]:
        raise ValueError('Неверный набор аргументов: гендер должен быть Male or Female, устройство на работе должно быть булевым значением(True, False)')

    (tallest_hero := superheroes_json[0])['appearance']['height'] = ["0'0", '0 cm']

    for hero in superheroes_json:
        if employment:
            superhero_employment = hero.get('work').get('occupation') != '-'
        else:
            superhero_employment = hero.get('work').get('occupation') == '-'

        if hero.get('appearance').get('gender') == gender and superhero_employment:
            my_hero_height = float(hero.get('appearance').get('height')[1].split(' ')[0])
            tallest_hero_height = float(tallest_hero.get('appearance').get('height')[1].split(' ')[0])
            if tallest_hero_height < my_hero_height:
                tallest_hero = hero

    return tallest_hero

