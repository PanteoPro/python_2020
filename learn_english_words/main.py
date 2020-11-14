import eel
import random
import os


FILENAME = "data.txt"


class DateManager:


    def __init__(self, filename):
        self._words = []
        self._filename = filename


    def load_data(self):
        with open(self._filename, "r", encoding="utf-8") as f:
            for line in f:
                self._words.append(line.replace("\n", "").split(" "))
            self._words = self._words
    

    def save_data(self, word_ru, word_en):
        self._words.append([word_ru, word_en])
        with open(self._filename, "a", encoding="utf-8") as f:
            print(word_ru, word_en, file=f)
    

    def get_words(self):
        return self._words
    

    def shuffle(self):
        random.shuffle(self._words)
    

    def is_have(self, word_ru, word_en):
        for rus, eng in self._words:
            if rus == word_ru or eng == word_en:
                return True
        return False





@eel.expose
def add_word(word_ru:str, word_en:str):
    word_ru = word_ru.strip().lower()
    word_en = word_en.strip().lower()

    flag = not manager.is_have(word_ru, word_en)
    
    if flag:
        manager.save_data(word_ru, word_en)
    return flag


@eel.expose
def get_words():
    return manager.get_words()


@eel.expose
def test(text):
    print(text)


@eel.expose
def equal_words(word1:str, word2:str):
    if word1.strip().lower() == word2.strip().lower():
        return True
    return False


@eel.expose
def shuffle():
    manager.shuffle()



manager = DateManager(FILENAME)
manager.load_data()

eel.init("web")
eel.start("index.html", size = (700,700))