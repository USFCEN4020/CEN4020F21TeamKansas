import csv
import os.path
import pytest
from csv import writer
import main as m
import student as s

# To test password verfication. In Terminal run: pytest test_main.py

class TestClass:

    # Tests if requirements for a valid password are satisfied within main.checkPass()

    # Validates if Less than 8 characters
    def test_checkPass_lessthan8(self):
        assert m.checkPass("1$A") == False  # 3 chars
        assert m.checkPass("1$Abcde") == False  # 7 char
        assert m.checkPass("1$Abcdef") == True  # 8 char

    # Validates if More than 12 characters
    def test_checkPass_morethan12(self):
        assert m.checkPass("1$Abcdefghijk") == False  # 13 characters
        assert m.checkPass("1$Abcdefghij") == True  # 12 characters
        assert m.checkPass("1$Abcdefghi") == True  # 11 characters

    # Validates if it includes an Uppercase letter
    def test_checkPass_noUpper(self):
        assert m.checkPass("1$abcdefg") == False  # Does not include an Uppercase letter
        assert m.checkPass("1$Abcdefg") == True  # Does include an Uppercase letter

    # Validates if it includes a digit char
    def test_checkPass_noDigit(self):
        assert m.checkPass("$Abcdefgh") == False  # Does not include a digit char
        assert m.checkPass("$Abcd5efgh") == True  # Does include a digit char

    # Validates if it includes a non-alphabetic char
    def test_checkPass_noNonAlpha(selfs):
        assert m.checkPass("1Abcdefgh") == False  # Does not include a non-alphabetic char
        assert m.checkPass("1Abc$defgh") == True  # Does include a non-alphabetic char

    # Validates a complete correct password
    def test_checkPass_correctRequirments(self):
        assert m.checkPass(
            "1$Abcdefg") == True  # At least 8 characters, Less than or equal to 12 characters, Includes an Uppercase letter, Includes a digit char, Includes a non-alphabetic char
        assert m.checkPass("test") == False
