def try_int(input_user):
    imp_correct = False
    try:
        # Convert the string to an integer
        integer_number = int(input_user)
        print(f"The integer value is: {integer_number}")
        imp_correct = True
    except ValueError:
        print("The string is not a valid integer.")
    return imp_correct