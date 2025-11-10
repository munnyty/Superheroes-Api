from typing import Any

import pytest
import requests


@pytest.fixture()
def superheroes_json() -> list[dict[str, Any]]:

    all_heroes_json = requests.get("https://akabab.github.io/superhero-api/api/all.json").json()
    return all_heroes_json



