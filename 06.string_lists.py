def is_palindrome(word: str): return word.lower() == ''.join(reversed(word.lower()))


if __name__ == '__main__':
    user_word = input('Please input a word or short phrase: ')
    if is_palindrome(user_word):
        print(f'{user_word} is a palindrome')
    else:
        print(f'{user_word} is not a palindrome')
