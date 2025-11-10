import pytest
import requests
from scr import find_hero

BASE_URL = "https://akabab.github.io/superhero-api/api/"

#POSITIVE_CASES
positive_cases = [
    {'gender': 'Male', "occupation": False, 'expected_name': 'Fin Fang Foom', "expected_height": ["32'0", '975 cm']},
    {'gender': 'Male', "occupation": True, 'expected_name': 'Galactus', "expected_height": ["28'9", '876 cm']},
    {'gender': 'Female', "occupation": False, 'expected_name': 'Ardina', "expected_height": ["6'4", '193 cm']},
    {'gender': 'Female', "occupation": True, 'expected_name': 'Wolfsbane', "expected_height": ["12'", '366 cm']}
]

#WRONG_CASES
    #WRONG ARGS TYPE
wrong_args_type = [
    {'gender': 'Male', "occupation": 0.9},
    {'gender': 'Male', "occupation": 'something else'},
    {'gender': 'Male', "occupation": ['something else', 'something else']},
    {'gender': 'Male', "occupation": {'something else', 'something else'}},
    {'gender': 'Male', "occupation": ('something else', 'something else')},
    {'gender': 0.9, "occupation": False},
    {'gender': 123, "occupation": False},
    {'gender': 'something else', "occupation": False},
    {'gender': ['something else', 'something else'], "occupation": False},
    {'gender': {'something else', 'something else'}, "occupation": False},
    {'gender': ('something else', 'something else'), "occupation": False},
    {'gender': ('something else', 'something else'), "occupation": 0.9}
]

#Data integrity testing
@pytest.mark.parametrize("case", positive_cases)
def test_positive_cases_right_full_info(case, superheroes_json):

    hero_info_json = find_hero.hero_finding(case.get("gender"), case.get("occupation"), superheroes_json)
    hero_id = hero_info_json.get("id")
    expected_full_hero_info_json = requests.get(f'{BASE_URL}id/{hero_id}.json').json()
    assert expected_full_hero_info_json == hero_info_json

#Verification against known data
@pytest.mark.parametrize("case", positive_cases)
def test_positive_cases_name(case, superheroes_json):

    full_hero_info = find_hero.hero_finding(case.get("gender"), case.get("occupation"), superheroes_json)
    hero_occupation = full_hero_info.get('work').get('occupation')
    assert full_hero_info.get('name') == case.get('expected_name')
    assert full_hero_info.get('appearance').get('height') == case.get('expected_height')
    assert full_hero_info.get('appearance').get('gender')  == case.get('gender')

    if case.get('occupation'):
        assert hero_occupation != '-'
    else:
        assert hero_occupation == '-'

#Errors checking for wrong type of args
@pytest.mark.parametrize("case", wrong_args_type)
def test_incorrect_argument_type_error(case, superheroes_json):
    with pytest.raises(ValueError):
        find_hero.hero_finding(case.get("gender"), case.get("occupation"), superheroes_json)






