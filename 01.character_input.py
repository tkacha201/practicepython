import datetime


def char_input(age: int) -> int:
    current_date = datetime.datetime.today()
    current_year = current_date.year
    birth_year = current_year - age
    return birth_year + 100


if __name__ == '__main__':
    while True:
        try:
            user_age = int(input('Please input your age: '))
            break
        except ValueError:
            print('You did not enter a whole number')

    year_100 = char_input(user_age)
    print(f'You will be 100 years old in {year_100}')
