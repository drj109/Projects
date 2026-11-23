import pytest
from app import app


@pytest.mark.parametrize(("skills", "expected"), [
    ("scan packages in a warehouse", "Parcel handler"),
    ("espresso drinks and milk", "Barista"),
    ("set up microphones for recording", "Audio assistant"),
])
def test_top_result(skills, expected):
    response = app.test_client().post("/api/matches", json={"skills": skills})
    first = response.get_json()["matches"][0]
    assert first["role"] == expected
    assert first["terms"] and 0 < first["score"] <= 1


def test_unknown_vocabulary():
    response = app.test_client().post("/api/matches", json={"skills": "xylophone"})
    assert response.get_json() == {"matches": []}


@pytest.mark.parametrize("payload", [{}, [], {"skills": "   "}, {"skills": 123}])
def test_bad_input(payload):
    assert app.test_client().post("/api/matches", json=payload).status_code == 400
