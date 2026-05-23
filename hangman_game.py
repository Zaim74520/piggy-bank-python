import random
import sys
import os
print("Текущая рабочая директория:", os.getcwd())
print("Файлы в папке:", os.listdir(os.getcwd()))

   


def load_words():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        if not words:
            print("Ошибка: файл 'words.txt' пуст.")
            sys.exit(1)
        return words
    except FileNotFoundError:
        print("Ошибка: файл 'words.txt' не найден.")
        sys.exit(1)


def play_hangman():
    words_list = load_words()
    secret_word = random.choice(words_list)
    guessed_letters = []
    attempts = 6

    print("Добро пожаловать в игру 'Виселица'!")
    print(f"У вас {attempts} попыток, чтобы угадать слово.")

    while attempts > 0:
        # Показываем текущее состояние слова (угаданные буквы и подчёркивания)
        display_word = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_'
        print(f"\nТекущее слово: {display_word}")
        print(f"Использованные буквы: {', '.join(guessed_letters)}")
        print(f"Осталось попыток: {attempts}")

        # Проверка победы
        if '_' not in display_word:
            print(f"\nПоздравляем! Вы угадали слово: {secret_word}")
            return

        # Ввод буквы
        guess = input("\nВведите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Такой буквы нет в слове.")
        else:
            print("Правильно! Эта буква есть в слове.")

    # Конец игры — проигрыш
    print(f"\nВы проиграли! Загаданное слово было: {secret_word}")


# Запуск игры
if __name__ == "__main__":
    while True:
        play_hangman()  # Сначала запускаем игру
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()  # Спрашиваем про повтор
        if play_again != 'да':  # Если ответ не «да»
            print("Спасибо за игру! До новых встреч!")  # Прощаемся
            break  # Выходим из цикла — программа завершается

