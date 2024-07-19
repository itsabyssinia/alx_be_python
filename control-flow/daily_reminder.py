task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        elif time_bound =="no":
            print(f"{task} is a high priority task that doesn't require immediate attention.")
        else:
            print("Invalid input")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires immediate attention.")
        elif time_bound =="no":
            print(f"{task} is a medium priority task that doesn't require immediate attention")
        else:
            print("Invalid input")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that requires immediate attention")
        elif time_bound =="no":
            print(f"{task} is a low priority task that doesn't require immediate atttention")
        else:
            print("Invalid input")
    case _: 
        print("Invalid input")


