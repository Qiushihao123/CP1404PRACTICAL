def extract_name_from_email(email):
    """Extract a formatted name from the email address."""
    name_part = email.split('@')[0]
    name_parts = name_part.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(name_parts).title()


def main():
    """Store email-name pairs in a dictionary and display them."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ")
        else:

            name = default_name
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
