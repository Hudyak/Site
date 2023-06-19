while True:
    #Вводим палиндром:
    palindrome = input('Введите слово или число: ')
    #Используем p для отзеркаливанья текста
    p = palindrome[::-1]
    #Проверяем, схожи ли palindrome и p
    if palindrome == p:
        print('Это палиндром')
    elif palindrome != p:
        print('Это не палиндром')
