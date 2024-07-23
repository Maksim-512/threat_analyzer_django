import nltk
import string
from nltk.stem import SnowballStemmer


def device_detection(text_input, word_list):
    '''Из введённого пользователем текста определяем какие устройства были введены'''

    stemmer_ru = SnowballStemmer('russian')

    text_input = text_input.translate(str.maketrans({char: ' ' for char in string.punctuation if char != '-'}))

    tokens = nltk.word_tokenize(text_input)

    stemmed_words = []

    for word in tokens:
        stemmed_words.append(stemmer_ru.stem(word.lower()))

    devices = []
    for w in word_list:
        w_mix = w.translate(str.maketrans({char: ' ' for char in string.punctuation if char != '-'}))
        stemmed_w = []
        for word in w_mix.split():
            stemmed_w.append(stemmer_ru.stem(word.lower()))
        if all(word in stemmed_words for word in stemmed_w):
            devices.append(w)

    return devices