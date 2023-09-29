from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services.urban_dictionary import UrbanDictionaryAPI
from django.views.decorators.http import require_GET, require_POST
from .models import Word
from django.views.decorators.csrf import csrf_exempt

# from .forms import WordSearchForm

# Create your views here.

def word_to_json(word_obj):
    """Convert Word object to JSON-serializable dict."""
    print(word_obj)
    return {
        "definition": word_obj.definition,
        "author": word_obj.author,
        "word": word_obj.word,
        "written_on": word_obj.written_on,
        "example": word_obj.example
    }
@require_GET
def get_word_definition(request, word):
    try:
        word_obj = UrbanDictionaryAPI.get_definition(word)
        if word_obj:
            return JsonResponse(word_obj)
        else:
            return JsonResponse({'error': 'Word not found.'}, status=404)
    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'Internal server error.'}, status=500)

@csrf_exempt
@require_POST
def save_word_definition(request, word):
    try:
        word_exists = UrbanDictionaryAPI.word_exists_in_db(word)

        if word_exists:
            word_obj = Word.objects.get(word=word)
            print("ALREADY SAVED IN DB")
            return JsonResponse(word_to_json(word_obj))
        else:
            word_obj = UrbanDictionaryAPI.get_definition(word)

            if word_obj:
                saved_word = Word.objects.create(
                    definition=word_obj['definition'],
                    author=word_obj['author'],
                    word=word_obj['word'],
                    written_on=word_obj['written_on'],
                    example=word_obj['example']
                )
                print("word saved in DB")

                return JsonResponse(word_to_json(saved_word))
            else:
                return JsonResponse({'error': 'Word not found.'}, status=404)
    except Exception as e:
        print(str(e))
        print("failed!!")
        return JsonResponse({'error': 'Internal server error.'}, status=500)
