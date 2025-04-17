import pytest
import yaml
import os

def test_definitions():
    with open("definitions.yaml", "r") as f:
        definitions = yaml.safe_load(f)
    assert isinstance(definitions, dict)

def test_generated_files():
    os.makedirs("generated_templates", exist_ok=True)
    assert os.path.exists("generated_templates/Definitions.h")
    assert os.path.exists("generated_templates/Definitions.hs")
    assert os.path.exists("generated_templates/Definitions.java")

def test_cpp_template_content():
    with open("generated_templates/Definitions.h", "r") as f:
        content = f.read()
    assert "#ifndef TYPES_H" in content
    assert "#define TYPES_H" in content
    assert "#endif" in content

def test_python_template_content():
    with open("generated_templates/definitions.py", "r") as f:
        content = f.read()
    assert "class Customer:" in content
    assert "def __init__(self, name: str, age: int, email: str):" in content
    assert "def calculate_total(customer: Customer, orders: list[Order]) -> str:" in content
    assert "# Calculates the total amount spent by a customer based on their orders." in content