#! /bin/python3

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print(f"Kim's favorite language is {favorite_languages.get('kim', 'Any')}.")

