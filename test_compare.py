import pytest
from syllabus_comparison import compare_syllabi

@pytest.fixture
def sample_syllabi():
    old_syllabus = {
        "syllabus": {
            "unit1": {"title": "Introduction", "topics": ["Basics of Python", "Data Types"]},
            "unit2": {"title": "Control Flow", "topics": ["If-Else", "Loops"]},
        }
    }

    new_syllabus = {
        "syllabus": {
            "unit1": {"title": "Introduction", "topics": ["Python Basics", "Data Types and Variables"]},
            "unit2": {"title": "Flow Control", "topics": ["Loops", "Conditionals"]},
            "unit3": {"title": "Functions", "topics": ["Defining Functions", "Lambda Functions"]},
        }
    }

    return old_syllabus, new_syllabus

def test_compare_syllabi(sample_syllabi):
    old_syllabus, new_syllabus = sample_syllabi
    result = compare_syllabi(old_syllabus, new_syllabus, similarity_threshold=0.6)

    # Check if added topics are correctly identified
    assert "Defining Functions" in result["added"]
    assert "Lambda Functions" in result["added"]

    # Check if removed topics are correctly identified
    assert "If-Else" in result["removed"]

    # Check if semantic matches include expected topics
    assert any(match["new"] == "Loops" and match["old"] == "Loops" for match in result["semantic_matches"])

    # Check if elaborations are detected
    assert any(elab["new"] == "Python Basics" and elab["old"] == "Basics of Python" for elab in result["elaborations"])

    # Check if shifted topics are identified
    assert any(shift["topic"] == "Conditionals" and shift["from"] == "Control Flow" and shift["to"] == "Flow Control" for shift in result["shifted_topics"])
