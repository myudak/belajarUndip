"""
IGNORE

cuma buat test function
"""

import os

from mean_olympique import MO
from positif import IsPositif
from apakah_huruf_a import IsAnA
from apakah_valid import IsValid
from least_square import LS


def test_mean_olympique():
    assert MO(10, 8, 12, 14) == 11
    print("test_mean_olympique bener")


def test_is_positif():
    assert IsPositif(5) == True
    assert IsPositif(0) == True
    assert IsPositif(-1) == False
    print("test_is_positif bener")


def test_is_an_a():
    assert IsAnA("A") == True
    assert IsAnA("B") == False
    assert IsAnA("a") == False
    print("test_is_an_a bener")


def test_is_valid():
    assert IsValid(4) == True
    assert IsValid(5) == False
    assert IsValid(500) == False
    assert IsValid(600) == True
    print("test_is_valid bener")


def test_ls():
    assert LS(1, 3, 5, 6) == 5.0
    print("test_ls bener")


if __name__ == "__main__":
    os.system("cls")
    test_mean_olympique()
    test_is_positif()
    test_is_an_a()
    test_is_valid()
    test_ls()
    print("\nbener semua!")
