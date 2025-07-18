import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


FILENAME = "languages.csv"


def main():
    """Read language data from file, store as objects, and display them."""
    languages = load_languages(FILENAME)
    display_languages(languages)


def load_languages(filename):
    """Load programming languages from a CSV file into a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            name, typing, reflection_str, year = row
            reflection = reflection_str == "Yes"
            language = ProgrammingLanguage(name, typing, reflection, int(year))
            languages.append(language)
    return languages


def display_languages(languages):
    """Display a list of ProgrammingLanguage objects."""
    for language in languages:
        print(language)


# Optional versions for demonstration purposes (commented out by default)

def using_csv():
    """Language file reader version using the csv module (no custom class)."""
    with open(FILENAME, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader using a named tuple."""
    with open(FILENAME, 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print("Field names:", file_field_names)
        Language = namedtuple('Language', 'name, typing, reflection, year')
        reader = csv.reader(in_file)
        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    with open(FILENAME, 'r') as in_file:
        next(in_file)  # Skip header
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(repr(language))


if __name__ == "__main__":
    main()