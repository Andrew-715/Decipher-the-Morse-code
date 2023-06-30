from random import choice

list_words = ['bird', 'apple', 'tiger', 'pencil', 'purple']
answers = []

print('Сегодня мы потренируемся расшифровывать морзянку.')
input('Нажмите Enter и начнём!')


def morse_encode(word):
    morse_dictionary = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }

    morse = ''

    for k, v in morse_dictionary.items():
        for k in word:
            morse = morse + morse_dictionary[k] + ' '
        return morse


def get_random_word():
    randoms = choice(list_words)
    return randoms


def print_statistics(answers):
    correct_answers = 0
    wrong_answers = 0

    for i in answers:
        if i == True:
            correct_answers += 1
        else:
            wrong_answers += 1

    print(f'Всего задачек: {len(answers)}')
    print(f'Верно отвечено: {correct_answers}')
    print(f'Неверно отвечено: {wrong_answers}')
    print('Спасибо за игру!')


for i in range(len(list_words)):
    random_word = get_random_word()
    print(f'Слово {i + 1} - {morse_encode(random_word)}')

    if input() == random_word:
        print(f'Верно, {random_word}!')
        answers.append(True)
    else:
        print(f'Неверно, {random_word}!')
        answers.append(False)

print(print_statistics(answers))
