from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"

#Call the main function that is part of the pytest so that the computer will execute the functions in this file.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])