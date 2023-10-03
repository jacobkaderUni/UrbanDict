# UrbanDict
An application that utilizes the [Urban Dictionary API](https://rapidapi.com/community/api/urban-dictionary) to allow users to view or save definitions of words found in the Urban Dictionary.

## Features
- **View Definition**: `port/definition/{word}` - Displays the definition of a word. If the word is found in the database, the definition is retrieved from there; otherwise, it fetches from the API endpoint.
- **Save Definition**: `port/save/{word}` - Saves the definition of a word to a PostgreSQL database.

## Prerequisites
- **Python Version**: The application uses Python 3.9.17.
- **Dependencies**: All required packages can be found in `requirements.txt`.


## Setting Up
1. **Clone the project**
    ```bash
    git clone https://github.com/jacobkaderUni/UrbanDict.git
    cd UrbanDict
    ```

2. **Set up a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:

```bash
python manage.py runserver
```

## Database migration/config
Ensure you correctly configure the database by checking settings.py. Fill in the correct username, password, port, and DB name. Once done, run the migrations:

```bash
python manage.py makemigration
python manage.py migrate
```

## Testing

Navigate to the folder containing the tests.py file:
```bash
cd urbanwords
```
Then, run the tests:
```bash
coverage run -m pytest tests.py
```

