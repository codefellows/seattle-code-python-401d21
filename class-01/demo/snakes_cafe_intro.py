
appetizers = ['Wings', 'Cookies', "Spring Rolls"]


def print_intro():
    # print("**************************************")
    # print("**    Welcome to the Snakes Cafe!   **")
    # print("**    Please see our menu below.    **")
    # print("**")
    # print('** To quit at any time, type "quit" **')
    # print("**************************************")

    # Appetizers
    # ----------
    # Wings
    # Cookies
    # Spring Rolls
    #
    # Entrees
    # -------
    # Salmon
    # Steak
    # Meat
    # Tornado
    # A Literal Garden
    #
    # Desserts
    # --------
    # Ice
    # Cream
    # Cake
    # Pie
    #
    # Drinks
    # ------
    # Coffee
    # Tea

    print('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    ''')
    # print("*" * 38)


def get_user_input():
    user_input = input("> ")
    return user_input


def quit_application():
    print("Thank you for using the Snakes Cafe!")


if __name__ == '__main__':
    print_intro()
    input_selection = get_user_input()
    while input_selection.lower() != "quit":

        if input_selection in appetizers:
            print(input_selection)

            # TODO: Find a way to track the totals

        else:
            print("Sorry, That items is not in the list.")
            # TODO: Re ask for input


    quit_application()


