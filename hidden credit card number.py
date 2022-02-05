credit_card_number = str(input("enter your 16 digit credit card:"))
if len(credit_card_number) > 16:
    print("you have entered more than 16 digits")
elif len(credit_card_number) < 16:
    print("you have entered less than 16 digits")
elif len(credit_card_number) == 16:
    dash = "*" * 12
    print(dash + credit_card_number)[-4:]
