def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))  # Convert input to integer
            if choice == 1:
                item = input("Enter item to add: ")
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")
            elif choice == 2:
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed '{item}' from the shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")
            elif choice == 3:
                print("Shopping List:")
                for item in shopping_list:
                    print(item)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
