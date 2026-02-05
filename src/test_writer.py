import os

def write_tests(code):
    os.makedirs("tests", exist_ok=True)
    with open("tests/test_generated.py", "w") as f:
        f.write(code)
