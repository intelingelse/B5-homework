def take_valid_input():
    """
    takes and validates input from the user
    :return: valid input of type: INT
    """

    # validating the user input for the number of iterations
    while True:  # this loop can run forever, basically
        try:
            # converting number to int
            iter_number = int((input("Enter the number of iterations to be considered:\n>>>> ")))
            return iter_number
            break
        # if number cannot be converted from string to int type i.e. float char or string type values were passed
        # we will print the capitalized exception string and will ask user to try again
        except ValueError as e:
            print(str(e).capitalize())
            print("Try again.")
            continue
