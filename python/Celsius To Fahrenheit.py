# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Main function to take input and display the result
def main():
    try:
        # Get the temperature in Celsius from the user
        celsius = float(input("Enter the temperature in Celsius: "))
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Display the result
        print(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
