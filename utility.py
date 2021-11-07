import student as s
import manage as m


class AccountPasswordClass:

    # Checks if the password is at most 12 characters
    def check_max_characters(self, password):
        if len(password) > 12:
            print("\nPassword must be at most 12 characters. Please Try Again.")
            return False
        else:
            return True

    # Checks if the password is at least 8 characters
    def check_min_characters(self, password):
        if len(password) < 8:
            print("\nPassword must be at least 8 characters. Please Try Again.")
            return False
        else:
            return True

    # Checks if the password has an Upper case letter
    def check_Uppercase_letter(self, password):
        if not any(character.isupper() for character in password):
            print("\nPassword must have an Uppercase letter. Please Try Again.")
            return False
        else:
            return True

    # Checks if the password has a non-alphabetic character
    def check_non_alpha(self, password):
        if password.isalnum():
            print("\nThe password needs a non-alphabetic character. Please Try Again.")
            return False
        else:
            return True

    # Checks if the password has a digit
    def check_digit(self, password):
        if not any(character.isdigit() for character in password):
            print("\nThe password needs a digit. Please Try Again.")
            return False
        else:
            return True


class AccountExistClass:
    def check_name(self, user_name):
        manage = m.Manage()
        for item in manage.get_list():
            if item.get_user_name() == user_name:
                return True
        print("\nThere is no account with this name.")
        return False

    def check_password(self, user_name, password):
        manage = m.Manage()
        for item in manage.get_list():
            if item.get_user_name() == user_name and item.get_password() == password:
                return True
        return False


class InputValueClass:
    # Checks if the value is an integer
    def check_isInteger(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        # Checks if the value is number

    def check_isNumber(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


# Utility function to check if the user inputted a value 1-5
def checkUserInput(inputValue, low_val, high_val):
    user_value = InputValueClass()
    while not user_value.check_isInteger(inputValue) or int(inputValue) < low_val or int(inputValue) > high_val:
        print("")
        print("You must type a value between " + str(low_val) + " - " + str(high_val) + ". Please try again.")
        inputValue = input("\nYour selection: ")
    return inputValue
