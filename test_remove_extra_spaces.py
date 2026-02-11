# test_remove_extra_spaces.py
from remove_extra_spaces import clean_spaces

def test_basic_cleaning():
    assert clean_spaces("hello    world") == "hello world"

def test_leading_trailing_spaces():
    assert clean_spaces("   hello world   ") == "hello world"

def test_multiple_spaces_between_words():
    assert clean_spaces("heavy   multi   space") == "heavy multi space"

def test_empty_string():
    assert clean_spaces("") == ""

def test_only_spaces():
    assert clean_spaces("     ") == ""
