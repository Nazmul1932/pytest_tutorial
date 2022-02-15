import pytest
import sys


@pytest.mark.parametrize("username,password", [
    ("admin","admin"),
    ("ami","ami123"),
])
def test_login(username, password):
    print(username)
    print(password)