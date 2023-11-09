"""EX07 - Dictionary Tests."""
__author__ = "730578454"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_names_towns() -> None:
    """Tests names with hometowns."""
    invert_dict1: dict[str, str] = {"Hari": "Charlotte", "Bella": "Durham", "Julia": "Raleigh", "Madi": "Hillsborough"}
    result = invert(invert_dict1)
    assert result == {"Charlotte": "Hari", "Durham": "Bella", "Raleigh": "Julia", "Hillsborough": "Madi"}


def test_invert_name_color() -> None:
    """Tests names with favorite color."""
    invert_dict2: dict[str, str] = {"Christina": "Red", "Aarya": "Green", "Nick": "Blue"}
    result = invert(invert_dict2)
    assert result == {"Red": "Christina", "Green": "Aarya", "Blue": "Nick"}


def test_invert_edge() -> None:
    """Edge Case invert items in a dictionary."""  
    invert_dict3: dict[str, str] = {}
    result = invert(invert_dict3)
    assert result == {}


def test_color1() -> None:
    """Tests name and color."""
    favorite_color1: dict[str, int] = {"Beth": "Blue", "Colby": "Green", "Kevin": "Green"}
    result = favorite_color(favorite_color1)
    assert result == {"Blue"}


def test_color2() -> None:
    """Tests name and color."""
    favorite_color2: dict[str, int] = {"Gamma": "Purple", "Anna": "Red", "Elliot": "Red"}
    result = favorite_color(favorite_color2)
    assert result == {"Red"}

    
def test_color_edge() -> None:
    """Edge Case: tests name and color."""
    favorite_color3: dict[str, int] = {}
    result = favorite_color(favorite_color3)
    assert result == {}


def test_count1() -> None:
    """Tests the number of times a fruit appears."""
    number_count1: list[str] = {"apple", "orange", "pineapple", "orange", "orange"}
    result = count(number_count1)
    assert result == {"apple": 1, "orange": 3, "pineapple": 1}


def test_count2() -> None:
    """Tests the number of times a item of clothing appears."""
    number_count2: list[str] = ["hat", "coat", "coat", "pants", "shirt", "hat"]
    result = count(number_count2)
    assert result == {"hat": 2, "coat": 2, "pants": 1, "shirt": 1}


def test_count_edge() -> None:
    """Edge: Tests the number of times an item appears."""
    number_count3: list[str] = []
    result = count(number_count3)
    assert result == {}


def test_alphabetizer1() -> None:
    """Tests the list of states sorted by letter."""
    list_alpha1: list[str] = ["Alabama", "Arizona", "Idaho", "Utah", "Vermont"]
    result = alphabetizer(list_alpha1)
    assert result == {'a': ['Alabama', 'Arizona'], 'i': ['Idaho'], 'u': ['Utah'], 'v': ['Vermont']}


def test_alphabetizer2() -> None:
    """Tests the list of drinks sorted by letter."""
    list_alpha2: list[str] = ["Coke", "Cheerwine", "Juice", "Milk", "Tea"]
    result = alphabetizer(list_alpha2)
    assert result == {'c': ['Coke', 'Cheerwine'], 'j': ["Juice"], 'm': ["Milk"], 't': ["Tea"]}


def test_alphabetizer_edge() -> None:
    """Edge: Tests the list of items sorted by letter."""
    list_alpha3: list[str] = []
    result = alphabetizer(list_alpha3)
    assert result == {}


def test_update_attend1() -> None:
    """Tests the updates of attendance log."""
    log1: dict[str, list[str]] = {"Monday": ["Madi", "Bella"], "Tuesday": ["Madi", "Christina"], "Wednesday": ["Bella"]}
    result = update_attendance(log1)
    assert result == {"Monday": ["Madi", "Bella"], "Tuesday": ["Madi", "Bella", "Christina"], "Wednesday": ["Bella"]}


def test_update_attend2() -> None:
    """Tests the updates of attendance log."""
    log2: dict[str, list[str]] = {"Monday": ["Colby", "Noah", "Beth"], "Tuesday": ["Colby", "Madi"], "Wednesday": ["Colby", "Madi"]}
    result = update_attendance(log2)
    assert result == {"Monday": ["Colby", "Noah", "Beth", "Madi"], "Tuesday": ["Colby", "Madi"], "Wednesday": ["Colby", "Madi"]}


def test_update_attend_edge() -> None:
    """Edge: Tests the updates of attendance log."""
    log3: dict[str, list[str]] = {}
    result = update_attendance(log3)
    assert result == {}

