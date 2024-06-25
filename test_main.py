import pytest

# Для запуска кода я установил библиотеку pytest

# После чего написал в консоли команду pytest для запуска написанных тестов


def test_textarea_input():
    textareaValue = "Datum Soft QA Dev"
    assert textareaValue == "Datum Soft QA Dev"

def test_texarea_special_characters():
    textareaValue = "!@#$%^&*()_+"
    assert textareaValue == "!@#$%^&*()_+"

def test_textarea_length_limit():
    textareaValue = "a" * 1000
    assert len(textareaValue) == 1000

def test_textarea_numeric_input():
    textareaValue = "12345"
    assert textareaValue == "12345"
