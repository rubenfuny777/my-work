# Import the math module for mathematical operations
import math

# Define the main function
def main():
    # Print the menu to the console
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    
    # Get the user's choice and convert it to lowercase
    choice = input("Enter your choice: ").lower()

    # Check if the user's choice is 'investment'
    if choice == 'investment':
        # Get the necessary details for the investment calculation
        P = float(input("Enter the amount of money that you are depositing: "))
        r = float(input("Enter the interest rate (as a percentage): ")) / 100
        t = float(input("Enter the number of years you plan on investing: "))
        interest = input("Do you want 'simple' or 'compound' interest: ").lower()

        # Check the type of interest and perform the appropriate calculation
        if interest == 'simple':
            A = P * (1 + r * t)
        elif interest == 'compound':
            A = P * math.pow((1 + r), t)
        else:
            print("Invalid interest type. Please enter either 'simple' or 'compound'.")
            return

        # Print the total amount after interest
        print(f"The total amount after {t} years is: {A}")

    # Check if the user's choice is 'bond'
    elif choice == 'bond':
        # Get the necessary details for the bond repayment calculation
        P = float(input("Enter the present value of the house: "))
        r = float(input("Enter the annual interest rate (as a percentage): ")) / 100 / 12
        n = float(input("Enter the number of months you plan to repay the bond: "))

        # Calculate the monthly repayment amount
        repayment = (r * P) / (1 - (1 + r) ** -n)
        
        # Print the monthly repayment amount
        print(f"You will have to repay: {repayment} every month.")

    else:
        # Print an error message if the user's choice is neither 'investment' nor 'bond'
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

# Call the main function
if __name__ == "__main__":
    main()

