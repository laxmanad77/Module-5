def main():
    total_rainfall = 0.0
    total_months = 0

    # Ask the user for the number of years
    years = int(input("Enter the number of years: "))

    # Validate input
    while years < 1:
        print("Number of years must be 1 or more.")
        years = int(input("Enter the number of years: "))

    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Inner loop for each month
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Try again.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            total_rainfall += rainfall
            total_months += 1

    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\nRainfall Statistics")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

# Call the main function
main()
