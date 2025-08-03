import wikipedia

def main():
    print("Welcome to the Wikipedia searcher!")
    while True:
        title = input("\nEnter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            # Attempt to get the page (with autosuggest off to avoid redirects)
            page = wikipedia.page(title, auto_suggest=False)
            print(f"\n{page.title}")
            print(wikipedia.summary(title, sentences=3))  # Show first 3 sentences
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Show only first 10 options
        except wikipedia.exceptions.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(title))


if __name__ == "__main__":
    main()
