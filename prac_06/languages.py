from programming_language import ProgrammingLanguage


def main():
    """Create and test ProgrammingLanguage objects."""

    # Create language objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test __str__ method
    print(python)

    # Create a list of languages
    languages = [python, ruby, visual_basic]

    # Display dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
