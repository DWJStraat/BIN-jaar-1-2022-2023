import pickle

def main():
    """
    This function will load a dictionary from a pickle file and print it.

    Funniest thing I've ever seen

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    try:
        with open('pickled_veggies.dat', 'rb') as file:
            veggies = pickle.load(file)
    except FileNotFoundError:
        veggies = {}
    print(veggies)
    choice1 = input('Would you like to add a vegetable? (y/n)')
    if choice1 == 'y':
        veggie = input('What vegetable would you like to add?')
        price = input('What is the price of this vegetable?')
        veggies[veggie] = price
        with open('pickled_veggies.dat', 'wb') as file:
            pickle.dump(veggies, file)
    choice2 = input('Would you like to change the price of a vegetable? (y/n)')
    if choice2 == 'y':
        veggie = input('What vegetable would you like to change the price of?')
        price = input('What is the new price of this vegetable?')
        veggies[veggie] = price
        with open('pickled_veggies.dat', 'wb') as file:
            pickle.dump(veggies, file)
    choice3 = input('Would you like to delete a vegetable? (y/n)')
    if choice3 == 'y':
        veggie = input('What vegetable would you like to delete?')
        del veggies[veggie]
        with open('pickled_veggies.dat', 'wb') as file:
            pickle.dump(veggies, file)
    print(veggies)
    print('Closing program')
main()