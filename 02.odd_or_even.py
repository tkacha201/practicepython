def odd_or_even(num: int):
    if num % 4 == 0:
        return f'{num} is a multiple of four.'
    elif num % 2 == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd.'


if __name__ == '__main__':
    while True:
        try:
            user_num = (input('Please input a whole number: '))
            assert user_num.isdigit()
            user_num = int(user_num)
            break
        except AssertionError:
            print('You did not input a whole number.')

    print(odd_or_even(user_num))
