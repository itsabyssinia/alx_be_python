def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Draw the pattern
    row = 0
    while row < size:
        # Print one row of asterisks
        for column in range(size):
            print("*", end="")
        # Move to the next line for the next row
        print()
        row += 1

if __name__ == "__main__":
    main()
