"""Testing the zip function."""
__author__ = "730578454"

from lessons.zip import zip


def test_use_case_ages() -> None:
    """Tests ages with names."""
    list1: list[str] = ["hari", "aarya", "christina"]
    list2: list[int] = [19, 18, 20]
    result = zip(list1, list2)  
    assert result == {"hari": 19, "aarya": 18, "christina": 20}
    

def test_use_case_comp_course() -> None:
    """Tests classes with class codes."""
    list1: list[str] = ["python", "java"]
    list2: list[int] = [110, 210]
    result = zip(list1, list2) 
    assert result == {"python": 110, "java": 210}
    

def test_edge_case_lengths() -> None:
    """Tests lists of different lengths."""
    list1: list[str] = ["python", "java"]
    list2: list[int] = [110]
    result = zip(list1, list2) 
    assert result == {}