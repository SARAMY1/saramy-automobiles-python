"""Saramy Automobiles: educational command-line car purchase simulator.

Demonstrates classes, dictionaries, loops, conditionals and input validation.
No inventory is checked and no payments are processed.
"""

# SECTION 1: Model a customer's car selection using a Python class.
class Car:
    """Store the customer's chosen vehicle specifications and listed price."""

    def __init__(self, color, brand, year, price):
        # Instance attributes belong to each individual Car object.
        self.color = color
        self.brand = brand
        self.year = year
        self.price = price

    def display_details(self):
        """Print a readable summary of the selected vehicle."""
        print("\n----- YOUR CAR SELECTION -----")
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Model Year: {self.year}")
        # :, adds thousands separators for easier reading.
        print(f"Price: ${self.price:,}")


# SECTION 2: Map available brands to illustrative prices in US dollars.
# A dictionary avoids repeating a long if/elif chain for each brand.
# These prices are examples, NOT real-world vehicle quotations.
car_prices = {
    "TESLA": 10000,
    "FERRARI": 5000,
    "LEXUS": 4000,
    "TOYOTA": 3000,
    "HONDA": 4000,
}


def main():
    """Run the interactive customer purchase-request workflow."""

    # SECTION 3: Welcome the customer and display the available brands.
    print("=" * 45)
    print("WELCOME TO SARAMY AUTOMOBILES")
    print("=" * 45)

    # strip() removes surrounding spaces; upper() standardizes the name.
    name = input("Enter your name: ").strip().upper()
    print(f"\nWe are glad to have you here, dear {name}!")
    print("\nBelow are the car brands we have available:")

    # items() provides each dictionary key (brand) and value (price).
    for brand, price in car_prices.items():
        print(f"{brand}: ${price:,}")

    # SECTION 4: Keep asking until the customer answers Yes or No.
    while True:
        query = input(
            "\nAre you interested in buying a car? Yes/No: "
        ).strip().lower()

        if query == "yes":
            print("\nGreat! Let's find your preferred car.")
            break
        elif query == "no":
            print("\nThank you for visiting Saramy Automobiles!")
            return  # Exit main() without starting the purchase process.
        else:
            print("Invalid response. Please enter Yes or No.")

    # SECTION 5: Check the selected brand against the dictionary keys.
    while True:
        selected_brand = input(
            "\nEnter the car brand you would like to purchase: "
        ).strip().upper()

        if selected_brand in car_prices:
            # Dictionary lookup retrieves the matching illustrative price.
            selected_price = car_prices[selected_brand]
            print(f"\nYou selected {selected_brand}.")
            print(f"The listed price is ${selected_price:,}.")
            break

        print("Sorry, that brand is not available.")
        print("Please select one of the listed brands.")

    # SECTION 6: Collect preferred specifications, not verified inventory.
    color = input("\nWhat color would you prefer? ").strip().title()

    while True:
        year = input("Enter your preferred model year: ").strip()

        # isdigit() checks numeric characters; length checks four digits.
        # This is a basic format check, not a vehicle-availability check.
        if len(year) == 4 and year.isascii() and year.isdigit():
            break
        print("Please enter a valid four-digit model year.")

    # SECTION 7: Construct a Car instance from the customer's inputs.
    decision = Car(color, selected_brand, year, selected_price)
    decision.display_details()

    # SECTION 8: Demonstrate payment-method selection without charging.
    while True:
        payment = input(
            "\nChoose a payment method (Card/Transfer/Cash): "
        ).strip().lower()

        if payment == "card":
            print("\nYou selected card payment.")
            print("Please proceed to the cashier's POS terminal.")
            break
        elif payment == "transfer":
            print("\nYou selected bank transfer.")
            print("Please request payment details from the cashier.")
            break
        elif payment == "cash":
            print("\nYou selected cash payment.")
            print("Please proceed to the cashier.")
            break
        else:
            print("Invalid payment method. Please try again.")

    # SECTION 9: Close the simulation without claiming a completed sale.
    print("\n" + "=" * 45)
    print(f"Thank you for choosing Saramy Automobiles, {name}!")
    print("Your purchase request has been recorded in this session.")
    print("Payment has not been processed.")
    print("=" * 45)


# Run the interactive program only when this file is executed directly.
# Importing the module elsewhere will not immediately prompt for input.
if __name__ == "__main__":
    main()
