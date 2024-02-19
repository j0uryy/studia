import random


def get_difficulty():
    print('Wybierz poziom trudności:')
    print('1. Łatwy. (Ilość prób - 2; Zakres liczby: 1-9)')
    print('2. Średni. (Ilość prób - 5; Zakres liczby: 10-99)')
    print('3. Trudny. (Ilość prób - 8; Zakres liczby: 100-999)')
    difficulty = int(input('Wpisz liczbe odpowiadającą poziomowi trudności: '))
    while difficulty < 1 or difficulty > 3:
        difficulty = int(input('Zła liczba! Wpisz liczbe odpowiadającą poziomowi trudności: '))
    return difficulty


def set_difficulty_properties(difficulty):
    match difficulty:
        case 1:
            tries = 2
            num_min = 1
            num_max = 9
        case 2:
            tries = 5
            num_min = 10
            num_max = 99
        case 3:
            tries = 8
            num_min = 100
            num_max = 999
    return tries, num_min, num_max


def run_game(tries, num_min, num_max, num_to_guess):
    while True:
        guess = int(input(f'Odgadnij liczbę między {num_min} a {num_max}: '))
        while guess < num_min or guess > num_max:
            guess = int(input(f'Zła liczba! Odgadnij liczbę między {num_min} a {num_max}: '))

        if guess == num_to_guess:
            print(f'Udało ci się odgadnąć liczbę! Była to liczba {num_to_guess}')
            break
        elif guess > num_to_guess:
            print(f'Twoja liczba {guess} jest za duża!')
        elif guess < num_to_guess:
            print(f'Twoja liczba {guess} jest za mała!')
        tries -= 1
        if tries == 0:
            print('Skończyły ci się próby! koniec gry')
            print(f'Sekretną liczbą było: {num_to_guess}')
            break


def main():
    print('Witam w grze "Sekretna liczba".')
    difficulty = get_difficulty()
    tries, num_min, num_max = set_difficulty_properties(difficulty)
    num_to_guess = random.randint(num_min, num_max)
    run_game(tries, num_min, num_max, num_to_guess)


if __name__ == '__main__':
    main()