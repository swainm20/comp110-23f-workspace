"""Combining two lists into a dictionary."""
__author__ = "730578454"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Dictionary where keys in list and values are index."""
    new_dict: dict[str, int] = {}

    if len(list1) != len(list2):
        new_dict = {}
        return new_dict
    
    for idx in range(len(list1)):
        new_dict[list1[idx]] = list2[idx]

    return new_dict