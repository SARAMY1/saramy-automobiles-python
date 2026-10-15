# Saramy Automobiles — Python Car Purchase Simulator

A beginner-friendly **command-line automobile purchase simulator** built with Python. Customers can browse a small catalog of car brands, select a preferred brand, color and model year, and choose a simulated payment method.

> **Educational project only:** Listed prices are illustrative, vehicle availability is not verified, and no real payment is processed.

## Features

- Displays five available car brands and example prices
- Validates Yes/No answers and brand selection
- Collects preferred car color and four-digit model year
- Uses a `Car` class to represent a selected vehicle
- Prints a formatted selection summary
- Demonstrates card, transfer and cash payment-method choices without collecting financial data

## Technologies and concepts

- **Language:** Python 3
- **Standard library only:** no third-party packages required
- **Concepts:** variables, `input()`, strings, dictionaries, `for` and `while` loops, `if/elif/else`, classes, constructors, instance methods, and basic input validation

## Getting started

1. Install Python 3.
2. Clone this repository or download its files.
3. From the project folder, run:

```bash
python saramy_automobiles.py
```

On some systems, use `python3` instead of `python`.

## Example interaction

```text
WELCOME TO SARAMY AUTOMOBILES
Enter your name: Samuel
We are glad to have you here, dear SAMUEL!

Below are the car brands we have available:
TESLA: $10,000
FERRARI: $5,000
LEXUS: $4,000
TOYOTA: $3,000
HONDA: $4,000

Are you interested in buying a car? Yes/No: Yes
Enter the car brand you would like to purchase: Toyota
You selected TOYOTA.
The listed price is $3,000.

What color would you prefer? Blue
Enter your preferred model year: 2022

----- YOUR CAR SELECTION -----
Brand: TOYOTA
Color: Blue
Model Year: 2022
Price: $3,000

Choose a payment method (Card/Transfer/Cash): Cash
You selected cash payment.
Please proceed to the cashier.
```

## How the code works

1. A **dictionary** associates each supported car brand with an illustrative price.
2. Input normalization with `strip()`, `upper()` and `lower()` makes text responses easier to compare.
3. **Loops and conditional statements** validate customer interest, brand selection and payment method.
4. A **Car class** stores the chosen brand, color, model year and price, then displays them using an instance method.
5. The program ends with a confirmation that the interaction was only a simulation.

## Limitations and possible improvements

- No persistent database, inventory records or actual checkout
- Model year validation checks format, not whether a car model exists
- Prices are hard-coded examples, not market data
- No automated test suite yet

Possible next steps include a product inventory file, separate customer/order classes, unit tests and a graphical user interface.

## Project background

This project was developed as a practical Python learning exercise to explore interactive programs and introductory object-oriented programming. The code includes explanatory comments to make the control flow and design choices easier to study.
