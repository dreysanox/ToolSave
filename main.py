import json
import os

CATEGORIES_FILE = "categories.json"

def main():
    print_toolsave_logo()
    menu()

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



#MENU
def menu():
    while True:
        print("\nWelcome to TOOLSAVE")
        print("1. Exit")
        print("2. Add Category")
        print("3. List Categories")

        choice = input("Enter your choice: ")

        if choice == '1':
            break
        elif choice == '2':
            name = input("Enter the name of the category: ")
            add_category(name)
        elif choice == '3':
            list_categories()
        else:
            print("Invalid choice. Please try again.")


#CATEGORIES


##############################             AÑADIR CATEGORIAS              ##################################################################

#Función que añade una categoría
def add_category(name):
    category = load_categories()
    category[name] = name
    save_categories(category)
    print(f"Command '{name}' added successfully.")

#Devuelve las categorias guardades en el fichero si hay, si no devuelve {}
def load_categories():
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, 'r') as file:
            return json.load(file)
    return {}

#Actualiza el fichero de categorias con una categoria nueva
def save_categories(category):
    with open(CATEGORIES_FILE, 'w') as file:
        json.dump(category, file, indent=4)



##############################             LISTAR CATEGORIAS              ##################################################################


#Lista todas las categorias y te da a elegir una
def list_categories():
    categories = load_categories()
    if categories:
        for i, name in enumerate(categories):
            print(f"{i}. {name}")
        try:
            selected_index = input("Select a category: ")
            selected_category = categories[selected_index]
            show_category(selected_category)
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
    else:
        print("No categories saved.")

#Muestra el menu de una categoria
def show_category(category):

    #Creamos el category file si no exsiste
    CATEGORY_FILE = category + ".json"
    if not os.path.exists(CATEGORIES_FILE):
        # Crea un archivo JSON con un diccionario vacío
        with open(CATEGORIES_FILE, 'w') as file:
            json.dump({}, file, indent=4)

    #Pasamos al menú
    choice = '0'
    while choice != '1':
        print(f"\nWelcome to {category}")
        print("1. Exit this category")
        print("2. Add Command")
        print("3. List Commands")

        choice = input("Enter your choice: ")

        if choice == '1':
            continue
        elif choice == '2':
            name = input("Enter the name of the command: ")
            command = input("Enter the command: ")
            add_command(name, command, CATEGORY_FILE)
        elif choice == '3':
            list_commands(CATEGORY_FILE)
        else:
            print("Invalid choice. Please try again.")











#COMANDOS
def list_commands(CATEGORY_FILE):
    commands = load_commands(CATEGORY_FILE)
    if commands:
        i = 0
        for name, command in commands.items():
            print(f"{i}. {name}: {command}")
            i += 1
    else:
        print("No commands saved.")

def load_commands(CATEGORY_FILE):
    if os.path.exists(CATEGORY_FILE):
        with open(CATEGORY_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_commands(commands, CATEGORY_FILE):
    with open(CATEGORY_FILE, 'w') as file:
        json.dump(commands, file, indent=4)

def add_command(name, command, CATEGORY_FILE):
    commands = load_commands(CATEGORY_FILE)
    commands[name] = command
    save_commands(commands, CATEGORY_FILE)
    print(f"Command '{name}' added successfully.")

#COPYRIGHT

if __name__ == "__main__":
    main()

