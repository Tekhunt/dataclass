import pytest

from tech_class import Technology

def test_technology_creation():
    t = Technology("Python", 5, "https://example.com/python")
    assert t.name == "Python"
    assert t.years_experience == 5
    assert t.project_url == "https://example.com/python"

def test_technology_defaults():
    t = Technology("Python")
    assert t.name == "Python"
    assert t.years_experience == 0
    assert t.project_url is None

def test_technology_repr():
    t = Technology("Python", 5, "https://example.com/python")
    assert repr(t) == "Technology(name='Python', years_experience=5, project_url='https://example.com/python')"
