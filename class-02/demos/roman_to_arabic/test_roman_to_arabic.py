import pytest

from roman_to_arabic import roman_to_arabic


def test_m():
  assert roman_to_arabic('m') == 1000

def test_c():
  assert roman_to_arabic('c') == 100

def test_x():
  assert roman_to_arabic('x') == 10

def test_i():
  assert roman_to_arabic('i') == 1

def test_blank():
  assert roman_to_arabic('') == 0

def test_cm():
  assert roman_to_arabic('cm') == 900

def test_xc():
  assert roman_to_arabic('xc') == 90

def test_ix():
  assert roman_to_arabic('ix') == 9

def test_mm():
  assert roman_to_arabic('mm') == 2000

def test_mmm():
  assert roman_to_arabic('mmm') == 3000

def test_v():
  assert roman_to_arabic('v') == 5

def test_vi():
  assert roman_to_arabic('vi') == 6

def test_iv():
  assert roman_to_arabic('iv') == 4

def test_3999():
  assert roman_to_arabic('mmmcmxcix') == 3999

def test_1984():
  assert roman_to_arabic('mcmlxxxiv') == 1984
