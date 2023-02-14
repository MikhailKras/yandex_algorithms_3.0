def get_most_frequent_word(words):
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    max_val = 0
    for word in words:
        if words_dict[word] > max_val:
            max_val = words_dict[word]
    for word in sorted(words):
        if words_dict[word] == max_val:
            return word


if __name__ == '__main__':
    in_words_lst = input().split()
    print(get_most_frequent_word(in_words_lst))
