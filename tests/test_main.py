from main import print_a, print_b
import os
import pytest


@pytest.mark.a
def test_print_a():
    assert print_a() == "a"


@pytest.mark.a
def test_env_var_for_a():
    assert os.environ["MY_ENV_VAR"] == "a"


@pytest.mark.b
def test_print_b():
    assert print_b() == "b"


@pytest.mark.b
def test_env_var_for_b():
    assert os.environ["MY_ENV_VAR"] == "b"
