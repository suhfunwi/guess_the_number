import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    while True:
        try:
            number = int(
                input('Please enter an integer number. You have as many tries as you need to enter a number: '))
            # whatever the user enters will be stored in the variable 'number'
            print(f'Thank you for entering the number {number}')
            break
    #         if there is a number, no need to repeat the loop anymore
        except ValueError:
    #         if there is no number, the line with int() raises a
    #         ValueError and this block of code runs
            print('That was not an integer number. Try again.')
    # since it's a while True loop, it will repeat and ask the user again.
    print(f'The number you entered was {number}')

    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
