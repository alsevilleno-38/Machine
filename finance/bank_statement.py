def process_payments(principal, interest, num_years):
    return principal * interest * num_years

def convert_to_decimal_percentage(per_str):    
    per_index = per_str.find("%")
    # returns 0 if there is character after % which indicates invalid value
    try:
        per_str[per_index + 1]
        return 0
    except IndexError:    
        try:
            return float(per_str[:per_index]) / 100
        except ValueError as e:
            return 0


if __name__ == '__main__':
    # print("processing bank statements...")
    # print("[bank_statement] main function")
    print(convert_to_decimal_percentage("45%"))