from functions import percentage_function
import pytest


def test_percentage_function_result():
    assert percentage_function(50, 100) == 50


def test_percentage_function_output_type():
    assert type(percentage_function(100, 200)) is int

