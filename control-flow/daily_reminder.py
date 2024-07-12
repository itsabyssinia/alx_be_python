def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Match case based on priority
    match priority.lower():
        case 'high':
            if time_bound.lower() == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Consider completing it soon.")
        
        case 'medium':
            if time_bound.lower() == 'yes':
                print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
            else:
                print(f"Note: '{task}' is a medium priority task. You can complete it as per your schedule.")
        
        case 'low':
            if time_bound.lower() == 'yes':
                print(f"Reminder: '{task}' is a low priority task that should be done today if possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Feel free to complete it at your convenience.")
        
        case _:
            print("Invalid priority level entered.")

if __name__ == "__main__":
    main()

