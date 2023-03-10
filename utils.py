import string
import sort as s
import re

def get_chars(word):
    return [*word]

def chars_to_number(chars):
    value = []

    for char in chars:
        value.append(ord(char))
    return  value

def number_to_chars(numbers):
    value = []

    for number in numbers:
        value.append(chr(number))
    return  value

def get_words(sentence, numbers):

    arr = str(sentence).split()
    pattern = r"[^a-zA-Z\-\.]"
    patternNoDots = r"[^a-zA-Z\-]"

    if numbers:
        try:
            for index in range(len(arr)):
                try:
                    float(arr[index])
                except:
                    arr[index] = re.sub(pattern, "", str(arr[index])).lower().capitalize()
        except:
            print("error in utils.get_words")
    else:
        try:
            for index in range(len(arr)):
                arr[index] = re.sub(patternNoDots, "", str(arr[index])).lower().capitalize().translate(str.maketrans('', '', string.digits))
                print(arr[index])
        except:
            print("error in utils.get_words")

    while("" in arr):
        arr.remove("")
    
    return arr

def sort(sentence, dedupe=False,  numbers=True):
    value = get_words(sentence, numbers)
    if dedupe:
        value = list(dict.fromkeys(value))
        
    print("It took " + str(s.merge_sort(value)) + "s to complete the operation.")

    return value

# def sort_sentence(sentence):

         