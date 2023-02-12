import pytest
from engr_class import SoftwareEngineer
from tech_class import Technology


def test_software_engineer_creation():
    swe = SoftwareEngineer("Private Smith")
    assert swe.name == "Private Smith"
    assert swe.skills == []
    assert swe.technologies == []

def test_add_technology():
    swe = SoftwareEngineer("Private Smith")
    swe.add_technology("Python", 5, "https://example.com/python")
    assert len(swe.technologies) == 1
    assert swe.technologies[0].name == "Python"
    assert swe.technologies[0].years_experience == 5
    assert swe.technologies[0].project_url == "https://example.com/python"

def test_get_technologies():
    swe = SoftwareEngineer("Private Smith")
    assert swe.get_technologies() == 'No technologies added'
    swe.add_technology("Python", 5, "https://example.com/python")
    assert len(swe.get_technologies()) == 1
    assert swe.get_technologies()[0].name == "Python"
    assert swe.get_technologies()[0].years_experience == 5
    assert swe.get_technologies()[0].project_url == "https://example.com/python"

def test_add_skills():
    swe = SoftwareEngineer("Private Smith")
    swe.add_skills("Python")
    assert len(swe.skills) == 1
    assert swe.skills == ["Python"]

def test_get_skills():
    swe = SoftwareEngineer("Private Smith")
    assert swe.get_skills() == 'No skills added'
    swe.add_skills("Python")
    assert len(swe.get_skills()) == 1
    assert swe.get_skills() == ["Python"]
