def main():
    # Prompt user for input
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()