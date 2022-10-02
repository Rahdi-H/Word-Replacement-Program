def word_replacement():
    strr = "hi im name is Rahdi"
    print(strr)

    word_to_replace = input('enter the word you want to replace: ')
    replace_by = input('enter the word you want to replace by: ')
    print(strr.replace(word_to_replace, replace_by))


word_replacement()