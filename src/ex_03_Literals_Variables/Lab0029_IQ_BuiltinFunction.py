# 1. assert — Validating Test Conditions
def test_login():
    expected = "Login Successful"
    actual = "Login Successful"
    assert actual == expected, f"Test Failed: Expected '{expected}', got '{actual}'"

# 2. len() — Checking List Length
users = ["admin", "qa", "dev"]
assert len(users) == 3

# 4. open() — Reading a File for Test Data
with open("testdata.txt", "r") as file:
    lines = file.readlines()
    assert len(lines) > 0, "Test data file is empty"
