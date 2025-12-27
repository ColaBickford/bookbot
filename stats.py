from collections import Counter

def get_num_words(document_text):
    return len(document_text.split())

def character_repeat_count(document_text):
    char_count_dict = {}
    lowercasing_text = document_text.lower()
    for char in lowercasing_text:
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    sorted_by_freq = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_by_freq
    
