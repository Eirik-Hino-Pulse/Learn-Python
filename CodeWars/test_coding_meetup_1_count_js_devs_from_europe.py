import pytest
from coding_meetup_1_count_js_devs_from_europe import count_developers

@pytest.mark.parametrize("lst, expected", [
    ([
        { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
        { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
        { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
        { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
    ], 1),
    ([
        { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
        { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
    ], 0),
    ([
        { 'firstName': 'Mark', 'lastName': 'Z.', 'country': 'Poland', 'continent': 'Europe', 'age': 20, 'language': 'JavaScript' },
    ], 1),
    ([
        { 'firstName': 'Anna', 'lastName': 'K.', 'country': 'Germany', 'continent': 'Europe', 'age': 45, 'language': 'Python' },
    ], 0),
    ([], 0)
])
def test_fixed(lst, expected):
    assert count_developers(lst) == expected

import random
continents = ["Europe", "Asia", "Oceania", "Africa", "Americas"]
languages = ["JavaScript", "Python", "Ruby", "HTML", "CSS"]

def test_random():
    for _ in range(10):
        n = random.randint(5, 20)
        lst = []
        expected = 0
        for _ in range(n):
            cont = random.choice(continents)
            lang = random.choice(languages)
            dev = {"firstName":"X", "lastName":"Y", "country":"Z", "continent":cont, "age":23, "language":lang}
            if cont=="Europe" and lang=="JavaScript":
                expected += 1
            lst.append(dev)
        assert count_developers(lst) == expected
