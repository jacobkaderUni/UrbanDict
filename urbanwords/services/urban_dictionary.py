import requests
from decouple import config
from ..models import Word


class UrbanDictionaryAPI:
    URL = config('URBAN_DICT_API_URL')
    HEADERS = {
        "X-RapidAPI-Key": config('X_RAPIDAPI_KEY'),
        "X-RapidAPI-Host": config('X_RAPIDAPI_HOST')
    }

    @staticmethod
    def word_exists_in_db(term):
        return Word.objects.filter(word=term).exists()

    @staticmethod
    def get_word_from_db(term):
        try:
            term_obj = Word.objects.get(word=term)
            data = {
                "definition": term_obj.definition,
                "author": term_obj.author,
                "word": term_obj.word,
                "written_on": term_obj.written_on,
                "example": term_obj.example
            }
            return data
        except Word.DoesNotExist:
            return None

    @classmethod
    def get_definition(cls, term):
        """
        Fetch definition from BASE_URL
        """
        if cls.word_exists_in_db(term):
            print("Word found in DB!")
            return cls.get_word_from_db(term)
        else:
            try:
                response = requests.get(cls.URL, headers=cls.HEADERS, params={"term": term})
                if response.status_code == 200:
                    print("Word NOT found in DB!")
                    return response.json().get('list', [{}])[0]

            except requests.RequestException:
                print(f"Failed to fetch data for word: {term}")
                return None

    # @classmethod
    # def save_word_in_db(cls, term):
    #     if not (cls.word_exists_in_db(term)):
    #         definition_data = cls.get_definition(term)
    #         if definition_data:
    #             word = Word.objects.create(
    #                 definition=definition_data.get("definition"),
    #                 author=definition_data.get("author"),
    #                 word=definition_data.get("word"),
    #                 written_on=definition_data.get("written_on"),
    #                 example=definition_data.get("example")
    #             )
    #             return word
    #         else:
    #             print(f"No data found for word: {term}")
    #             return None
    #     else:
    #         print(f"The word '{term}' is already saved in the database.")
    #         return cls.get_word_from_db(term)
