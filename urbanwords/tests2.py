from django.test import TestCase
import json
# Create your tests here.
import pytest
from django.urls import reverse
from .models import Word
from django.conf import settings
from .services.urban_dictionary import UrbanDictionaryAPI


@pytest.mark.django_db
def test_get_from_db(client):
    word = "bruf"
    response = client.post(reverse("save_word_definition", args=[word]))
    db_word = UrbanDictionaryAPI().get_word_from_db(word)
    word_is_in_db = UrbanDictionaryAPI().word_exists_in_db(word)

    assert response.status_code == 200
    assert response.json() == db_word
    assert word_is_in_db == True


@pytest.mark.django_db
def test_get_definition(client):
    word = "bruf"
    response = UrbanDictionaryAPI().get_definition(word)

    assert response['definition'] == 'Slang for [brother], bro, [brethren], bruh, [bru], etc.'


@pytest.mark.django_db
def test_get_definition_fail(client):
    word = " "
    response = UrbanDictionaryAPI().get_definition(word)

    assert response == None
