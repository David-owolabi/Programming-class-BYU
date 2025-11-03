
# test_weather.py
from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    assert cels_from_fahr(32) == approx(0, abs=0.01)
    assert cels_from_fahr(212) == approx(100, abs=0.01)
    assert cels_from_fahr(-40) == approx(-40, abs=0.01)
    
pytest.main()