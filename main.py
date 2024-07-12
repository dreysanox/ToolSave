import json
import os
import re
import subprocess

CATEGORIES_FILE = "categories.json"


def main():
    print_toolsave_logo()
    menu()


def clear_screen():
    subprocess.run('clear', shell=True, check=True)
    print_toolsave_logo()


def print_toolsave_logo():
    logo = """
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░        
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░   
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░ 
    """
    print(logo)


# --------------------------------------MENU--------------------------------------


def menu():
    clear_screen()
    while True:
        print("\nWelcome to TOOLSAVE")
        print("1. Exit")
        print("2. Add Category")
        print("3. List Categories")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            break
        elif choice == '2':
            name = input("\nEnter the name of the category: ")
            add_category(name)
        elif choice == '3':
            list_categories()
        else:
            print("\nInvalid choice. Please try again.")


# CATEGORIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# --------------------------------------AÑADIR CATEGORIAS--------------------------------------

def add_category(name):  # Función que añade una categoría
    clear_screen()
    category = load_categories()
    next_index = len(category)
    category[next_index] = name
    save_categories(category)
    print(f"Command '{name}' added successfully.")


def load_categories():  # Devuelve las categorias guardades en el fichero si hay, si no devuelve {}
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_categories(category):  # Actualiza el fichero de categorias con una categoria nueva
    with open(CATEGORIES_FILE, 'w') as file:
        json.dump(category, file, indent=4)


# --------------------------------------LISTAR CATEGORIAS--------------------------------------

def list_categories():  # Lista todas las categorias y te da a elegir una
    clear_screen()
    categories = load_categories()
    if categories:
        for i, name in enumerate(categories):
            print(f"{i}. {categories[name]}")
        try:
            selected_index = input("Select a category or press enter to exit: ")
            if selected_index == '':
                return
            selected_category = categories[selected_index]
            show_category(selected_category)
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
    else:
        print("No categories saved.")


def show_category(category):  # Muestra el menu de una categoria
    # Creamos el category file si no exsiste
    category_file = category + ".json"
    if not os.path.exists(CATEGORIES_FILE):
        # Crea un archivo JSON con un diccionario vacío
        with open(CATEGORIES_FILE, 'w') as file:
            json.dump({}, file, indent=4)

    # Pasamos al menú
    choice = '0'
    print(f"\nThis is your {category}ToolSave")
    while choice != '1':
        clear_screen()
        print("1. Exit this category")
        print("2. Add Command")
        print("3. List Commands")

        choice = input("Enter your choice: ")

        if choice == '1':
            continue
        elif choice == '2':
            name = input("Enter the name of the command: ")
            command = input("Enter the command: ")
            add_command(name, command, category_file)
        elif choice == '3':
            list_commands(category_file)
        else:
            print("Invalid choice. Please try again.")
    clear_screen()


# COMMANDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def load_commands(catgoryfile):
    if os.path.exists(catgoryfile):
        with open(catgoryfile, 'r') as file:
            return json.load(file)
    return {}


def save_commands(commands, catgoryfile):
    with open(catgoryfile, 'w') as file:
        json.dump(commands, file, indent=4)


# --------------------------------------LISTAR COMANDOS DE UNA CATEGORIA--------------------------------------


def list_commands(category_file):
    clear_screen()
    commands = load_commands(category_file)
    if commands:

        for i, command_info in commands.items():
            name = command_info.get("name")
            command = command_info.get("command")
            print(f"{i}. {name} [{command}]")

        try:
            selected_name = input("Select a command or press enter to exit: ")
            if selected_name == '':
                return
            execute_command(category_file, selected_name)
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
    else:
        print("No commands saved.")


# --------------------------------------AÑADIR COMANDO A UNA CATEGORÍA--------------------------------------


def add_command(name, command, category_file):
    clear_screen()
    commands = load_commands(category_file)
    next_index = len(commands)
    if next_index not in commands:
        commands[next_index] = {}
    commands[next_index]['name'] = name
    commands[next_index]['command'] = command
    save_commands(commands, category_file)
    print(f"Command '{name}' added successfully to the category.")


def prompt_for_variables(command):
    variables = re.findall(r'\{(.*?)\}', command)
    values = {}
    for var in variables:
        values[var] = input(f"Enter value for {var}: ")
    return values


def replace_variables(command, values):
    for var, val in values.items():
        command = command.replace(f'{{{var}}}', val)
    return command


def execute_command(category_file, name):
    clear_screen()
    print("This is your output:\n")
    commands = load_commands(category_file)
    command_value = commands[name]['command']
    values = prompt_for_variables(command_value)
    command_with_values = replace_variables(command_value, values)
    try:
        subprocess.run(command_with_values, shell=True, check=True)
        print("\n")
        input("")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{name}': {e}")


if __name__ == "__main__":
    main()
