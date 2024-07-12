def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add item
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")

        elif choice == '2':
            # Remove item
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # View list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(item)
            else:
                print("Shopping List is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()