"""EX06 - Dictionary."""
__author__ = "730578454"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    new_dict: dict[str, str] = {}

    for key, value in original.items():
        if value in new_dict:
            raise KeyError("This dictionary has a repeated value!")
        else:
            new_dict[value] = key

    return new_dict


def favorite_color(favorite_color: dict[str, str]) -> str:
    """Finds the most popular color."""
    highest_amount: int = 0
    color_amount: dict[str, int] = {}

    for key, value in favorite_color.items():
        if value not in color_amount:
            color_amount[value] = 1
        else:
            color_amount[value] += 1

    for key, value in color_amount.items():
        if value > highest_amount:
            most_popular = key
            highest_amount = value
        
    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    values_dict: dict[str, int] = {}

    for elem in values:
        if elem not in values_dict:
            values_dict[elem] = 1
        else:
            values_dict[elem] += 1
    
    return values_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizes the list of words and gives the list of words with that letter."""
    words_dict: dict[str, list[str]] = {}
    word: str = ""
    for word in words:
        word = word.lower()
        if word[0] not in words_dict:
            words_dict[word[0]] = []
    
        words_dict[word[0]].append(word)

    return words_dict


def update_attendance(attendance_log: dict[str, list[str]], week_day: str, name: str) -> dict[str, list[str]]:
    """Updates the attendance log with a new day of the week and new names."""
    if week_day not in attendance_log:
        attendance_log[week_day] = []

    attendance_log[week_day] += [name]

    return attendance_log