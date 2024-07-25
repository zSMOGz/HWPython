def single_root_words(root_word: str, *other_words: str):
    same_words = []
    for word in other_words:
        if (word.lower().find(root_word.lower()) != -1
                or root_word.lower().find(word.lower()) != -1):
            same_words.append(word)

    return same_words


result1 = single_root_words('rich',
                            'richiest',
                            'orichalcum',
                            'cheers',
                            'richies')
result2 = single_root_words('Disablement',
                            'Able',
                            'Mable',
                            'Disable',
                            'Bagel')
print(result1)
print(result2)