from django.test import TestCase
import json
# Create your tests here.
import pytest
from django.urls import reverse
from .models import Word
from django.conf import settings

test_word = {
    "definition": "Slang for [brother], bro, [brethren], bruh, [bru], etc.",
    "permalink": "http://bruf.urbanup.com/13109503",
    "thumbs_up": 25,
    "author": "Matthew69Bruf",
    "word": "bruf",
    "defid": 13109503,
    "current_vote": "",
    "written_on": "2018-08-02T19:30:09.735Z",
    "example": "Thanks bruf.\n\nDamn bruf, [you better] watch out, those [hoes] are a bunch of [snakes], bruf."
}

@pytest.mark.django_db
def test_get_definition(client):
    url = reverse("get_word_definition", args=["bruf"])
    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["definition"] == test_word["definition"]
    assert response.json()["author"] == test_word["author"]
    assert response.json()["word"] == test_word["word"]
    assert response.json()["written_on"] == test_word["written_on"]
    assert response.json()["example"] == test_word["example"]

@pytest.mark.django_db
def test_get_definition_fail(client):
    url = reverse("get_word_definition", args=[" "])
    response = client.get(url)

    assert response.status_code != 200

@pytest.mark.django_db
def test_save_definition_fail(client):
    url = reverse("save_word_definition", args=[" "])
    response = client.get(url)
    breakpoint()
    assert response.status_code != 200

@pytest.mark.django_db
def test_save_definition(client):
    url = reverse("save_word_definition", args=["bruf"])
    response = client.post(url)

    assert response.status_code == 200
    assert response.json()["definition"] == test_word["definition"]
    assert response.json()["author"] == test_word["author"]
    assert response.json()["word"] == test_word["word"]
    assert response.json()["written_on"] == test_word["written_on"]
    assert response.json()["example"] == test_word["example"]



@pytest.mark.django_db
def test_saved_definition(client):
    url = reverse("save_word_definition", args=["bruf"])
    response = client.post(url)
    word_from_db = Word.objects.get(word="bruf")

    assert response.status_code == 200
    assert word_from_db.definition == test_word["definition"]
    assert word_from_db.author == test_word["author"]
    assert word_from_db.word == test_word["word"]
    assert word_from_db.written_on == test_word["written_on"]
    assert word_from_db.example == test_word["example"]
