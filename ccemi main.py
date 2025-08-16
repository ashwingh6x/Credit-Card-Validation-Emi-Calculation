# -------------------------------------------------------------
# Project: Credit Card Validation and EMI Calculator
# Author : Ashwin G
# Language: Python
# Date   : 2025-08-17
# Description:
#   This Python project validates credit card numbers using
#   the Luhn Algorithm and calculates EMI (Equated Monthly 
#   Installment) based on principal, interest rate, and tenure.
#
# Features:
#   • Validates credit card numbers for correctness
#   • Calculates EMI, total payment, and total interest
#   • User-friendly interactive console program
# -------------------------------------------------------------



# Fancy Header definition
def fancy_header(text):
    border = "╔" + "═" * (len(text) + 2) + "╗"
    middle = f"║ {text} ║"
    footer = "╚" + "═" * (len(text) + 2) + "╝"
    print("\n" + border)
    print(middle)
    print(footer)

# Luhn Algorithm for Credit Card Validation definition
def vcard(cardno):
    cardno = cardno.replace(" ", "").replace("-", "")
    if not cardno.isdigit():
        return False

    total = 0
    revdigits = cardno[::-1]

    for i in range(len(revdigits)):
        digit = int(revdigits[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total = total + digit

    return total % 10 == 0

# Emi Calculation definition
def calcemi(principal, intrate, months):
    interest_rate = ((principal * intrate) / 100)
    emi_permonth = (interest_rate + principal) / months
    total_payment = principal + interest_rate
    total_interest = total_payment - principal
    return round(emi_permonth, 2), round(total_payment, 2), round(total_interest, 2)

# Main Program and calling functions

fancy_header("Credit Card Validation and EMI Calculator")
def main():
    print("*************************************************")
    card = input("Enter your credit card number: ")

    if vcard(card):
        print("✅ Valid Credit Card")
        print("Do you want to calculate EMI?")
        value = input("Type 'emi' to Proceed or Enter '0' to Exit: ")
        if value == "0":
            print("Thank you for using our services. Goodbye!")
            exit()
        if value == "emi":
                amount = float(input("Enter the amount (₹): "))
                rate = float(input("Enter fixed interest rate (%): "))
                tenure = int(input("Enter tenure (months): "))
                emi, total, interest = calcemi(amount, rate, tenure)
                print("\n📊 EMI Calculation:")
                print(f"👉 EMI per month: ₹{emi}")
                print(f"💰 Total amount payable: ₹{total}")
                print(f"📈 Total interest payable: ₹{interest}")
    else:
        print("❌ Invalid Credit Card Number")

while True:
    main()
    choice = input("Press 'Enter' to validate again or Enter '0' to Exit: ")
    if choice == "0":
        print("Thank you for using our services. Goodbye!")
        break

# End of the program

