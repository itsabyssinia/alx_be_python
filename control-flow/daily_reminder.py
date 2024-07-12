def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()  # Convert to lower case for case insensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()  # Convert to lower case for case insensitivity
    
    # Process the task based on priority and time sensitivity
    if priority == 'high':
        # Match case for Python 3.10+
        match time_bound:
            case 'yes':
                reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            case 'no':
                reminder = f"Note: '{task}' is a high priority task. Consider completing it when you have free time."
        # For Python versions below 3.10, use if-elif statements
        """
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        elif time_bound == 'no':
            reminder = f"Note: '{task}' is a high priority task. Consider completing it when you have free time."
        """
    elif priority == 'medium':
        reminder = f"'{task}' is a medium priority task. You can complete it as per your schedule."
    elif priority == 'low':
        reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    else:
        reminder = "Invalid priority level entered. Please choose from high, medium, or low."
    
    # Print the customized reminder
    print(reminder)

if __name__ == "__main__":
    main()
