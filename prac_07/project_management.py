from project import Project
from datetime import datetime

FILENAME = "projects.txt"


def main():
    """Main function to run the project management system."""
    projects = load_projects(FILENAME)
    print("Project Management")
    menu = """\nMenu:
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""
    choice = input(menu + "\n>>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            try:
                filter_date = datetime.strptime(filter_date_str, "%d/%m/%Y").date()
                display_projects(filter_projects_by_date(projects, filter_date))
            except ValueError:
                print("Invalid date format.")
        elif choice == "a":
            new_project = create_project_from_user_input()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(menu + "\n>>> ").lower()

    if input("Save projects to default file? (y/n): ").lower() == 'y':
        save_projects(FILENAME, projects)
    print("Goodbye.")


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                name, start_date_str, priority, cost_estimate, percent_complete = data
                project = Project(
                    name,
                    datetime.strptime(start_date_str, "%d/%m/%Y").date(),
                    int(priority),
                    float(cost_estimate),
                    int(percent_complete)
                )
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_tab_delimited() + '\n')


def display_projects(projects):
    """Display incomplete and complete projects separately, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda p: p.priority)
    complete = sorted([p for p in projects if p.is_complete()], key=lambda p: p.priority)

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")

    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects, filter_date):
    """Return projects starting after a specific date, sorted by date."""
    return sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)


def create_project_from_user_input():
    """Prompt user for project fields and return a new Project."""
    name = input("Name: ")
    start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    """Allow the user to select a project and update its priority or completion percentage."""
    for i, project in enumerate(projects):
        print(f"{i} - {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_percentage = input("New Percentage (leave blank to keep current): ")
        new_priority = input("New Priority (leave blank to keep current): ")
        if new_percentage:
            project.completion_percentage = int(new_percentage)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection or input.")


if __name__ == '__main__':
    main()
