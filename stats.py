def get_num_words(book_words):
    return len(book_words.split())

def get_letter_occurrence(letters):
    letter_found = {}
    for letter in letters:
        try:
            letter_found[letter.lower()] += 1
        except KeyError:
            letter_found[letter.lower()] = 1
    return letter_found

def get_key(dictionary):
    return dictionary["num"]

def get_sorted_dict(dictionary):
    list_of_dict = []
    for letter in dictionary:
        if letter.isalpha():
            temp_dict = {
                "char" : letter,
                "num" : dictionary[letter]
                }
            list_of_dict.append(temp_dict)
        else:
            continue
    list_of_dict.sort(key=get_key, reverse=True)
    return list_of_dict
        