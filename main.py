import finance.bank_statement as b


if __name__ == "__main__":
    my_interest_str = input("Please input a percentage: ")
    try:
        my_interest = float(my_interest_str)
    except ValueError:
        my_interest = b.convert_to_decimal_percentage(my_interest_str)

    due_to_pay = b.process_payments(1950, my_interest, 1)

    #if float is an integer then remove decimal point
    if float.is_integer(due_to_pay) :
        due_to_pay_display = int(due_to_pay)
    else:
        due_to_pay_display = due_to_pay

    print(f"Your bill is {due_to_pay_display}")