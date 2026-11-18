from src.normalization import normalize_items

def test_normalize_items():
    items = [
        " a-101 ",
        "A-102",
        "a-101",
        " A-103 "
    ]

    expected = {"A-101", "A-102", "A-103"}

    result = normalize_items(items)

    assert result == expected

def test_normalize_items_empty():
    items = []
    expected = set()

    result = normalize_items(items)

    assert result == expected